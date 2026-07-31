<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listConversationMembers -->

[English](list-conversation-members.md) | [简体中文](../zh-CN/api-reference/list-conversation-members.md)

# `list_conversation_members`

Explicit Python method for public Device API operation `listConversationMembers`.

- HTTP: `GET /v1/accounts/{account_id}/conversations/members`
- Python method: `list_conversation_members`
- Node operationId: `listConversationMembers`

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
| `cursor` | `cursor` | no | `str` |
| `limit` | `limit` | no | `int` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `ListConversationMembersRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListConversationMembersResponse`
- Contract schema: `ResponseEnvelope[ConversationMemberListResult]`

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
