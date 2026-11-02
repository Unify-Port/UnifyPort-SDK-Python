<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createAccount -->

[English](../../api-reference/create-account.md) | [简体中文](create-account.md)

# `create_account`

公开 Device API operation `createAccount` 的 Python 显式方法。

- HTTP: `POST /v1/accounts`
- Python 方法: `create_account`
- Node operationId: `createAccount`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `Idempotency-Key` | `idempotency_key` | 否 | `str` |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `是`
- Python model: `CreateAccountRequestBody`
- Contract schema: `AccountCreateRequest`

## 成功响应

- Python model: `CreateAccountResponse`
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
