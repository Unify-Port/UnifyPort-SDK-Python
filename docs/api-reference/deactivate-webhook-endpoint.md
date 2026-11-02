<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: deactivateWebhookEndpoint -->

[English](deactivate-webhook-endpoint.md) | [简体中文](../zh-CN/api-reference/deactivate-webhook-endpoint.md)

# `deactivate_webhook_endpoint`

Explicit Python method for public Device API operation `deactivateWebhookEndpoint`.

- HTTP: `POST /v1/webhook-endpoints/{endpoint_id}/deactivate`
- Python method: `deactivate_webhook_endpoint`
- Node operationId: `deactivateWebhookEndpoint`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `endpoint_id` | `endpoint_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | no | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `DeactivateWebhookEndpointRequestBody`
- Contract schema: `None`

## Success response

- Python model: `DeactivateWebhookEndpointResponse`
- Contract schema: `ResponseEnvelope[WebhookEndpoint]`

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
