<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateAccount -->

[English](../../api-reference/update-account.md) | [简体中文](update-account.md)

# `update_account`

公开 Device API operation `updateAccount` 的 Python 显式方法。

- HTTP: `PATCH /v1/accounts/{account_id}`
- Python 方法: `update_account`
- Node operationId: `updateAccount`

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

- 必填: `是`
- Python model: `UpdateAccountRequestBody`
- Contract schema: `AccountUpdateRequest`

## 成功响应

- Python model: `UpdateAccountResponse`
- Contract schema: `ResponseEnvelope[Account]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
