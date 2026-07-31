<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateGroupMembers -->

[English](update-group-members.md) | [简体中文](../zh-CN/api-reference/update-group-members.md)

# `update_group_members`

Explicit Python method for public Device API operation `updateGroupMembers`.

- HTTP: `POST /v1/accounts/{account_id}/groups/members`
- Python method: `update_group_members`
- Node operationId: `updateGroupMembers`

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
- Python model: `UpdateGroupMembersRequestBody`
- Contract schema: `GroupMemberUpdateRequest`

## Success response

- Python model: `UpdateGroupMembersResponse`
- Contract schema: `ResponseEnvelope[OkData]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `true` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `destructive` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
