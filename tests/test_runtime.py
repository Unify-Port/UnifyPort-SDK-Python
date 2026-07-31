from __future__ import annotations

import asyncio
import inspect
import time
from collections.abc import AsyncIterator, Callable, Iterator, Mapping
from typing import Any, cast

import httpx
import pytest

from unifyport import (
    ApiResult,
    AsyncUnifyPortDeviceClient,
    DeviceClientConfig,
    RequestOptions,
    RetryConfig,
    UnifyPortApiError,
    UnifyPortConfigurationError,
    UnifyPortDeviceClient,
    UnifyPortNetworkError,
    UnifyPortResponseParseError,
    UnifyPortTimeoutError,
    models,
)
from unifyport._generated import (
    OPERATIONS,
    AsyncDeviceMethodsMixin,
    SyncDeviceMethodsMixin,
)
from unifyport._runtime import common as runtime_common


def json_response(
    value: object,
    status: int = 200,
    headers: dict[str, str] | None = None,
) -> httpx.Response:
    return httpx.Response(status, json=value, headers=headers)


def assert_secret_free_configuration_error(
    error: UnifyPortConfigurationError,
    secret: str,
) -> None:
    assert_secret_free_error(error, secret)
    exposed = (repr(error.field), repr(error.reason))
    assert all(secret not in value for value in exposed)


def assert_secret_free_error(error: BaseException, secret: str) -> None:
    # cause/context 与基础异常字段都属于调用方可观察面，不能保留原始敏感输入。
    assert error.__cause__ is None
    assert error.__context__ is None
    exposed = (
        str(error),
        repr(error),
        repr(error.args),
        repr(error.__dict__),
    )
    assert all(secret not in value for value in exposed)


class FailIfReadSyncStream(httpx.SyncByteStream):
    def __init__(self, secret: str) -> None:
        self.secret = secret
        self.iterated = False
        self.closed = False

    def __iter__(self) -> Iterator[bytes]:
        # 触发即说明 runtime 在拒绝编码前已进入潜在解压路径。
        self.iterated = True
        raise AssertionError(self.secret)

    def close(self) -> None:
        self.closed = True


class FailIfReadAsyncStream(httpx.AsyncByteStream):
    def __init__(self, secret: str) -> None:
        self.secret = secret
        self.iterated = False
        self.closed = False

    async def __aiter__(self) -> AsyncIterator[bytes]:
        # 保留 async generator 形态，若开始消费则立即暴露测试失败。
        self.iterated = True
        raise AssertionError(self.secret)
        yield b""  # pragma: no cover

    async def aclose(self) -> None:
        self.closed = True


class RecordingSyncMixin(SyncDeviceMethodsMixin):
    def __init__(self) -> None:
        self.calls: list[str] = []

    def _execute_operation(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, object] | None = None,
        query: Mapping[str, object] | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[Any]:
        self.calls.append(operation_id)
        return ApiResult(data=None, status=204)


class RecordingAsyncMixin(AsyncDeviceMethodsMixin):
    def __init__(self) -> None:
        self.calls: list[str] = []

    async def _execute_operation(
        self,
        operation_id: str,
        *,
        path_params: Mapping[str, object] | None = None,
        query: Mapping[str, object] | None = None,
        body: object | None = None,
        headers: Mapping[str, str] | None = None,
        options: RequestOptions | Mapping[str, Any] | None = None,
    ) -> ApiResult[Any]:
        self.calls.append(operation_id)
        return ApiResult(data=None, status=204)


def generated_method_arguments(method: Callable[..., object]) -> dict[str, object]:
    arguments: dict[str, object] = {}
    for name, parameter in inspect.signature(method).parameters.items():
        if name == "body":
            arguments[name] = {}
        elif name == "limit":
            arguments[name] = 1
        elif name == "x_request_id":
            arguments[name] = "req_generated"
        elif name == "options":
            arguments[name] = RequestOptions(retry=False)
        elif parameter.default is inspect.Parameter.empty:
            arguments[name] = "value"
        elif name not in {"options"}:
            # optional query 字段也传值，覆盖生成 wrapper 的 location 映射分支。
            arguments[name] = "value"
    return arguments


def test_all_generated_sync_methods_delegate_to_catalog_operation() -> None:
    facade = RecordingSyncMixin()
    for spec in OPERATIONS.values():
        method = getattr(facade, spec.python_method)
        result = method(**generated_method_arguments(method))
        assert result.status == 204
    assert facade.calls == list(OPERATIONS)


async def test_all_generated_async_methods_delegate_to_catalog_operation() -> None:
    facade = RecordingAsyncMixin()
    for spec in OPERATIONS.values():
        method = getattr(facade, spec.python_method)
        result = await method(**generated_method_arguments(method))
        assert result.status == 204
    assert facade.calls == list(OPERATIONS)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://device.example.com",
        "http://127.0.0.1:8080",
        "https://user:password@device.example.com",
        "https://device.example.com?tenant=secret",
        "https://device.example.com#secret",
        "not-a-url",
    ],
)
def test_base_url_rejects_unsafe_configuration(base_url: str) -> None:
    with pytest.raises(UnifyPortConfigurationError):
        UnifyPortDeviceClient(base_url=base_url, api_key="key")


def test_loopback_http_requires_explicit_exact_boolean_opt_in() -> None:
    client = UnifyPortDeviceClient(
        base_url="http://127.0.0.1:8080",
        api_key="key",
        allow_insecure_http=True,
        transport=httpx.MockTransport(lambda _request: httpx.Response(204)),
    )
    client.close()

    with pytest.raises(UnifyPortConfigurationError, match="boolean"):
        UnifyPortDeviceClient(
            base_url="http://127.0.0.1:8080",
            api_key="key",
            allow_insecure_http=cast(bool, 1),
        )
    with pytest.raises(UnifyPortConfigurationError):
        UnifyPortDeviceClient(
            base_url="http://device.example.com",
            api_key="key",
            allow_insecure_http=True,
        )


def test_sensitive_validation_failures_do_not_retain_original_exception_context() -> None:
    transport = httpx.MockTransport(lambda _request: httpx.Response(204))

    api_marker = "api-marker"
    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=f"{api_marker}\ud800",
        transport=transport,
    ) as client:
        with pytest.raises(UnifyPortConfigurationError) as captured:
            client.get_workspace()
    assert_secret_free_configuration_error(captured.value, api_marker)

    base_url_marker = "url-marker"
    with pytest.raises(UnifyPortConfigurationError) as captured:
        UnifyPortDeviceClient(
            base_url=f"https://device.example.com:{base_url_marker}",
            api_key="key",
        )
    assert_secret_free_configuration_error(captured.value, base_url_marker)

    path_marker = "path-marker"
    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=transport,
    ) as client:
        with pytest.raises(UnifyPortConfigurationError) as captured:
            client.get_account(account_id=f"{path_marker}\ud800")
    assert_secret_free_configuration_error(captured.value, path_marker)

    query_marker = "query-marker"
    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=transport,
    ) as client:
        with pytest.raises(UnifyPortConfigurationError) as captured:
            client.list_contacts(account_id="account", cursor=f"{query_marker}\ud800")
    assert_secret_free_configuration_error(captured.value, query_marker)

    body_marker = "body-marker"
    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=transport,
    ) as client:
        with pytest.raises(UnifyPortConfigurationError) as captured:
            client.update_workspace(body={"name": f"{body_marker}\ud800", "status": "active"})
    assert_secret_free_configuration_error(captured.value, body_marker)

    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=transport,
    ) as client:
        with pytest.raises(UnifyPortConfigurationError) as captured:
            client.get_workspace(options={"max_retries": 0, "retry": False})
    assert_secret_free_configuration_error(captured.value, "not-present")

    target_marker = "target-marker"
    normalized = runtime_common.normalize_config(
        DeviceClientConfig(base_url="https://device.example.com", api_key="key")
    )
    with pytest.raises(UnifyPortConfigurationError) as captured:
        runtime_common._ensure_target_inside_base(
            f"https://device.example.com:{target_marker}/v1/workspace",
            normalized,
        )
    assert_secret_free_configuration_error(captured.value, target_marker)


def test_request_target_is_quoted_and_credential_comes_only_from_config() -> None:
    captured: httpx.Request | None = None

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal captured
        captured = request
        return json_response({"data": {"id": "acc"}})

    with UnifyPortDeviceClient(
        base_url="https://device.example.com/api",
        api_key="trusted-key",
        transport=httpx.MockTransport(handler),
    ) as client:
        result = client.get_account(
            account_id="account/with/slash",
            x_request_id="client_req-1",
        )

    assert result.status == 200
    assert captured is not None
    assert str(captured.url) == (
        "https://device.example.com/api/v1/accounts/account%2Fwith%2Fslash"
    )
    assert captured.headers["X-Api-Key"] == "trusted-key"
    assert captured.headers["X-Request-Id"] == "client_req-1"


def test_response_cookies_are_not_replayed_as_credentials() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(204, headers={"Set-Cookie": "session=untrusted"})

    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="trusted",
        transport=httpx.MockTransport(handler),
    ) as client:
        client.get_workspace()
        client.get_workspace()

    assert len(requests) == 2
    assert all("Cookie" not in request.headers for request in requests)


@pytest.mark.parametrize(
    "headers",
    [
        {"X-Api-Key": "untrusted"},
        {"authorization": "Bearer untrusted"},
        {"Cookie": "session=untrusted"},
        {"X-Unknown": "value"},
        {"X-Request-Id": "contains spaces"},
        {"X-Request-Id": "a" * 129},
        {"X-Request-Id": "line\nbreak"},
    ],
)
def test_operation_headers_are_allowlisted_and_validated(headers: dict[str, str]) -> None:
    called = False

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal called
        called = True
        return httpx.Response(204)

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="trusted",
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(UnifyPortConfigurationError):
        request_id = next(
            (value for name, value in headers.items() if name.lower() == "x-request-id"),
            None,
        )
        if request_id is not None and len(headers) == 1:
            client.get_workspace(x_request_id=request_id)
        else:
            # public wrapper 不暴露任意 header；private 入口仍须纵深拒绝 credential/unknown header。
            client._execute_operation("getWorkspace", headers=headers)
    client.close()
    assert not called


def test_unknown_inputs_and_required_body_fail_before_credential_resolution() -> None:
    resolved = 0

    def provider() -> str:
        nonlocal resolved
        resolved += 1
        return "key"

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        transport=httpx.MockTransport(lambda _request: httpx.Response(204)),
    )
    with pytest.raises(UnifyPortConfigurationError, match="query"):
        client._execute_operation("getWorkspace", query={"unknown": "value"})
    with pytest.raises(UnifyPortConfigurationError, match="required"):
        client._execute_operation("createAccount", body=None)
    client.close()
    assert resolved == 0


def test_retry_resolves_credential_once_and_reuses_it_across_attempts() -> None:
    credential_calls = 0
    requests: list[str] = []

    def provider() -> str:
        nonlocal credential_calls
        credential_calls += 1
        return f"key-{credential_calls}"

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request.headers["X-Api-Key"])
        if len(requests) < 3:
            return json_response({"error": {"code": "TEMPORARY"}}, 503)
        return json_response({"request_id": "req_ok", "data": {"ok": True}})

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        retry=RetryConfig(max_retries=2, base_delay=0.0001, max_delay=0.0001),
        transport=httpx.MockTransport(handler),
    )
    result = client.get_workspace()
    client.close()

    assert result.request_id == "req_ok"
    assert requests == ["key-1", "key-1", "key-1"]
    assert credential_calls == 1


def test_retry_budget_is_tightened_and_never_granted_to_write_operations() -> None:
    read_calls = 0

    def read_handler(_request: httpx.Request) -> httpx.Response:
        nonlocal read_calls
        read_calls += 1
        return json_response({"error": {"code": "TEMPORARY"}}, 503)

    read_client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        retry=RetryConfig(max_retries=2, base_delay=0.0001, max_delay=0.0001),
        transport=httpx.MockTransport(read_handler),
    )
    with pytest.raises(UnifyPortApiError):
        read_client.get_workspace(options=RequestOptions(max_retries=1))
    read_client.close()
    assert read_calls == 2

    write_calls = 0

    def write_handler(_request: httpx.Request) -> httpx.Response:
        nonlocal write_calls
        write_calls += 1
        return json_response({"error": {"code": "TEMPORARY"}}, 503)

    write_client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        retry=RetryConfig(max_retries=2, base_delay=0.0001, max_delay=0.0001),
        transport=httpx.MockTransport(write_handler),
    )
    with pytest.raises(UnifyPortApiError):
        write_client.update_workspace(
            body={"name": "Demo", "status": "active"},
            options=RequestOptions(retry=True),
        )
    write_client.close()
    assert write_calls == 1


def test_retryable_operation_retries_all_httpx_transport_errors() -> None:
    calls = 0

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        if calls == 1:
            raise httpx.LocalProtocolError("must-not-leak")
        return httpx.Response(204)

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        retry=RetryConfig(max_retries=1, base_delay=0.0001, max_delay=0.0001),
        transport=httpx.MockTransport(handler),
    )
    assert client.get_workspace().status == 204
    client.close()
    assert calls == 2


def test_redirect_is_not_followed_and_is_normalized_as_api_error() -> None:
    calls = 0

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(302, headers={"Location": "https://evil.example.com/secret"})

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(UnifyPortApiError) as captured:
        client.get_workspace()
    client.close()

    assert captured.value.status == 302
    assert captured.value.code == "HTTP_302"
    assert "evil" not in str(captured.value)
    assert calls == 1


def test_empty_success_and_optional_reply_token_are_both_safe() -> None:
    responses = iter(
        [
            httpx.Response(204),
            json_response({"data": {"message_id": "msg_1", "status": "accepted"}}),
            json_response(
                {
                    "data": {
                        "message_id": "msg_2",
                        "status": "accepted",
                        "reply_token": "opaque-token",
                    }
                }
            ),
        ]
    )
    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(lambda _request: next(responses)),
    )

    empty = client.get_workspace()
    message_body: models.SendMessageRequestBody = {
        "account_id": "acc_test",
        "to": {"id": "recipient_test", "type": "user"},
        "message": {"type": "text", "text": "hello"},
    }
    without_token = client.send_message(body=message_body)
    with_token = client.send_message(body=message_body)
    client.close()

    assert empty.data is None
    assert without_token.data == {"data": {"message_id": "msg_1", "status": "accepted"}}
    assert with_token.data["data"]["reply_token"] == "opaque-token"
    assert not hasattr(empty, "response")
    assert not hasattr(empty, "headers")


def test_response_limit_parse_and_api_errors_retain_only_safe_metadata() -> None:
    oversized = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        max_response_bytes=8,
        transport=httpx.MockTransport(
            lambda _request: httpx.Response(
                200,
                content=b'{"secret":"must-not-leak"}',
                headers={"X-Request-Id": "req_large"},
            )
        ),
    )
    with pytest.raises(UnifyPortResponseParseError) as large_error:
        oversized.get_workspace()
    oversized.close()
    assert large_error.value.request_id == "req_large"
    assert not hasattr(large_error.value, "response")

    api_client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(
            lambda _request: json_response(
                {
                    "request_id": "unsafe request id",
                    "error": {
                        "code": "SECRET value",
                        "message": "credential=must-not-leak",
                        "details": {"api_key": "must-not-leak"},
                    },
                },
                401,
            )
        ),
    )
    with pytest.raises(UnifyPortApiError) as api_error:
        api_client.get_workspace()
    api_client.close()
    assert api_error.value.code == "HTTP_401"
    assert api_error.value.request_id is None
    assert api_error.value.details is None
    assert "must-not-leak" not in str(api_error.value)
    assert api_error.value.__cause__ is None


def test_sync_rejects_encoded_response_before_raw_stream_read() -> None:
    secret = "sync-marker"
    stream = FailIfReadSyncStream(secret)
    request_encoding: str | None = None

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal request_encoding
        request_encoding = request.headers.get("Accept-Encoding")
        return httpx.Response(
            200,
            headers={
                "Content-Encoding": f"gzip; {secret}",
                "X-Request-Id": "req_encoding_sync",
            },
            stream=stream,
        )

    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(UnifyPortResponseParseError) as captured:
            client.get_workspace()

    assert request_encoding == "identity"
    assert not stream.iterated
    assert stream.closed
    assert captured.value.status == 200
    assert captured.value.request_id == "req_encoding_sync"
    assert_secret_free_error(captured.value, secret)


async def test_async_rejects_encoded_response_before_raw_stream_read() -> None:
    secret = "async-marker"
    stream = FailIfReadAsyncStream(secret)
    request_encoding: str | None = None

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal request_encoding
        request_encoding = request.headers.get("Accept-Encoding")
        return httpx.Response(
            200,
            headers={
                "Content-Encoding": f"gzip; {secret}",
                "X-Request-Id": "req_encoding_async",
            },
            stream=stream,
        )

    async with AsyncUnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(UnifyPortResponseParseError) as captured:
            await client.get_workspace()

    assert request_encoding == "identity"
    assert not stream.iterated
    assert stream.closed
    assert captured.value.status == 200
    assert captured.value.request_id == "req_encoding_async"
    assert_secret_free_error(captured.value, secret)


def test_network_error_does_not_retain_transport_text_or_cause() -> None:
    def handler(_request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("credential=must-not-leak")

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="key",
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(UnifyPortNetworkError) as captured:
        client.get_workspace(options=RequestOptions(retry=False))
    client.close()

    assert "must-not-leak" not in str(captured.value)
    assert captured.value.__cause__ is None
    assert not hasattr(captured.value, "response")


def test_sync_total_deadline_rejects_late_credential_without_sending() -> None:
    sent = False

    def provider() -> str:
        time.sleep(0.02)
        return "key"

    def handler(_request: httpx.Request) -> httpx.Response:
        nonlocal sent
        sent = True
        return httpx.Response(204)

    client = UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        timeout=0.005,
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(UnifyPortTimeoutError):
        client.get_workspace()
    client.close()
    # sync callback 不可安全强杀，但返回后不得再把过期 credential 发到网络。
    assert not sent


async def test_async_client_matches_result_and_credential_semantics() -> None:
    credential_calls = 0
    attempts = 0

    async def provider() -> str:
        nonlocal credential_calls
        credential_calls += 1
        await asyncio.sleep(0)
        return f"key-{credential_calls}"

    async def handler(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        assert request.headers["X-Api-Key"] == "key-1"
        if attempts == 1:
            return json_response({"error": {"code": "TEMPORARY"}}, 503)
        return json_response({"request_id": "req_async", "data": {"ok": True}})

    async with AsyncUnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        retry=RetryConfig(max_retries=1, base_delay=0.0001, max_delay=0.0001),
        transport=httpx.MockTransport(handler),
    ) as client:
        result = await client.get_workspace()

    assert result.status == 200
    assert result.request_id == "req_async"
    assert credential_calls == 1
    assert attempts == 2


async def test_async_total_timeout_covers_credential_provider() -> None:
    async def provider() -> str:
        await asyncio.Event().wait()
        return "unreachable"

    client = AsyncUnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        timeout=0.01,
        transport=httpx.MockTransport(lambda _request: httpx.Response(204)),
    )
    with pytest.raises(UnifyPortTimeoutError):
        await client.get_workspace()
    await client.aclose()


async def test_async_task_cancellation_remains_python_native() -> None:
    started = asyncio.Event()

    async def provider() -> str:
        started.set()
        await asyncio.Event().wait()
        return "unreachable"

    client = AsyncUnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key=provider,
        transport=httpx.MockTransport(lambda _request: httpx.Response(204)),
    )
    pending = asyncio.create_task(client.get_workspace())
    await started.wait()
    pending.cancel("caller-owned-reason")
    with pytest.raises(asyncio.CancelledError):
        await pending
    await client.aclose()


def test_public_config_repr_redacts_url_and_credential() -> None:
    client = UnifyPortDeviceClient(
        base_url="https://device.example.com/private-prefix",
        api_key="must-not-leak",
        transport=httpx.MockTransport(lambda _request: httpx.Response(204)),
    )
    rendered = repr(client)
    client.close()

    assert "must-not-leak" not in rendered
    assert "private-prefix" not in rendered
