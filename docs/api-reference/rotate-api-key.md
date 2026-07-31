<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: rotateApiKey -->

[English](rotate-api-key.md) | [简体中文](../zh-CN/api-reference/rotate-api-key.md)

# `rotate_api_key`

Explicit Python method for public Device API operation `rotateApiKey`.

- HTTP: `POST /v1/api-keys/{key_id}/rotate`
- Python method: `rotate_api_key`
- Node operationId: `rotateApiKey`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `key_id` | `key_id` | yes | `str` |

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
- Python model: `RotateApiKeyRequestBody`
- Contract schema: `APIKeyCreateRequest`

## Success response

- Python model: `RotateApiKeyResponse`
- Contract schema: `ResponseEnvelope[APIKeyCreateResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
