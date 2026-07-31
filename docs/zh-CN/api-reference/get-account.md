<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getAccount -->

[English](../../api-reference/get-account.md) | [简体中文](get-account.md)

# `get_account`

公开 Device API operation `getAccount` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}`
- Python 方法: `get_account`
- Node operationId: `getAccount`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `GetAccountRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `GetAccountResponse`
- Contract schema: `ResponseEnvelope[Account]`

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
