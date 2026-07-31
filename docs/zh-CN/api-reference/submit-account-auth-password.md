<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: submitAccountAuthPassword -->

[English](../../api-reference/submit-account-auth-password.md) | [简体中文](submit-account-auth-password.md)

# `submit_account_auth_password`

公开 Device API operation `submitAccountAuthPassword` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth/password`
- Python 方法: `submit_account_auth_password`
- Node operationId: `submitAccountAuthPassword`

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
- Python model: `SubmitAccountAuthPasswordRequestBody`
- Contract schema: `FreeFormObject`

## 成功响应

- Python model: `SubmitAccountAuthPasswordResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
