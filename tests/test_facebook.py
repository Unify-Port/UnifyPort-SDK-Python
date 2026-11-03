from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from unifyport import UnifyPortApiError, UnifyPortDeviceClient
from unifyport._generated import OPERATIONS


def test_facebook_creation_session_and_uncertain_send() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        # 创建和导入不代替运行就绪判断，未知发送结果不允许隐式重试。
        requests.append(request)
        if request.url.path == "/v1/messages":
            return httpx.Response(502, json={"error": {"code": "provider_unavailable"}})
        return httpx.Response(200, json={"data": {"runtime_status": "starting"}})

    with UnifyPortDeviceClient(
        base_url="https://api.example.com",
        api_key="test-key",
        transport=httpx.MockTransport(respond),
    ) as client:
        client.create_account(
            body={"provider": "facebook", "auth_mode": "session", "region": "sg"},
            idempotency_key="facebook-example",
        )
        client.import_account_auth_session(
            account_id="acc_example",
            body={"session_url": "https://example.com/temporary-session.json"},
        )
        with pytest.raises(UnifyPortApiError):
            client.send_message(
                body={
                    "account_id": "acc_example",
                    "to": {"id": "9007199254740995", "type": "user"},
                    "message": {"type": "text", "text": "Hello"},
                }
            )
    assert len(requests) == 3
    assert requests[0].headers["Idempotency-Key"] == "facebook-example"
    assert requests[1].url.path == "/v1/accounts/acc_example/auth/session"
    assert json.loads(requests[2].content)["to"]["id"] == "9007199254740995"
    for operation in ["sendMessage", "importAccountAuthSession"]:
        assert OPERATIONS[operation].retryable is False


def test_facebook_public_fixtures_preserve_sparse_media_and_state_boundaries() -> None:
    cases = json.loads((Path(__file__).parent / "fixtures/webhook-examples.json").read_text())
    samples = {case["name"]: case["body"] for case in cases if case["name"].startswith("facebook")}
    assert len(samples) == 8
    message = samples["facebookMessageReceived/inbound"]["data"]["message"]
    assert message["id"] == "9007199254740993"
    assert message["sent_at"] == "2026-01-01T00:00:00.123456789Z"
    outbound = samples["facebookMessageReceived/outbound"]["data"]["message"]
    assert outbound["direction"] == "outbound"
    assert "sent_at" not in outbound
    media = samples["facebookMessageReceived/orderedMedia"]["data"]["message"]["attachments"]
    assert [item["type"] for item in media] == ["image", "audio"]
    assert media[0]["metadata"]["animated"] is False
    assert media[0]["size"] == 0
    assert media[1]["metadata"]["ptt"] is False
    assert media[1]["metadata"]["duration"] == 0
    assert "url" not in media[1] and "duration_ms" not in media[1]
    assert "auth_status" not in samples["facebookAccountStatusUpdated/example"]["data"]
    assert samples["facebookAccountAuthSucceeded/example"]["data"]["runtime_status"] == "running"
    assert samples["facebookAccountAuthFailed/example"]["data"]["auth_status"] == "failed"
