<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getAccountOperation -->

[English](../../api-reference/get-account-operation.md) | [简体中文](get-account-operation.md)

# `get_account_operation`

公开 Device API operation `getAccountOperation` 的 Python 显式方法。

- HTTP: `GET /v1/account-operations/{operation_id}`
- Python 方法: `get_account_operation`
- Node operationId: `getAccountOperation`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `operation_id` | `operation_id` | 是 | `str` |

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
- Python model: `GetAccountOperationRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `GetAccountOperationResponse`
- Contract schema: `ResponseEnvelope[AccountOperation]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
