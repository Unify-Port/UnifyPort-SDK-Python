<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getConversation -->

[English](../../api-reference/get-conversation.md) | [简体中文](get-conversation.md)

# `get_conversation`

公开 Device API operation `getConversation` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/conversations/info`
- Python 方法: `get_conversation`
- Node operationId: `getConversation`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `conversation_id` | `conversation_id` | 是 | `str` |
| `type` | `type` | 否 | `ConversationType` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `GetConversationRequestBody`
- Contract schema: `None`

## 成功响应

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
