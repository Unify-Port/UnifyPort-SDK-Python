from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, cast

import yaml

from unifyport._generated import OPERATIONS, models

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts/device.openapi.yaml"
EXPECTED_CONTRACT_SHA256 = "47face9790a454fb0d6204721785846427ca7ead23cf854061ab54646682e904"
EXPECTED_RETRYABLE = {
    "getAccount",
    "getAccountAuthState",
    "getContact",
    "getConversation",
    "getGroup",
    "getGroupInviteCode",
    "getWebhookEndpoint",
    "getWorkspace",
    "listAccounts",
    "listApiKeys",
    "listContactBlocklist",
    "listContacts",
    "listConversationLabels",
    "listConversationMembers",
    "listConversations",
    "listGroupJoinRequests",
    "listGroups",
    "listProviderRegions",
    "listWebhookEndpoints",
}
EXPECTED_DESTRUCTIVE = {
    "deleteAccount",
    "deleteConversationLabel",
    "hangupCall",
    "deleteWebhookEndpoint",
    "leaveGroup",
    "revokeMessage",
    "updateGroupJoinRequests",
    "updateGroupMembers",
}
EXPECTED_SECRET_INPUT = {
    "createAccount",
    "createWebhookEndpoint",
    "importAccountAuthSession",
    "sendMessage",
    "submitAccountAuthCode",
    "submitAccountAuthPassword",
    "submitAccountPasskeyResponse",
    "updateAccount",
    "updateWebhookEndpoint",
}
EXPECTED_SECRET_OUTPUT = {
    "confirmAccountPasskey",
    "createAccountAuthSession",
    "createCall",
    "submitAccountPasskeyResponse",
    "checkAccountQrAuth",
    "createAccount",
    "createApiKey",
    "getAccount",
    "getAccountAuthState",
    "getGroupInviteCode",
    "listAccounts",
    "rotateApiKey",
    "sendMessage",
    "startAccountAuth",
    "startAccountQrAuth",
    "updateAccount",
}
EXPECTED_NODE_MCP = {
    "getWorkspace": "read",
    "listApiKeys": "read",
    "listProviderRegions": "read",
    "updateApiKeyStatus": "write",
}


def contract() -> dict[str, Any]:
    parsed = yaml.safe_load(CONTRACT_PATH.read_text(encoding="utf-8"))
    assert isinstance(parsed, dict)
    return cast(dict[str, Any], parsed)


def test_contract_is_exact_approved_node_source() -> None:
    source = json.loads((ROOT / "parity/source.json").read_text(encoding="utf-8"))
    digest = hashlib.sha256(CONTRACT_PATH.read_bytes()).hexdigest()
    assert digest == EXPECTED_CONTRACT_SHA256
    assert source["nodeSdk"]["version"] == "0.4.0"
    assert source["nodeSdk"]["baselineKind"] == "approved-source"
    assert source["nodeSdk"]["ref"] == "5901244c409f63fd6b77a899c239ebc9ee96dd50"
    assert source["contract"] == {
        "path": "contracts/device.openapi.yaml",
        "sha256": EXPECTED_CONTRACT_SHA256,
        "operationCount": 78,
        "schemaCount": 218,
    }


def test_operation_policy_sets_are_exact() -> None:
    policy = json.loads((ROOT / "policy/operation-policies.json").read_text(encoding="utf-8"))
    assert set(policy["retryAllowlist"]) == EXPECTED_RETRYABLE
    assert {
        key for key, value in policy["mutabilityOverrides"].items() if value == "destructive"
    } == EXPECTED_DESTRUCTIVE
    assert set(policy["secretInput"]) == EXPECTED_SECRET_INPUT
    assert set(policy["secretOutput"]) == EXPECTED_SECRET_OUTPUT
    assert policy["nodeMcpExposure"] == EXPECTED_NODE_MCP
    assert policy["headerAllowlist"] == ["X-Request-Id"]
    assert policy["headerPolicySource"] == "sdk_transport_policy"
    assert policy["authenticationHeadersExposed"] is False
    assert policy["pythonMcp"] == {
        "enabled": False,
        "defaultExposure": "never",
        "eligibleOperations": [],
    }
    assert {key for key, value in OPERATIONS.items() if value.retryable} == EXPECTED_RETRYABLE
    assert {key for key, value in OPERATIONS.items() if value.destructive} == EXPECTED_DESTRUCTIVE
    assert {key for key, value in OPERATIONS.items() if value.secret_input} == (
        EXPECTED_SECRET_INPUT
    )
    assert {key for key, value in OPERATIONS.items() if value.secret_output} == (
        EXPECTED_SECRET_OUTPUT
    )


def test_provider_profile_and_provider_names_remain_public_contract_types() -> None:
    schemas = contract()["components"]["schemas"]
    provider_profile = schemas["ProviderProfile"]
    assert provider_profile["additionalProperties"] is True
    assert set(provider_profile["properties"]) == {
        "id",
        "phone",
        "username",
        "display_name",
        "first_name",
        "last_name",
        "avatar_url",
        "bio",
        "business_name",
        "push_name",
        "platform",
        "device_id",
    }
    assert models.ProviderProfile.__optional_keys__ == set(provider_profile["properties"])
    assert models.ProviderProfile.__extra_items__ == models.JsonValue
    assert schemas["ProviderName"]["enum"] == [
        "telegram",
        "whatsapp",
        "line",
        "twitter",
        "zalo",
        "tiktok",
        "whatsapp-protocol",
    ]


def test_reply_token_input_and_optional_output_are_preserved() -> None:
    schemas = contract()["components"]["schemas"]
    reply_to = schemas["ReplyTo"]
    send_result = schemas["SendMessageResult"]
    assert reply_to["required"] == ["reply_token"]
    assert reply_to["properties"]["reply_token"]["type"] == "string"
    assert "reply_token" not in send_result["required"]
    assert send_result["properties"]["reply_token"]["type"] == "string"
    assert models.ReplyTo.__required_keys__ == {"reply_token"}
    assert "reply_token" in models.SendMessageResult.__optional_keys__


def test_conversation_read_does_not_impose_whatsapp_pair_on_telegram() -> None:
    # provider 相关约束由服务端判断，Telegram 消息边界不能被通用 sender guard 拒绝。
    extension = contract()["components"]["schemas"]["ConversationReadRequest"]["allOf"][1]
    assert "dependentRequired" not in extension
    assert "ConversationReadRequest" not in models.DEPENDENT_REQUIRED
