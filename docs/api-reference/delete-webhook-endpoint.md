<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: deleteWebhookEndpoint -->

[English](delete-webhook-endpoint.md) | [简体中文](../zh-CN/api-reference/delete-webhook-endpoint.md)

# `delete_webhook_endpoint`

Explicit Python method for public Device API operation `deleteWebhookEndpoint`.

- HTTP: `DELETE /v1/webhook-endpoints/{endpoint_id}`
- Python method: `delete_webhook_endpoint`
- Node operationId: `deleteWebhookEndpoint`

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
- Python model: `DeleteWebhookEndpointRequestBody`
- Contract schema: `None`

## Success response

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
