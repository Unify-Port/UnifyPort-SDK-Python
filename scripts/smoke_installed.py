"""Exercise the installed wheel without relying on development dependencies."""

from __future__ import annotations

import asyncio
from typing import get_args, get_type_hints

import httpx

from unifyport import (
    OPERATIONS,
    AsyncUnifyPortDeviceClient,
    UnifyPortDeviceClient,
    __version__,
    models,
)

# 独立固定预期版本，避免旧 wheel 与旧 runtime 同时通过自洽检查。
EXPECTED_VERSION = "0.2.0"


def _response(request: httpx.Request) -> httpx.Response:
    # mock transport 同时验证 credential/header 边界，且不会触达真实 Device API。
    assert request.headers["X-Api-Key"] == "wheel-smoke-key"
    assert request.headers["X-Request-Id"].startswith("wheel-smoke-")
    assert "Cookie" not in request.headers
    return httpx.Response(
        200,
        headers={"X-Request-Id": "wheel-smoke-response"},
        json={"data": {"id": "workspace-wheel-smoke"}},
    )


def _sync_smoke() -> None:
    with UnifyPortDeviceClient(
        base_url="https://api.example.test",
        api_key="wheel-smoke-key",
        transport=httpx.MockTransport(_response),
    ) as client:
        result = client.get_workspace(x_request_id="wheel-smoke-sync")
    assert result.status == 200
    assert result.request_id == "wheel-smoke-response"


async def _async_smoke() -> None:
    async with AsyncUnifyPortDeviceClient(
        base_url="https://api.example.test",
        api_key="wheel-smoke-key",
        transport=httpx.MockTransport(_response),
    ) as client:
        result = await client.get_workspace(x_request_id="wheel-smoke-async")
    assert result.status == 200
    assert result.request_id == "wheel-smoke-response"


def main() -> None:
    # public import/version/model metadata 可防止 wheel 漏文件或安装到旧 editable checkout。
    assert __version__ == EXPECTED_VERSION
    # 安装产物必须包含 FB 类型，防止只在 editable checkout 中验证通过。
    assert "facebook" in get_args(models.ProviderName)
    assert models.FacebookMessage.__required_keys__ == frozenset({"id", "direction"})
    assert "facebook" in get_args(
        get_type_hints(models.FacebookMessageReceivedWebhookEvent)["provider"]
    )
    assert models.ReplyTo.__required_keys__ == frozenset({"reply_token"})
    # 逐方法解析能发现 postponed annotation 在 wheel 中缺 runtime import 的问题。
    for spec in OPERATIONS.values():
        get_type_hints(getattr(UnifyPortDeviceClient, spec.python_method))
        get_type_hints(getattr(AsyncUnifyPortDeviceClient, spec.python_method))
    _sync_smoke()
    asyncio.run(_async_smoke())
    print("installed wheel sync/async smoke passed")


if __name__ == "__main__":
    main()
