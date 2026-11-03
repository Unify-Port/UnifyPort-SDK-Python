<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: startAccountAuth -->

[English](../../api-reference/start-account-auth.md) | [简体中文](start-account-auth.md)

# `start_account_auth`

公开 Device API operation `startAccountAuth` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/auth/start`
- Python 方法: `start_account_auth`
- Node operationId: `startAccountAuth`

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
- Python model: `StartAccountAuthRequestBody`
- Contract schema: `FreeFormObject`

## 成功响应

- Python model: `StartAccountAuthResponse`
- Contract schema: `ResponseEnvelope[StartCodeAuthData]`

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
