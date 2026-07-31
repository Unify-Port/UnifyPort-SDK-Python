<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createWebhookEndpoint -->

[English](create-webhook-endpoint.md) | [简体中文](../zh-CN/api-reference/create-webhook-endpoint.md)

# `create_webhook_endpoint`

Explicit Python method for public Device API operation `createWebhookEndpoint`.

- HTTP: `POST /v1/webhook-endpoints`
- Python method: `create_webhook_endpoint`
- Node operationId: `createWebhookEndpoint`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

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
- Python model: `CreateWebhookEndpointRequestBody`
- Contract schema: `WebhookEndpointRequest`

## Success response

- Python model: `CreateWebhookEndpointResponse`
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
