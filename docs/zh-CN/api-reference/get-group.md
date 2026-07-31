<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getGroup -->

[English](../../api-reference/get-group.md) | [简体中文](get-group.md)

# `get_group`

公开 Device API operation `getGroup` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/groups/info`
- Python 方法: `get_group`
- Node operationId: `getGroup`

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
- Python model: `GetGroupRequestBody`
- Contract schema: `None`

## 成功响应

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
