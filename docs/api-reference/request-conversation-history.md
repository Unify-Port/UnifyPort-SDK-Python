<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: requestConversationHistory -->

[English](request-conversation-history.md) | [简体中文](../zh-CN/api-reference/request-conversation-history.md)

# `request_conversation_history`

Explicit Python method for public Device API operation `requestConversationHistory`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/history/request`
- Python method: `request_conversation_history`
- Node operationId: `requestConversationHistory`

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
- Python model: `RequestConversationHistoryRequestBody`
- Contract schema: `ConversationHistoryRequest`

## Success response

- Python model: `RequestConversationHistoryResponse`
- Contract schema: `ResponseEnvelope[ConversationHistoryAccepted]`

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
