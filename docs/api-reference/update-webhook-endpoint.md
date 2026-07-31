<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateWebhookEndpoint -->

[English](update-webhook-endpoint.md) | [简体中文](../zh-CN/api-reference/update-webhook-endpoint.md)

# `update_webhook_endpoint`

Explicit Python method for public Device API operation `updateWebhookEndpoint`.

- HTTP: `PATCH /v1/webhook-endpoints/{endpoint_id}`
- Python method: `update_webhook_endpoint`
- Node operationId: `updateWebhookEndpoint`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `endpoint_id` | `endpoint_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `yes`
- Python model: `UpdateWebhookEndpointRequestBody`
- Contract schema: `WebhookEndpointRequest`

## Success response

- Python model: `UpdateWebhookEndpointResponse`
- Contract schema: `ResponseEnvelope[WebhookEndpoint]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
