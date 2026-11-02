<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listWebhookEndpoints -->

[English](list-webhook-endpoints.md) | [简体中文](../zh-CN/api-reference/list-webhook-endpoints.md)

# `list_webhook_endpoints`

Explicit Python method for public Device API operation `listWebhookEndpoints`.

- HTTP: `GET /v1/webhook-endpoints`
- Python method: `list_webhook_endpoints`
- Node operationId: `listWebhookEndpoints`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

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
- Python model: `ListWebhookEndpointsRequestBody`
- Contract schema: `None`

## Success response

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
