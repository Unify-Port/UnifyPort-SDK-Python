<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getConversation -->

[English](get-conversation.md) | [简体中文](../zh-CN/api-reference/get-conversation.md)

# `get_conversation`

Explicit Python method for public Device API operation `getConversation`.

- HTTP: `GET /v1/accounts/{account_id}/conversations/info`
- Python method: `get_conversation`
- Node operationId: `getConversation`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `conversation_id` | `conversation_id` | yes | `str` |
| `type` | `type` | no | `ConversationType` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `GetConversationRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetConversationResponse`
- Contract schema: `ResponseEnvelope[Conversation]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
