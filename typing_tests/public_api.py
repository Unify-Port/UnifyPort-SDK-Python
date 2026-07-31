"""Compile-only assertions for the public typed SDK surface."""

from typing import assert_type

from unifyport import ApiResult, AsyncUnifyPortDeviceClient, UnifyPortDeviceClient, models


def check_sync_surface(client: UnifyPortDeviceClient) -> None:
    workspace = client.get_workspace(x_request_id="req_typecheck")
    assert_type(workspace, ApiResult[models.GetWorkspaceResponse])

    account = client.get_account(account_id="acc_typecheck")
    assert_type(account, ApiResult[models.GetAccountResponse])

    # reply_token 为 optional output；输入 reply_to 存在时仍由 TypedDict 要求该字段。
    body: models.SendMessageRequestBody = {
        "account_id": "acc_typecheck",
        "to": {"id": "recipient_typecheck", "type": "user"},
        "message": {"type": "text", "text": "hello"},
        "reply_to": {"reply_token": "opaque_typecheck"},
    }
    sent = client.send_message(body=body)
    assert_type(sent, ApiResult[models.SendMessageResponse])


async def check_async_surface(client: AsyncUnifyPortDeviceClient) -> None:
    workspace = await client.get_workspace()
    assert_type(workspace, ApiResult[models.GetWorkspaceResponse])
