<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listConversations -->

[English](../../api-reference/list-conversations.md) | [简体中文](list-conversations.md)

# `list_conversations`

公开 Device API operation `listConversations` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/conversations`
- Python 方法: `list_conversations`
- Node operationId: `listConversations`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `type` | `type` | 否 | `str` |
| `cursor` | `cursor` | 否 | `str` |
| `limit` | `limit` | 否 | `int` |
| `label_id` | `label_id` | 否 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListConversationsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListConversationsResponse`
- Contract schema: `ResponseEnvelope[ConversationListResult]`

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
