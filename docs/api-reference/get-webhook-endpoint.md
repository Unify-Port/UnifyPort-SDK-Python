<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getWebhookEndpoint -->

[English](get-webhook-endpoint.md) | [简体中文](../zh-CN/api-reference/get-webhook-endpoint.md)

# `get_webhook_endpoint`

Explicit Python method for public Device API operation `getWebhookEndpoint`.

- HTTP: `GET /v1/webhook-endpoints/{endpoint_id}`
- Python method: `get_webhook_endpoint`
- Node operationId: `getWebhookEndpoint`

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

- Required: `no`
- Python model: `GetWebhookEndpointRequestBody`
- Contract schema: `None`

## Success response

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
