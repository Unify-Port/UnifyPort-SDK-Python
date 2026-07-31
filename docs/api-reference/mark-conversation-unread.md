<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: markConversationUnread -->

[English](mark-conversation-unread.md) | [简体中文](../zh-CN/api-reference/mark-conversation-unread.md)

# `mark_conversation_unread`

Explicit Python method for public Device API operation `markConversationUnread`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/unread`
- Python method: `mark_conversation_unread`
- Node operationId: `markConversationUnread`

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
- Python model: `MarkConversationUnreadRequestBody`
- Contract schema: `ConversationIdRequest`

## Success response

- Python model: `MarkConversationUnreadResponse`
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
