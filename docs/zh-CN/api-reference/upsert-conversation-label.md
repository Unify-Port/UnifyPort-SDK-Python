<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: upsertConversationLabel -->

[English](../../api-reference/upsert-conversation-label.md) | [简体中文](upsert-conversation-label.md)

# `upsert_conversation_label`

公开 Device API operation `upsertConversationLabel` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/conversations/labels/upsert`
- Python 方法: `upsert_conversation_label`
- Node operationId: `upsertConversationLabel`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `是`
- Python model: `UpsertConversationLabelRequestBody`
- Contract schema: `ConversationLabelUpsertRequest`

## 成功响应

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
