<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: checkAccountQrAuth -->

[English](../../api-reference/check-account-qr-auth.md) | [简体中文](check-account-qr-auth.md)

# `check_account_qr_auth`

公开 Device API operation `checkAccountQrAuth` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth/qr/check`
- Python 方法: `check_account_qr_auth`
- Node operationId: `checkAccountQrAuth`

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
- Python model: `CheckAccountQrAuthRequestBody`
- Contract schema: `FreeFormObject`

## 成功响应

- Python model: `CheckAccountQrAuthResponse`
- Contract schema: `ResponseEnvelope[QRAuthCheckData]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
