<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listAccounts -->

[English](../../api-reference/list-accounts.md) | [简体中文](list-accounts.md)

# `list_accounts`

公开 Device API operation `listAccounts` 的 Python 显式方法。

- HTTP: `GET /v1/accounts`
- Python 方法: `list_accounts`
- Node operationId: `listAccounts`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `limit` | `limit` | 否 | `int` |
| `cursor` | `cursor` | 否 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListAccountsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListAccountsResponse`
- Contract schema: `ResponseEnvelope[AccountListResult]`

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
