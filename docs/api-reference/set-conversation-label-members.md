<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: setConversationLabelMembers -->

[English](set-conversation-label-members.md) | [简体中文](../zh-CN/api-reference/set-conversation-label-members.md)

# `set_conversation_label_members`

Explicit Python method for public Device API operation `setConversationLabelMembers`.

- HTTP: `POST /v1/accounts/{account_id}/conversations/labels`
- Python method: `set_conversation_label_members`
- Node operationId: `setConversationLabelMembers`

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
- Python model: `SetConversationLabelMembersRequestBody`
- Contract schema: `ConversationLabelMembersRequest`

## Success response

- Python model: `SetConversationLabelMembersResponse`
- Contract schema: `ResponseEnvelope[ConversationLabelMembersResult]`

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
