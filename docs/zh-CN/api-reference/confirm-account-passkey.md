<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: confirmAccountPasskey -->

[English](../../api-reference/confirm-account-passkey.md) | [简体中文](confirm-account-passkey.md)

# `confirm_account_passkey`

公开 Device API operation `confirmAccountPasskey` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth/passkey-confirm`
- Python 方法: `confirm_account_passkey`
- Node operationId: `confirmAccountPasskey`

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
- Python model: `ConfirmAccountPasskeyRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ConfirmAccountPasskeyResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

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
