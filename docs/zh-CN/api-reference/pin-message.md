<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: pinMessage -->

[English](../../api-reference/pin-message.md) | [简体中文](pin-message.md)

# `pin_message`

公开 Device API operation `pinMessage` 的 Python 显式方法。

- HTTP: `POST /v1/messages/pin`
- Python 方法: `pin_message`
- Node operationId: `pinMessage`

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
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `是`
- Python model: `PinMessageRequestBody`
- Contract schema: `MessagePinRequest`

## 成功响应

- Python model: `PinMessageResponse`
- Contract schema: `ResponseEnvelope[OkData]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
