<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getActiveCall -->

[English](../../api-reference/get-active-call.md) | [简体中文](get-active-call.md)

# `get_active_call`

公开 Device API operation `getActiveCall` 的 Python 显式方法。

- HTTP: `GET /v1/calls/active`
- Python 方法: `get_active_call`
- Node operationId: `getActiveCall`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `GetActiveCallRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `GetActiveCallResponse`
- Contract schema: `ResponseEnvelope[ActiveCallData | dict[str, JsonValue]]`

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
