<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: deleteWebhookEndpoint -->

[English](../../api-reference/delete-webhook-endpoint.md) | [简体中文](delete-webhook-endpoint.md)

# `delete_webhook_endpoint`

公开 Device API operation `deleteWebhookEndpoint` 的 Python 显式方法。

- HTTP: `DELETE /v1/webhook-endpoints/{endpoint_id}`
- Python 方法: `delete_webhook_endpoint`
- Node operationId: `deleteWebhookEndpoint`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `endpoint_id` | `endpoint_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 否 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `DeleteWebhookEndpointRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `DeleteWebhookEndpointResponse`
- Contract schema: `None`

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
