<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: hangupCall -->

[English](../../api-reference/hangup-call.md) | [简体中文](hangup-call.md)

# `hangup_call`

公开 Device API operation `hangupCall` 的 Python 显式方法。

- HTTP: `POST /v1/calls/{call_id}/hangup`
- Python 方法: `hangup_call`
- Node operationId: `hangupCall`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `call_id` | `call_id` | 是 | `str` |

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
- Python model: `HangupCallRequestBody`
- Contract schema: `dict[str, JsonValue]`

## 成功响应

- Python model: `HangupCallResponse`
- Contract schema: `ResponseEnvelope[EndedCallData]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `true` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `destructive` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
