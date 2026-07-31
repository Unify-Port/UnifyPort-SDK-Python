<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listGroups -->

[English](../../api-reference/list-groups.md) | [简体中文](list-groups.md)

# `list_groups`

公开 Device API operation `listGroups` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/groups`
- Python 方法: `list_groups`
- Node operationId: `listGroups`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `cursor` | `cursor` | 否 | `str` |
| `limit` | `limit` | 否 | `int` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListGroupsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListGroupsResponse`
- Contract schema: `ResponseEnvelope[GroupListResult]`

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
