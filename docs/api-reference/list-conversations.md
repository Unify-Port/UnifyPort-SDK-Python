<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listConversations -->

[English](list-conversations.md) | [简体中文](../zh-CN/api-reference/list-conversations.md)

# `list_conversations`

Explicit Python method for public Device API operation `listConversations`.

- HTTP: `GET /v1/accounts/{account_id}/conversations`
- Python method: `list_conversations`
- Node operationId: `listConversations`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `type` | `type` | no | `str` |
| `cursor` | `cursor` | no | `str` |
| `limit` | `limit` | no | `int` |
| `label_id` | `label_id` | no | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `ListConversationsRequestBody`
- Contract schema: `None`

## Success response

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
