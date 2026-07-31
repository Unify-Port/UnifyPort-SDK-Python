<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getGroupInviteCode -->

[English](get-group-invite-code.md) | [简体中文](../zh-CN/api-reference/get-group-invite-code.md)

# `get_group_invite_code`

Explicit Python method for public Device API operation `getGroupInviteCode`.

- HTTP: `GET /v1/accounts/{account_id}/groups/invite-code`
- Python method: `get_group_invite_code`
- Node operationId: `getGroupInviteCode`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `group_id` | `group_id` | yes | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `GetGroupInviteCodeRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetGroupInviteCodeResponse`
- Contract schema: `ResponseEnvelope[GroupInviteCode]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
