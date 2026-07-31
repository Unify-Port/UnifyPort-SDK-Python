<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: markConversationRead -->

[English](mark-conversation-read.md) | [简体中文](../zh-CN/api-reference/mark-conversation-read.md)

# `mark_conversation_read`

Explicit Python method for public Device API operation `markConversationRead`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/read`
- Python method: `mark_conversation_read`
- Node operationId: `markConversationRead`

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
- Python model: `MarkConversationReadRequestBody`
- Contract schema: `ConversationReadRequest`

## Success response

- Python model: `MarkConversationReadResponse`
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
