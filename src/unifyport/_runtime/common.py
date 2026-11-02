"""Shared validation, request preparation, retry, and response decoding."""

from __future__ import annotations

import inspect
import ipaddress
import json
import math
import random
import re
from collections.abc import Awaitable, Iterable, Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from typing import Any, Protocol, TypeGuard, TypeVar
from urllib.parse import quote, unquote, urlsplit, urlunsplit

import httpx

from ..config import (
    MAX_RESPONSE_BYTES,
    MAX_RETRIES,
    MAX_TIMEOUT,
    AsyncDeviceClientConfig,
    AsyncSecretSource,
    DeviceClientConfig,
    RequestOptions,
    RequestOptionsInput,
    RetryConfig,
    SecretSource,
    SyncSecretSource,
)
from ..errors import (
    UnifyPortApiError,
    UnifyPortConfigurationError,
    UnifyPortError,
    UnifyPortResponseParseError,
)
from ..result import ApiResult

T = TypeVar("T")

RETRYABLE_STATUSES = frozenset({408, 429, 502, 503, 504})
FORBIDDEN_REQUEST_HEADERS = frozenset(
    {"authorization", "proxy-authorization", "cookie", "x-api-key"}
)
_DIAGNOSTIC = re.compile(r"^[A-Za-z0-9_.:/-]+$")
_PATH_PLACEHOLDER = re.compile(r"\{([^{}]+)\}")
_CONTROL_CHARACTER = re.compile(r"[\x00-\x1f\x7f]")

# HTTPX 已把请求配置错误隔离在 TransportError 之外；policy-safe operation 可重试其全部子类。
RETRYABLE_NETWORK_ERRORS = (httpx.TransportError,)


class OperationSpecLike(Protocol):
    """Runtime-facing subset of generated operation metadata."""

    @property
    def operation_id(self) -> str: ...

    @property
    def http_method(self) -> str: ...

    @property
    def path(self) -> str: ...

    @property
    def path_params(self) -> tuple[ParameterSpecLike, ...]: ...

    @property
    def query_params(self) -> tuple[ParameterSpecLike, ...]: ...

    @property
    def header_params(self) -> tuple[ParameterSpecLike, ...]: ...

    @property
    def request_body(self) -> str | None: ...

    @property
    def request_body_required(self) -> bool: ...

    @property
    def retryable(self) -> bool: ...


class ParameterSpecLike(Protocol):
    """Runtime-facing subset of generated parameter metadata."""

    @property
    def name(self) -> str: ...

    @property
    def python_name(self) -> str: ...

    @property
    def required(self) -> bool: ...


@dataclass(frozen=True, slots=True)
class NormalizedConfig:
    base_url: str
    base_origin: tuple[str, str, int | None]
    base_path: str
    api_key: SecretSource
    timeout: float
    retry: RetryConfig
    max_response_bytes: int


@dataclass(frozen=True, slots=True)
class CallSettings:
    timeout: float
    max_retries: int


@dataclass(frozen=True, slots=True)
class PreparedOperation:
    operation_id: str
    method: str
    url: str
    query: tuple[tuple[str, str], ...]
    headers: tuple[tuple[str, str], ...]
    content: bytes | None
    retryable: bool


class CredentialProviderFailure(Exception):
    """Internal marker that deliberately carries no provider exception."""

    __slots__ = ()


def normalize_config(config: DeviceClientConfig | AsyncDeviceClientConfig) -> NormalizedConfig:
    if not isinstance(config, (DeviceClientConfig, AsyncDeviceClientConfig)):
        raise UnifyPortConfigurationError("config", "has an unsupported type")
    if not isinstance(config.allow_insecure_http, bool):
        raise UnifyPortConfigurationError("allow_insecure_http", "must be a boolean")
    base_url, origin, base_path = _normalize_base_url(
        config.base_url,
        allow_insecure_http=config.allow_insecure_http,
    )
    timeout = _positive_finite_number(config.timeout, "timeout", maximum=MAX_TIMEOUT)
    retry = normalize_retry_config(config.retry)
    maximum_bytes = _integer(config.max_response_bytes, "max_response_bytes", minimum=1)
    if maximum_bytes > MAX_RESPONSE_BYTES:
        raise UnifyPortConfigurationError(
            "max_response_bytes", f"must not exceed {MAX_RESPONSE_BYTES}"
        )
    if not isinstance(config.api_key, str) and not callable(config.api_key):
        raise UnifyPortConfigurationError("api_key", "must be a string or zero-argument provider")
    return NormalizedConfig(
        base_url=base_url,
        base_origin=origin,
        base_path=base_path,
        api_key=config.api_key,
        timeout=timeout,
        retry=retry,
        max_response_bytes=maximum_bytes,
    )


def build_sync_client_config(
    config: DeviceClientConfig | None,
    *,
    base_url: str | None,
    api_key: SyncSecretSource | None,
    timeout: float | None,
    retry: RetryConfig | Mapping[str, object] | None,
    max_response_bytes: int | None,
    allow_insecure_http: bool | None,
) -> DeviceClientConfig:
    direct_values = (
        base_url,
        api_key,
        timeout,
        retry,
        max_response_bytes,
        allow_insecure_http,
    )
    if config is not None:
        if any(value is not None for value in direct_values):
            raise UnifyPortConfigurationError(
                "config", "cannot be combined with direct constructor fields"
            )
        return config
    if base_url is None:
        raise UnifyPortConfigurationError("base_url", "is required")
    if api_key is None:
        raise UnifyPortConfigurationError("api_key", "is required")
    if allow_insecure_http is not None and not isinstance(allow_insecure_http, bool):
        raise UnifyPortConfigurationError("allow_insecure_http", "must be a boolean")
    normalized_retry = normalize_retry_config(retry)
    defaults = DeviceClientConfig(base_url=base_url, api_key=api_key)
    return DeviceClientConfig(
        base_url=base_url,
        api_key=api_key,
        timeout=defaults.timeout if timeout is None else timeout,
        retry=normalized_retry,
        max_response_bytes=(
            defaults.max_response_bytes if max_response_bytes is None else max_response_bytes
        ),
        allow_insecure_http=False if allow_insecure_http is None else allow_insecure_http,
    )


def build_async_client_config(
    config: AsyncDeviceClientConfig | None,
    *,
    base_url: str | None,
    api_key: AsyncSecretSource | None,
    timeout: float | None,
    retry: RetryConfig | Mapping[str, object] | None,
    max_response_bytes: int | None,
    allow_insecure_http: bool | None,
) -> AsyncDeviceClientConfig:
    direct_values = (
        base_url,
        api_key,
        timeout,
        retry,
        max_response_bytes,
        allow_insecure_http,
    )
    if config is not None:
        if any(value is not None for value in direct_values):
            raise UnifyPortConfigurationError(
                "config", "cannot be combined with direct constructor fields"
            )
        return config
    if base_url is None:
        raise UnifyPortConfigurationError("base_url", "is required")
    if api_key is None:
        raise UnifyPortConfigurationError("api_key", "is required")
    if allow_insecure_http is not None and not isinstance(allow_insecure_http, bool):
        raise UnifyPortConfigurationError("allow_insecure_http", "must be a boolean")
    normalized_retry = normalize_retry_config(retry)
    defaults = AsyncDeviceClientConfig(base_url=base_url, api_key=api_key)
    return AsyncDeviceClientConfig(
        base_url=base_url,
        api_key=api_key,
        timeout=defaults.timeout if timeout is None else timeout,
        retry=normalized_retry,
        max_response_bytes=(
            defaults.max_response_bytes if max_response_bytes is None else max_response_bytes
        ),
        allow_insecure_http=False if allow_insecure_http is None else allow_insecure_http,
    )


def normalize_retry_config(value: RetryConfig | Mapping[str, object] | None) -> RetryConfig:
    if value is None:
        value = RetryConfig()
    elif isinstance(value, Mapping):
        unknown = set(value) - {"max_retries", "base_delay", "max_delay"}
        if unknown:
            raise UnifyPortConfigurationError("retry", "contains unsupported fields")
        defaults = RetryConfig()
        mapped_retries = _integer(
            value.get("max_retries", defaults.max_retries),
            "retry.max_retries",
            minimum=0,
        )
        mapped_base_delay = _positive_finite_number(
            value.get("base_delay", defaults.base_delay), "retry.base_delay"
        )
        mapped_max_delay = _positive_finite_number(
            value.get("max_delay", defaults.max_delay), "retry.max_delay"
        )
        value = RetryConfig(
            max_retries=mapped_retries,
            base_delay=mapped_base_delay,
            max_delay=mapped_max_delay,
        )
    if not isinstance(value, RetryConfig):
        raise UnifyPortConfigurationError("retry", "must be a RetryConfig")
    max_retries = _integer(value.max_retries, "retry.max_retries", minimum=0)
    if max_retries > MAX_RETRIES:
        raise UnifyPortConfigurationError("retry.max_retries", f"must not exceed {MAX_RETRIES}")
    base_delay = _positive_finite_number(value.base_delay, "retry.base_delay")
    max_delay = _positive_finite_number(value.max_delay, "retry.max_delay")
    return RetryConfig(
        max_retries=max_retries,
        base_delay=base_delay,
        max_delay=max_delay,
    )


def resolve_call_settings(
    options: RequestOptionsInput,
    config: NormalizedConfig,
    *,
    retryable: bool,
) -> CallSettings:
    normalized = _coerce_request_options(options)
    if normalized.retry is not None and not isinstance(normalized.retry, bool):
        raise UnifyPortConfigurationError("options.retry", "must be a boolean")
    timeout = config.timeout
    if normalized.timeout is not None:
        requested_timeout = _positive_finite_number(
            normalized.timeout,
            "options.timeout",
            maximum=MAX_TIMEOUT,
        )
        # 单次调用只能缩短全局 deadline，较大的值不会延长 logical operation。
        timeout = min(timeout, requested_timeout)

    requested_retries = normalized.max_retries
    if normalized.retry is False:
        requested_retries = 0
    elif normalized.retry is True:
        # True 不能给 policy 未授权的 operation 开启重试，也不代表扩大预算。
        requested_retries = config.retry.max_retries
    if requested_retries is not None:
        requested_retries = _integer(
            requested_retries,
            "options.max_retries",
            minimum=0,
        )
    maximum_retries = (
        0
        if not retryable
        else min(config.retry.max_retries, requested_retries or 0)
        if requested_retries is not None
        else config.retry.max_retries
    )
    return CallSettings(timeout=timeout, max_retries=maximum_retries)


def prepare_operation(
    spec: OperationSpecLike,
    config: NormalizedConfig,
    *,
    path_params: Mapping[str, object] | None,
    query: Mapping[str, object] | None,
    body: object | None,
    headers: Mapping[str, str] | None,
) -> PreparedOperation:
    operation_id = safe_diagnostic(spec.operation_id, maximum=128)
    if operation_id is None:
        raise UnifyPortConfigurationError("operation_id", "is invalid")
    method = spec.http_method.upper()
    if method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        raise UnifyPortConfigurationError("operation method", "is unsupported")
    path = _build_path(spec, path_params)
    url = f"{config.base_url}{path}"
    _ensure_target_inside_base(url, config)
    normalized_query = _normalize_query(spec, query)
    normalized_headers = _normalize_headers(spec, headers)
    content = _serialize_body(spec, body)
    return PreparedOperation(
        operation_id=operation_id,
        method=method,
        url=url,
        query=normalized_query,
        headers=normalized_headers,
        content=content,
        retryable=spec.retryable,
    )


def credential_headers(
    source: Iterable[tuple[str, str]],
    credential: str,
) -> dict[str, str]:
    headers = {
        name: value for name, value in source if name.lower() not in FORBIDDEN_REQUEST_HEADERS
    }
    # credential 只在 logical operation 内注入，retry 共用同一份已解析值。
    headers["X-Api-Key"] = credential
    return headers


def validate_credential(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise UnifyPortConfigurationError("api_key", "provider returned an empty value")
    if _CONTROL_CHARACTER.search(value):
        raise UnifyPortConfigurationError("api_key", "provider returned an invalid header value")
    invalid_encoding = False
    try:
        value.encode("ascii")
    except UnicodeEncodeError:
        invalid_encoding = True
    if invalid_encoding:
        # UnicodeEncodeError.object 会保留完整 credential，必须离开 handler 后再抛公开错误。
        raise UnifyPortConfigurationError("api_key", "provider returned an invalid header value")
    return value


def sync_credential_source(source: SecretSource) -> str:
    if isinstance(source, str):
        value: object = source
    else:
        failed = False
        try:
            value = source()
        except Exception:
            failed = True
            value = None
        if failed:
            # provider 异常可能携带 secret，因此跨过 except 边界后只抛无内容 marker。
            raise CredentialProviderFailure
    if inspect.isawaitable(value):
        # sync client 不隐式启动 event loop，避免 credential provider 的线程与取消语义失控。
        if inspect.iscoroutine(value):
            value.close()
        raise UnifyPortConfigurationError(
            "api_key", "async providers require AsyncUnifyPortDeviceClient"
        )
    return validate_credential(value)


async def async_credential_source(source: SecretSource) -> str:
    failed = False
    try:
        value: object = source if isinstance(source, str) else source()
        if is_awaitable(value):
            value = await value
    except Exception:
        failed = True
        value = None
    if failed:
        raise CredentialProviderFailure
    return validate_credential(value)


def is_awaitable(value: object) -> TypeGuard[Awaitable[object]]:
    return inspect.isawaitable(value)


def response_outcome(
    *,
    operation_id: str,
    status: int,
    headers: Iterable[tuple[str, str]],
    body: bytes,
) -> ApiResult[Any] | UnifyPortError:
    header_request_id = response_request_id(headers)
    parsed, parse_failed = _parse_json_body(body)
    if 200 <= status < 300:
        if parse_failed:
            return UnifyPortResponseParseError(
                operation_id=operation_id,
                status=status,
                request_id=header_request_id,
            )
        request_id = request_id_from(parsed) or header_request_id
        return ApiResult(
            data=parsed,
            status=status,
            request_id=request_id,
        )

    code = f"HTTP_{status}"
    numeric_code = None
    if isinstance(parsed, Mapping):
        nested = parsed.get("error")
        candidate = nested if isinstance(nested, Mapping) else parsed
        # 严格 ASCII 五位字符串，错误元数据不应成为敏感输出通道。
        numeric = candidate.get("numeric_code")
        if isinstance(numeric, str) and re.fullmatch(r"[1-9][0-9]{4}", numeric):
            numeric_code = numeric
        safe_code = safe_diagnostic(candidate.get("code"), maximum=64)
        if safe_code is not None:
            code = safe_code
    request_id = request_id_from(parsed) or header_request_id
    return UnifyPortApiError(
        status=status,
        code=code,
        numeric_code=numeric_code,
        operation_id=operation_id,
        request_id=request_id,
    )


def response_request_id(headers: Iterable[tuple[str, str]]) -> str | None:
    for name, value in headers:
        if name.lower() == "x-request-id":
            # response headers 只读取 allowlist 诊断值，其他 header 从不进入 result/error。
            candidate = safe_diagnostic(value.strip(), maximum=128)
            if candidate is not None:
                return candidate
    return None


def response_has_unsupported_content_encoding(
    headers: Iterable[tuple[str, str]],
) -> bool:
    for name, value in headers:
        if name.lower() != "content-encoding":
            continue
        # identity 之外的编码可能在计数前触发透明解压，因此即使组合出现也必须拒绝。
        encodings = (encoding.strip().lower() for encoding in value.split(","))
        if any(encoding and encoding != "identity" for encoding in encodings):
            return True
    return False


def retry_delay(retry_after: str | None, attempt: int, retry: RetryConfig) -> float:
    cap = min(retry.max_delay, retry.base_delay * (2**attempt))
    random_value = random.random()
    if not math.isfinite(random_value) or random_value < 0:
        random_value = 0.0
    elif random_value >= 1:
        random_value = math.nextafter(1.0, 0.0)
    jitter = random_value * cap
    server_delay = _parse_retry_after(retry_after)
    return float(min(retry.max_delay, max(jitter, server_delay)))


def safe_diagnostic(value: object, *, maximum: int) -> str | None:
    if not isinstance(value, str) or not 0 < len(value) <= maximum:
        return None
    return value if _DIAGNOSTIC.fullmatch(value) else None


def request_id_from(value: object) -> str | None:
    if not isinstance(value, Mapping):
        return None
    return safe_diagnostic(value.get("request_id"), maximum=128) or safe_diagnostic(
        value.get("requestId"), maximum=128
    )


def _coerce_request_options(options: RequestOptionsInput) -> RequestOptions:
    if options is None:
        return RequestOptions()
    if isinstance(options, RequestOptions):
        return options
    if not isinstance(options, Mapping):
        raise UnifyPortConfigurationError("options", "must be RequestOptions or a mapping")
    unknown = set(options) - {"timeout", "max_retries", "retry"}
    if unknown:
        raise UnifyPortConfigurationError("options", "contains unsupported fields")
    raw_timeout = options.get("timeout")
    raw_max_retries = options.get("max_retries")
    raw_retry = options.get("retry")
    timeout: float | None
    if raw_timeout is None:
        timeout = None
    else:
        timeout = _positive_finite_number(raw_timeout, "options.timeout", maximum=MAX_TIMEOUT)
    max_retries: int | None
    if raw_max_retries is None:
        max_retries = None
    else:
        max_retries = _integer(raw_max_retries, "options.max_retries", minimum=0)
    if raw_retry is not None and not isinstance(raw_retry, bool):
        raise UnifyPortConfigurationError("options.retry", "must be a boolean")
    retry = raw_retry if isinstance(raw_retry, bool) else None
    conflicting = False
    try:
        normalized = RequestOptions(timeout=timeout, max_retries=max_retries, retry=retry)
    except ValueError:
        conflicting = True
        normalized = None
    if conflicting or normalized is None:
        # dataclass 的 ValueError 仍可能随未来字段携带输入，公开异常需在 handler 外创建。
        raise UnifyPortConfigurationError("options", "contains conflicting fields")
    return normalized


def _normalize_base_url(
    value: object,
    *,
    allow_insecure_http: bool,
) -> tuple[str, tuple[str, str, int | None], str]:
    if not isinstance(value, str) or _CONTROL_CHARACTER.search(value) or "\\" in value:
        raise UnifyPortConfigurationError("base_url", "must be an absolute URL")
    parse_failed = False
    parsed = None
    host = None
    port = None
    username = None
    password = None
    try:
        parsed = urlsplit(value)
        host = parsed.hostname
        port = parsed.port
        username = parsed.username
        password = parsed.password
    except ValueError:
        parse_failed = True
    if parse_failed or parsed is None:
        # urllib 的 ValueError 会回显非法 port/host，离开 handler 后才能断开异常链。
        raise UnifyPortConfigurationError("base_url", "must be an absolute URL")
    scheme = parsed.scheme.lower()
    if scheme not in {"http", "https"} or not parsed.netloc or host is None:
        raise UnifyPortConfigurationError("base_url", "must be an absolute HTTP(S) URL")
    if username is not None or password is not None:
        raise UnifyPortConfigurationError("base_url", "must not contain username or password")
    if parsed.query or parsed.fragment:
        raise UnifyPortConfigurationError("base_url", "must not contain query or fragment")
    if any(character.isspace() for character in host):
        raise UnifyPortConfigurationError("base_url", "contains an invalid hostname")
    if scheme == "http" and not (allow_insecure_http and _is_loopback(host)):
        raise UnifyPortConfigurationError(
            "base_url", "must use HTTPS; loopback HTTP requires explicit opt-in"
        )
    decoded_path = unquote(parsed.path)
    if "\\" in decoded_path or any(segment in {".", ".."} for segment in decoded_path.split("/")):
        raise UnifyPortConfigurationError("base_url", "contains an unsafe path")
    base_path = parsed.path.rstrip("/")
    netloc = parsed.netloc.lower()
    normalized = urlunsplit((scheme, netloc, base_path, "", ""))
    effective_port = port if port is not None else (443 if scheme == "https" else 80)
    return normalized, (scheme, host.lower(), effective_port), base_path


def _is_loopback(host: str) -> bool:
    if host.lower() == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def _build_path(
    spec: OperationSpecLike,
    values: Mapping[str, object] | None,
) -> str:
    template = spec.path
    if not template.startswith("/") or "?" in template or "#" in template or "\\" in template:
        raise UnifyPortConfigurationError("operation path", "is invalid")
    expected = {_parameter_name(parameter) for parameter in spec.path_params}
    supplied = {} if values is None else dict(values)
    if set(supplied) - expected:
        raise UnifyPortConfigurationError("path_params", "contains unsupported fields")
    required = {
        _parameter_name(parameter)
        for parameter in spec.path_params
        if _parameter_required(parameter)
    }
    missing = required - set(supplied)
    if missing:
        raise UnifyPortConfigurationError("path_params", "is missing required fields")
    path = template
    for parameter in spec.path_params:
        name = _parameter_name(parameter)
        if name not in supplied:
            continue
        value = supplied[name]
        if not isinstance(value, (str, int)) or isinstance(value, bool):
            raise UnifyPortConfigurationError("path_params", "contains an invalid value")
        rendered = str(value)
        if not rendered or _CONTROL_CHARACTER.search(rendered):
            raise UnifyPortConfigurationError("path_params", "contains an invalid value")
        encoded = None
        try:
            encoded = quote(rendered, safe="")
        except UnicodeEncodeError:
            pass
        if encoded is None:
            # UnicodeEncodeError.object 会保留完整 path 值，因此公开异常不能在 handler 内抛出。
            raise UnifyPortConfigurationError("path_params", "contains an invalid value")
        path = path.replace(f"{{{name}}}", encoded)
    if _PATH_PLACEHOLDER.search(path):
        raise UnifyPortConfigurationError("operation path", "contains unresolved parameters")
    decoded = unquote(path)
    if any(segment in {".", ".."} for segment in decoded.split("/")):
        raise UnifyPortConfigurationError("operation path", "contains unsafe traversal")
    return path


def _normalize_query(
    spec: OperationSpecLike,
    values: Mapping[str, object] | None,
) -> tuple[tuple[str, str], ...]:
    expected = {_parameter_name(parameter) for parameter in spec.query_params}
    required = {
        _parameter_name(parameter)
        for parameter in spec.query_params
        if _parameter_required(parameter)
    }
    if values is None:
        if required:
            raise UnifyPortConfigurationError("query", "is missing required fields")
        return ()
    if set(values) - expected:
        raise UnifyPortConfigurationError("query", "contains unsupported fields")
    if required - {name for name, value in values.items() if value is not None}:
        raise UnifyPortConfigurationError("query", "is missing required fields")
    pairs: list[tuple[str, str]] = []
    for name, value in values.items():
        if value is None:
            continue
        items: Sequence[object]
        if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            items = value
        else:
            items = (value,)
        for item in items:
            pairs.append((name, _query_value(item)))
    return tuple(pairs)


def _query_value(value: object) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float) and math.isfinite(value):
        return str(value)
    if isinstance(value, str) and not _CONTROL_CHARACTER.search(value):
        invalid_encoding = False
        try:
            value.encode("utf-8")
        except UnicodeEncodeError:
            invalid_encoding = True
        if invalid_encoding:
            # surrogate 编码异常会持有原 query，必须先退出 handler 再生成公开错误。
            raise UnifyPortConfigurationError("query", "contains an invalid value")
        return value
    raise UnifyPortConfigurationError("query", "contains an invalid value")


def _normalize_headers(
    spec: OperationSpecLike,
    values: Mapping[str, str] | None,
) -> tuple[tuple[str, str], ...]:
    expected = {_parameter_name(parameter).lower() for parameter in spec.header_params}
    required = {
        _parameter_name(parameter).lower()
        for parameter in spec.header_params
        if _parameter_required(parameter)
    }
    if values is None:
        if required:
            raise UnifyPortConfigurationError("headers", "is missing required fields")
        # 禁用压缩可让 max_response_bytes 始终约束网络原始字节，而不是解压后的不受控输出。
        return (("Accept", "application/json"), ("Accept-Encoding", "identity"))
    result: list[tuple[str, str]] = [
        ("Accept", "application/json"),
        ("Accept-Encoding", "identity"),
    ]
    seen: set[str] = set()
    for name, value in values.items():
        if not isinstance(name, str):
            raise UnifyPortConfigurationError("headers", "contains an invalid name")
        lower_name = name.lower()
        if lower_name in FORBIDDEN_REQUEST_HEADERS:
            # 明确拒绝可避免调用方误以为 operation 参数已覆盖 client credential。
            raise UnifyPortConfigurationError("headers", "contains a forbidden credential field")
        if lower_name not in expected:
            raise UnifyPortConfigurationError("headers", "contains an unsupported field")
        if lower_name in seen:
            raise UnifyPortConfigurationError("headers", "contains duplicate fields")
        if not isinstance(value, str) or _CONTROL_CHARACTER.search(value) or len(value) > 8192:
            raise UnifyPortConfigurationError("headers", "contains an invalid value")
        if lower_name == "x-request-id" and safe_diagnostic(value, maximum=128) is None:
            raise UnifyPortConfigurationError("headers", "contains an invalid X-Request-Id")
        result.append((name, value))
        seen.add(lower_name)
    if required - seen:
        raise UnifyPortConfigurationError("headers", "is missing required fields")
    return tuple(result)


def _serialize_body(spec: OperationSpecLike, body: object | None) -> bytes | None:
    required = spec.request_body_required
    supported = spec.request_body is not None
    if body is None:
        if required:
            raise UnifyPortConfigurationError("body", "is required")
        return None
    if not supported:
        raise UnifyPortConfigurationError("body", "is not supported by this operation")
    serialized_body = None
    try:
        serialized = json.dumps(
            body,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
        )
        serialized_body = serialized.encode("utf-8")
    except (TypeError, ValueError, OverflowError, RecursionError, UnicodeEncodeError):
        pass
    if serialized_body is None:
        # serializer 异常可能引用 body/repr 中的 secret，公开错误必须脱离其 handler。
        raise UnifyPortConfigurationError("body", "must be JSON serializable")
    return serialized_body


def _parameter_name(parameter: ParameterSpecLike | str) -> str:
    # 兼容早期生成快照的纯字符串参数，正式生成物使用 ParameterSpec。
    return parameter if isinstance(parameter, str) else parameter.name


def _parameter_required(parameter: ParameterSpecLike | str) -> bool:
    return True if isinstance(parameter, str) else parameter.required


def _ensure_target_inside_base(url: str, config: NormalizedConfig) -> None:
    parse_failed = False
    parsed = None
    port = None
    host = None
    try:
        parsed = urlsplit(url)
        port = parsed.port
        host = parsed.hostname
    except ValueError:
        parse_failed = True
    if parse_failed or parsed is None:
        # request URL 的 port 错误可能包含敏感 path，公开错误需在 handler 外抛出。
        raise UnifyPortConfigurationError("request target", "is invalid")
    effective_port = port if port is not None else (443 if parsed.scheme == "https" else 80)
    origin = (parsed.scheme.lower(), "" if host is None else host.lower(), effective_port)
    prefix = config.base_path
    inside_path = not prefix or parsed.path == prefix or parsed.path.startswith(f"{prefix}/")
    if origin != config.base_origin or not inside_path:
        raise UnifyPortConfigurationError("request target", "is outside configured base_url")


def _parse_json_body(body: bytes) -> tuple[object | None, bool]:
    if not body or not body.strip():
        # 204 与其他合法空 2xx 都统一返回 None，不强迫调用方处理 JSON parser 异常。
        return None, False
    try:
        value = json.loads(
            body.decode("utf-8"),
            parse_constant=lambda _value: _raise_invalid_number(),
        )
        _reject_non_finite(value)
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError, RecursionError):
        return None, True
    return value, False


def _raise_invalid_number() -> object:
    raise ValueError("non-finite JSON number")


def _reject_non_finite(value: object) -> None:
    pending = [value]
    while pending:
        current = pending.pop()
        if isinstance(current, float) and not math.isfinite(current):
            raise ValueError("non-finite JSON number")
        if isinstance(current, list):
            pending.extend(current)
        elif isinstance(current, dict):
            pending.extend(current.values())


def _parse_retry_after(value: str | None) -> float:
    if value is None:
        return 0.0
    normalized = value.strip()
    try:
        seconds = float(normalized)
    except ValueError:
        seconds = -1.0
    if math.isfinite(seconds) and seconds >= 0:
        return seconds
    try:
        parsed = parsedate_to_datetime(normalized)
    except (TypeError, ValueError, OverflowError):
        return 0.0
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return max(0.0, (parsed - datetime.now(UTC)).total_seconds())


def _integer(value: object, field: str, *, minimum: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < minimum:
        raise UnifyPortConfigurationError(field, f"must be an integer >= {minimum}")
    return value


def _positive_finite_number(
    value: object,
    field: str,
    *,
    maximum: float | None = None,
) -> float:
    if (
        not isinstance(value, (int, float))
        or isinstance(value, bool)
        or not math.isfinite(value)
        or value <= 0
    ):
        raise UnifyPortConfigurationError(field, "must be a positive finite number")
    normalized = float(value)
    if maximum is not None and normalized > maximum:
        raise UnifyPortConfigurationError(field, f"must not exceed {maximum}")
    return normalized


__all__ = [
    "CallSettings",
    "CredentialProviderFailure",
    "NormalizedConfig",
    "OperationSpecLike",
    "PreparedOperation",
    "RETRYABLE_NETWORK_ERRORS",
    "RETRYABLE_STATUSES",
    "async_credential_source",
    "build_async_client_config",
    "build_sync_client_config",
    "credential_headers",
    "normalize_config",
    "normalize_retry_config",
    "prepare_operation",
    "resolve_call_settings",
    "response_has_unsupported_content_encoding",
    "response_request_id",
    "response_outcome",
    "retry_delay",
    "sync_credential_source",
]
