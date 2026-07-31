"""Public asynchronous Device API client."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, overload

import httpx

from ._generated import OPERATIONS, AsyncDeviceMethodsMixin
from ._runtime import AsyncRuntime
from ._runtime.common import build_async_client_config
from .config import (
    AsyncDeviceClientConfig,
    AsyncSecretSource,
    RequestOptions,
    RetryConfig,
)
from .errors import UnifyPortConfigurationError
from .result import ApiResult


class AsyncUnifyPortDeviceClient(AsyncDeviceMethodsMixin):
    """Async client whose task cancellation propagates as ``asyncio.CancelledError``."""

    __slots__ = ("_runtime",)

    @overload
    def __init__(
        self,
        config: AsyncDeviceClientConfig,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        base_url: str,
        api_key: AsyncSecretSource,
        timeout: float | None = None,
        retry: RetryConfig | Mapping[str, object] | None = None,
        max_response_bytes: int | None = None,
        allow_insecure_http: bool | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None: ...

    def __init__(
        self,
        config: AsyncDeviceClientConfig | None = None,
        *,
        base_url: str | None = None,
        api_key: AsyncSecretSource | None = None,
        timeout: float | None = None,
        retry: RetryConfig | Mapping[str, object] | None = None,
        max_response_bytes: int | None = None,
        allow_insecure_http: bool | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        resolved = build_async_client_config(
            config,
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            retry=retry,
            max_response_bytes=max_response_bytes,
            allow_insecure_http=allow_insecure_http,
        )
        self._runtime = AsyncRuntime(resolved, transport=transport)

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
        spec = OPERATIONS.get(operation_id)
        if spec is None:
            raise UnifyPortConfigurationError("operation_id", "is not in the generated catalog")
        return await self._runtime.execute(
            spec,
            path_params=path_params,
            query=query,
            body=body,
            headers=headers,
            options=options,
        )

    async def aclose(self) -> None:
        await self._runtime.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: object | None,
    ) -> None:
        await self.aclose()

    def __repr__(self) -> str:
        return "AsyncUnifyPortDeviceClient(<configured>)"


__all__ = ["AsyncUnifyPortDeviceClient"]
