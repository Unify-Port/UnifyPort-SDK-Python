<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listConversationLabels -->

[English](../../api-reference/list-conversation-labels.md) | [简体中文](list-conversation-labels.md)

# `list_conversation_labels`

公开 Device API operation `listConversationLabels` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/conversations/labels`
- Python 方法: `list_conversation_labels`
- Node operationId: `listConversationLabels`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `cursor` | `cursor` | 否 | `str` |
| `limit` | `limit` | 否 | `int` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListConversationLabelsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListConversationLabelsResponse`
- Contract schema: `ResponseEnvelope[ConversationLabelListResult]`

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
