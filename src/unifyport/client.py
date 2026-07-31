"""Public synchronous Device API client."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, overload

import httpx

from ._generated import OPERATIONS, SyncDeviceMethodsMixin
from ._runtime import SyncRuntime
from ._runtime.common import build_sync_client_config
from .config import (
    DeviceClientConfig,
    RequestOptions,
    RetryConfig,
    SyncCredentialProvider,
    SyncSecretSource,
)
from .errors import UnifyPortConfigurationError
from .result import ApiResult


class UnifyPortDeviceClient(SyncDeviceMethodsMixin):
    """Synchronous client exposing the generated Device API operation surface."""

    __slots__ = ("_runtime",)

    @overload
    def __init__(
        self,
        config: DeviceClientConfig,
        *,
        transport: httpx.BaseTransport | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        base_url: str,
        api_key: str | SyncCredentialProvider,
        timeout: float | None = None,
        retry: RetryConfig | Mapping[str, object] | None = None,
        max_response_bytes: int | None = None,
        allow_insecure_http: bool | None = None,
        transport: httpx.BaseTransport | None = None,
    ) -> None: ...

    def __init__(
        self,
        config: DeviceClientConfig | None = None,
        *,
        base_url: str | None = None,
        api_key: SyncSecretSource | None = None,
        timeout: float | None = None,
        retry: RetryConfig | Mapping[str, object] | None = None,
        max_response_bytes: int | None = None,
        allow_insecure_http: bool | None = None,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        resolved = build_sync_client_config(
            config,
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            retry=retry,
            max_response_bytes=max_response_bytes,
            allow_insecure_http=allow_insecure_http,
        )
        self._runtime = SyncRuntime(resolved, transport=transport)

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
        spec = OPERATIONS.get(operation_id)
        if spec is None:
            # 只有生成 catalog 中的 operation 可进入 runtime，防止形成 generic request 逃生口。
            raise UnifyPortConfigurationError("operation_id", "is not in the generated catalog")
        return self._runtime.execute(
            spec,
            path_params=path_params,
            query=query,
            body=body,
            headers=headers,
            options=options,
        )

    def close(self) -> None:
        self._runtime.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object | None,
    ) -> None:
        self.close()

    def __repr__(self) -> str:
        # client repr 不展开 config/runtime，避免 credential provider 或 URL 被间接记录。
        return "UnifyPortDeviceClient(<configured>)"


__all__ = ["UnifyPortDeviceClient"]
