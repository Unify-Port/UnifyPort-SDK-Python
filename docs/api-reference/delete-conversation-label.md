<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: deleteConversationLabel -->

[English](delete-conversation-label.md) | [简体中文](../zh-CN/api-reference/delete-conversation-label.md)

# `delete_conversation_label`

Explicit Python method for public Device API operation `deleteConversationLabel`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/labels/delete`
- Python method: `delete_conversation_label`
- Node operationId: `deleteConversationLabel`

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
- Python model: `DeleteConversationLabelRequestBody`
- Contract schema: `ConversationLabelDeleteRequest`

## Success response

- Python model: `DeleteConversationLabelResponse`
- Contract schema: `ResponseEnvelope[ConversationLabelDeleteResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `true` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `destructive` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
