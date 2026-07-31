<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getGroupInviteCode -->

[English](../../api-reference/get-group-invite-code.md) | [简体中文](get-group-invite-code.md)

# `get_group_invite_code`

公开 Device API operation `getGroupInviteCode` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/groups/invite-code`
- Python 方法: `get_group_invite_code`
- Node operationId: `getGroupInviteCode`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `group_id` | `group_id` | 是 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `GetGroupInviteCodeRequestBody`
- Contract schema: `None`

## 成功响应

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
