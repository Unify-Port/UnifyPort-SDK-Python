<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getGroup -->

[English](get-group.md) | [简体中文](../zh-CN/api-reference/get-group.md)

# `get_group`

Explicit Python method for public Device API operation `getGroup`.

- HTTP: `GET /v1/accounts/{account_id}/groups/info`
- Python method: `get_group`
- Node operationId: `getGroup`

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
- Python model: `GetGroupRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetGroupResponse`
- Contract schema: `ResponseEnvelope[Group]`

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
