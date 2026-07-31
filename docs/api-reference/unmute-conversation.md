<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: unmuteConversation -->

[English](unmute-conversation.md) | [简体中文](../zh-CN/api-reference/unmute-conversation.md)

# `unmute_conversation`

Explicit Python method for public Device API operation `unmuteConversation`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/unmute`
- Python method: `unmute_conversation`
- Node operationId: `unmuteConversation`

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
- Python model: `UnmuteConversationRequestBody`
- Contract schema: `ConversationIdRequest`

## Success response

- Python model: `UnmuteConversationResponse`
- Contract schema: `ResponseEnvelope[OkData]`

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
