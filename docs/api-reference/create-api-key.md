<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createApiKey -->

[English](create-api-key.md) | [简体中文](../zh-CN/api-reference/create-api-key.md)

# `create_api_key`

Explicit Python method for public Device API operation `createApiKey`.

- HTTP: `POST /v1/api-keys`
- Python method: `create_api_key`
- Node operationId: `createApiKey`

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
- Python model: `CreateApiKeyRequestBody`
- Contract schema: `APIKeyCreateRequest`

## Success response

- Python model: `CreateApiKeyResponse`
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
