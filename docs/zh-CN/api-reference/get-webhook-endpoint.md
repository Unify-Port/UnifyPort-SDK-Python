<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getWebhookEndpoint -->

[English](../../api-reference/get-webhook-endpoint.md) | [简体中文](get-webhook-endpoint.md)

# `get_webhook_endpoint`

公开 Device API operation `getWebhookEndpoint` 的 Python 显式方法。

- HTTP: `GET /v1/webhook-endpoints/{endpoint_id}`
- Python 方法: `get_webhook_endpoint`
- Node operationId: `getWebhookEndpoint`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `endpoint_id` | `endpoint_id` | 是 | `str` |

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
- Python model: `GetWebhookEndpointRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `GetWebhookEndpointResponse`
- Contract schema: `ResponseEnvelope[WebhookEndpoint]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
