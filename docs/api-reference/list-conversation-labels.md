<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listConversationLabels -->

[English](list-conversation-labels.md) | [简体中文](../zh-CN/api-reference/list-conversation-labels.md)

# `list_conversation_labels`

Explicit Python method for public Device API operation `listConversationLabels`.

- HTTP: `GET /v1/accounts/{account_id}/conversations/labels`
- Python method: `list_conversation_labels`
- Node operationId: `listConversationLabels`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `cursor` | `cursor` | no | `str` |
| `limit` | `limit` | no | `int` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `ListConversationLabelsRequestBody`
- Contract schema: `None`

## Success response

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
