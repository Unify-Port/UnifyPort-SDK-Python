<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: upsertConversationLabel -->

[English](upsert-conversation-label.md) | [简体中文](../zh-CN/api-reference/upsert-conversation-label.md)

# `upsert_conversation_label`

Explicit Python method for public Device API operation `upsertConversationLabel`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/labels/upsert`
- Python method: `upsert_conversation_label`
- Node operationId: `upsertConversationLabel`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `yes`
- Python model: `UpsertConversationLabelRequestBody`
- Contract schema: `ConversationLabelUpsertRequest`

## Success response

- Python model: `UpsertConversationLabelResponse`
- Contract schema: `ResponseEnvelope[ConversationLabel]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
