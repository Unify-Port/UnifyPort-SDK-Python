<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listWebhookEndpoints -->

[English](../../api-reference/list-webhook-endpoints.md) | [简体中文](list-webhook-endpoints.md)

# `list_webhook_endpoints`

公开 Device API operation `listWebhookEndpoints` 的 Python 显式方法。

- HTTP: `GET /v1/webhook-endpoints`
- Python 方法: `list_webhook_endpoints`
- Node operationId: `listWebhookEndpoints`

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

- 必填: `否`
- Python model: `ListWebhookEndpointsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListWebhookEndpointsResponse`
- Contract schema: `ResponseEnvelope[list[WebhookEndpoint]]`

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
