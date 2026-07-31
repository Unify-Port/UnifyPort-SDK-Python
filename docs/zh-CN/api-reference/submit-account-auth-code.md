<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: submitAccountAuthCode -->

[English](../../api-reference/submit-account-auth-code.md) | [简体中文](submit-account-auth-code.md)

# `submit_account_auth_code`

公开 Device API operation `submitAccountAuthCode` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth/code`
- Python 方法: `submit_account_auth_code`
- Node operationId: `submitAccountAuthCode`

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
- Python model: `SubmitAccountAuthCodeRequestBody`
- Contract schema: `FreeFormObject`

## 成功响应

- Python model: `SubmitAccountAuthCodeResponse`
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
