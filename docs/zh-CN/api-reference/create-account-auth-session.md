<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createAccountAuthSession -->

[English](../../api-reference/create-account-auth-session.md) | [简体中文](create-account-auth-session.md)

# `create_account_auth_session`

公开 Device API operation `createAccountAuthSession` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth-sessions`
- Python 方法: `create_account_auth_session`
- Node operationId: `createAccountAuthSession`

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
- Python model: `CreateAccountAuthSessionRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `CreateAccountAuthSessionResponse`
- Contract schema: `ResponseEnvelope[ProviderAuthSession]`

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
