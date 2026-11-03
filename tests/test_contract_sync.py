from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx
import pytest

from unifyport import AsyncUnifyPortDeviceClient, UnifyPortApiError, UnifyPortDeviceClient
from unifyport._generated import OPERATIONS

ROOT = Path(__file__).resolve().parents[1]


def operation_arguments(operation: Any) -> dict[str, Any]:
    arguments = {parameter.python_name: "example/value" for parameter in operation.path_params}
    arguments.update(
        {
            parameter.python_name: "example"
            for parameter in operation.query_params
            if parameter.required
        }
    )
    if operation.request_body is not None:
        arguments["body"] = {}
    return arguments


@pytest.mark.asyncio
async def test_all_http_methods_and_paths_in_sync_and_async_clients() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        # 所有新增写操作只进入 mock，校验路径编码时不接触真实账号。
        requests.append(request)
        return httpx.Response(200, json={"data": {}})

    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="test-key",
        transport=httpx.MockTransport(respond),
    ) as client:
        for operation in OPERATIONS.values():
            getattr(client, operation.python_method)(**operation_arguments(operation))
    async with AsyncUnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="test-key",
        transport=httpx.MockTransport(respond),
    ) as asynchronous:
        for operation in OPERATIONS.values():
            await getattr(asynchronous, operation.python_method)(**operation_arguments(operation))
    assert len(requests) == 156
    for index, operation in enumerate([*OPERATIONS.values(), *OPERATIONS.values()]):
        path = operation.path
        for parameter in operation.path_params:
            path = path.replace("{" + parameter.name + "}", quote("example/value", safe=""))
        assert requests[index].method == operation.http_method
        assert requests[index].url.raw_path.split(b"?")[0].decode() == path


@pytest.mark.parametrize(
    "numeric", ["12345", None, 12345, "01234", "123456", "１２３４５", "secret=value"]
)
def test_optional_numeric_error_code_is_filtered_independently(numeric: object) -> None:
    transport = httpx.MockTransport(
        lambda request: httpx.Response(
            400,
            json={
                "request_id": "req_example",
                "error": {"code": "BAD_REQUEST", "numeric_code": numeric},
            },
        )
    )
    with (
        UnifyPortDeviceClient(
            base_url="https://device.example.com", api_key="test-key", transport=transport
        ) as client,
        pytest.raises(UnifyPortApiError) as captured,
    ):
        client.get_workspace()
    assert captured.value.numeric_code == ("12345" if numeric == "12345" else None)
    assert captured.value.code == "BAD_REQUEST"
    assert captured.value.request_id == "req_example"
    assert "secret=value" not in str(captured.value)


def test_delete_accepted_and_no_content_remain_distinct() -> None:
    responses = iter(
        [
            httpx.Response(
                202,
                json={"data": {"operation_id": "op_example", "kind": "DELETE", "state": "PENDING"}},
            ),
            httpx.Response(204),
        ]
    )
    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="test-key",
        transport=httpx.MockTransport(lambda request: next(responses)),
    ) as client:
        accepted = client.delete_account(account_id="acc_example")
        assert accepted.status == 202
        assert accepted.data is not None
        assert accepted.data["data"]["state"] == "PENDING"
        assert client.delete_account(account_id="acc_example").data is None


def test_idempotency_header_and_telegram_read_boundary() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"data": {}})

    with UnifyPortDeviceClient(
        base_url="https://device.example.com",
        api_key="test-key",
        transport=httpx.MockTransport(respond),
    ) as client:
        client.create_account(
            body={"provider": "whatsapp", "region": "example", "auth_mode": "qrcode"},
            idempotency_key="idem_example",
        )
        client.mark_conversation_read(
            account_id="acc_example",
            body={
                "conversation_id": "conversation_example",
                "up_to_message_id": "12345",
            },
        )
    assert requests[0].headers["Idempotency-Key"] == "idem_example"
    assert json.loads(requests[1].content) == {
        "conversation_id": "conversation_example",
        "up_to_message_id": "12345",
    }


def test_all_public_webhook_examples_have_static_type_cases() -> None:
    cases = json.loads((ROOT / "tests/fixtures/webhook-examples.json").read_text())
    module = ast.parse((ROOT / "pyright_tests/webhook_examples.py").read_text())
    declarations = [node for node in module.body if isinstance(node, ast.AnnAssign)]
    assert len(cases) == len(declarations) == 57
    assert len({case["schema"] for case in cases}) == 29
    for case, declaration in zip(cases, declarations, strict=True):
        assert isinstance(declaration.annotation, ast.Attribute)
        assert declaration.annotation.attr == case["schema"]
        assert ast.literal_eval(declaration.value) == case["body"]
