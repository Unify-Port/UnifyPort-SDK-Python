"""Asynchronous HTTPX runtime with the same policy as the sync client."""

from __future__ import annotations

import asyncio
import time
from collections.abc import Mapping
from typing import Any

import httpx

from ..config import AsyncDeviceClientConfig, RequestOptionsInput
from ..errors import (
    UnifyPortConfigurationError,
    UnifyPortError,
    UnifyPortNetworkError,
    UnifyPortResponseParseError,
    UnifyPortTimeoutError,
)
from ..result import ApiResult
from .common import (
    RETRYABLE_NETWORK_ERRORS,
    RETRYABLE_STATUSES,
    CredentialProviderFailure,
    OperationSpecLike,
    PreparedOperation,
    async_credential_source,
    credential_headers,
    normalize_config,
    prepare_operation,
    resolve_call_settings,
    response_has_unsupported_content_encoding,
    response_outcome,
    response_request_id,
    retry_delay,
)


class AsyncRuntime:
    """Execute generated async operations under one logical deadline."""

    __slots__ = ("_client", "_config")

    def __init__(
        self,
        config: AsyncDeviceClientConfig,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        self._config = normalize_config(config)
        self._client = httpx.AsyncClient(
            transport=transport,
            follow_redirects=False,
            trust_env=False,
            timeout=None,
            event_hooks={
                "request": [self._strip_ambient_credentials],
                "response": [self._discard_response_cookies],
            },
        )

    async def execute(
        self,
        spec: OperationSpecLike,
        *,
        path_params: Mapping[str, object] | None = None,
        query: Mapping[str, object] | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
        options: RequestOptionsInput = None,
    ) -> ApiResult[Any]:
        # 不捕获 CancelledError，让 Python task cancellation 保留原生控制流语义。
        started = time.monotonic()
        settings = resolve_call_settings(options, self._config, retryable=spec.retryable)
        deadline = started + settings.timeout
        prepared = prepare_operation(
            spec,
            self._config,
            path_params=path_params,
            query=query,
            body=body,
            headers=headers,
        )
        if time.monotonic() >= deadline:
            raise UnifyPortTimeoutError(settings.timeout, operation_id=prepared.operation_id)

        outcome: ApiResult[Any] | UnifyPortError
        timeout_context = asyncio.timeout(max(0.0, deadline - time.monotonic()))
        try:
            async with timeout_context:
                outcome = await self._perform(
                    prepared,
                    settings.max_retries,
                    deadline,
                    settings.timeout,
                )
        except TimeoutError:
            if timeout_context.expired():
                outcome = UnifyPortTimeoutError(
                    settings.timeout,
                    operation_id=prepared.operation_id,
                )
            else:
                outcome = UnifyPortNetworkError(operation_id=prepared.operation_id)
        if time.monotonic() >= deadline and not isinstance(outcome, UnifyPortTimeoutError):
            outcome = UnifyPortTimeoutError(settings.timeout, operation_id=prepared.operation_id)
        if isinstance(outcome, UnifyPortError):
            raise outcome from None
        return outcome

    async def aclose(self) -> None:
        await self._client.aclose()

    async def _strip_ambient_credentials(self, request: httpx.Request) -> None:
        # HTTPX 会合并内部 cookie jar；SDK 只允许显式的 X-Api-Key credential 上线。
        for name in ("Cookie", "Authorization", "Proxy-Authorization"):
            request.headers.pop(name, None)

    async def _discard_response_cookies(self, _response: httpx.Response) -> None:
        # Device API 不使用 cookie，及时清空避免跨 operation 保存服务端状态。
        self._client.cookies.clear()

    async def _perform(
        self,
        operation: PreparedOperation,
        maximum_retries: int,
        deadline: float,
        timeout: float,
    ) -> ApiResult[Any] | UnifyPortError:
        # async provider 可由总 timeout 取消；同步 provider 若阻塞 event loop 只能在返回后判定超时。
        try:
            api_key = await async_credential_source(self._config.api_key)
        except CredentialProviderFailure:
            return UnifyPortNetworkError(operation_id=operation.operation_id)
        except UnifyPortConfigurationError as error:
            return error
        if time.monotonic() >= deadline:
            return UnifyPortTimeoutError(timeout, operation_id=operation.operation_id)

        request_headers = credential_headers(operation.headers, api_key)
        if operation.content is not None:
            request_headers["Content-Type"] = "application/json"

        for attempt in range(maximum_retries + 1):
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                return UnifyPortTimeoutError(timeout, operation_id=operation.operation_id)
            retry_after: str | None = None
            outcome: ApiResult[Any] | UnifyPortError | None = None
            failure_kind: str | None = None
            try:
                async with self._client.stream(
                    operation.method,
                    operation.url,
                    params=operation.query,
                    headers=request_headers,
                    content=operation.content,
                    timeout=remaining,
                    follow_redirects=False,
                ) as response:
                    if response.status_code in RETRYABLE_STATUSES and attempt < maximum_retries:
                        retry_after = response.headers.get("Retry-After")
                    else:
                        body, read_error = await self._read_response(
                            response,
                            operation_id=operation.operation_id,
                            deadline=deadline,
                            timeout=timeout,
                        )
                        if read_error is not None:
                            outcome = read_error
                        elif body is not None:
                            response_headers = tuple(response.headers.multi_items())
                            outcome = response_outcome(
                                operation_id=operation.operation_id,
                                status=response.status_code,
                                headers=response_headers,
                                body=body,
                            )
            except httpx.TimeoutException:
                failure_kind = "timeout"
            except RETRYABLE_NETWORK_ERRORS:
                failure_kind = "retryable"
            except httpx.HTTPError:
                failure_kind = "network"
            except Exception:
                failure_kind = "network"

            if time.monotonic() >= deadline:
                return UnifyPortTimeoutError(timeout, operation_id=operation.operation_id)
            if outcome is not None:
                return outcome
            if retry_after is not None:
                wait_error = await self._wait_before_retry(
                    retry_after,
                    attempt,
                    deadline,
                    timeout,
                    operation.operation_id,
                )
                if wait_error is not None:
                    return wait_error
                continue
            if failure_kind is None:
                wait_error = await self._wait_before_retry(
                    None,
                    attempt,
                    deadline,
                    timeout,
                    operation.operation_id,
                )
                if wait_error is not None:
                    return wait_error
                continue
            can_retry = failure_kind in {"timeout", "retryable"} and attempt < maximum_retries
            if can_retry:
                wait_error = await self._wait_before_retry(
                    None,
                    attempt,
                    deadline,
                    timeout,
                    operation.operation_id,
                )
                if wait_error is not None:
                    return wait_error
                continue
            if failure_kind == "timeout":
                return UnifyPortTimeoutError(timeout, operation_id=operation.operation_id)
            return UnifyPortNetworkError(operation_id=operation.operation_id)

        return UnifyPortNetworkError(operation_id=operation.operation_id)

    async def _read_response(
        self,
        response: httpx.Response,
        *,
        operation_id: str,
        deadline: float,
        timeout: float,
    ) -> tuple[bytes | None, UnifyPortError | None]:
        response_headers = tuple(response.headers.multi_items())
        request_id = response_request_id(response_headers)
        if response_has_unsupported_content_encoding(response_headers):
            # 在任何 stream 读取前拒绝压缩，避免 HTTPX decoder 先展开攻击载荷。
            return None, UnifyPortResponseParseError(
                operation_id=operation_id,
                status=response.status_code,
                request_id=request_id,
            )
        content_length = response.headers.get("Content-Length")
        if content_length is not None and content_length.isdecimal():
            if int(content_length) > self._config.max_response_bytes:
                return None, UnifyPortResponseParseError(
                    operation_id=operation_id,
                    status=response.status_code,
                    request_id=request_id,
                )
        if response.is_stream_consumed:
            materialized: bytes | None = None
            try:
                materialized = response.content
            except httpx.ResponseNotRead:
                pass
            if materialized is None or len(materialized) > self._config.max_response_bytes:
                return None, UnifyPortResponseParseError(
                    operation_id=operation_id,
                    status=response.status_code,
                    request_id=request_id,
                )
            # MockTransport 可返回已 materialize 的 identity body，无法再消费 raw iterator。
            return materialized, None
        buffered = bytearray()
        # raw iterator 保证字节上限在透明 decoder 之前生效。
        async for chunk in response.aiter_raw():
            if time.monotonic() >= deadline:
                return None, UnifyPortTimeoutError(timeout, operation_id=operation_id)
            if len(buffered) + len(chunk) > self._config.max_response_bytes:
                return None, UnifyPortResponseParseError(
                    operation_id=operation_id,
                    status=response.status_code,
                    request_id=request_id,
                )
            buffered.extend(chunk)
        return bytes(buffered), None

    async def _wait_before_retry(
        self,
        retry_after: str | None,
        attempt: int,
        deadline: float,
        timeout: float,
        operation_id: str,
    ) -> UnifyPortTimeoutError | None:
        delay = retry_delay(retry_after, attempt, self._config.retry)
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return UnifyPortTimeoutError(timeout, operation_id=operation_id)
        await asyncio.sleep(min(delay, remaining))
        if delay >= remaining or time.monotonic() >= deadline:
            return UnifyPortTimeoutError(timeout, operation_id=operation_id)
        return None


__all__ = ["AsyncRuntime"]
