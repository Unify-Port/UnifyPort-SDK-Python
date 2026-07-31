<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listApiKeys -->

[English](list-api-keys.md) | [简体中文](../zh-CN/api-reference/list-api-keys.md)

# `list_api_keys`

Explicit Python method for public Device API operation `listApiKeys`.

- HTTP: `GET /v1/api-keys`
- Python method: `list_api_keys`
- Node operationId: `listApiKeys`

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

- Required: `no`
- Python model: `ListApiKeysRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListApiKeysResponse`
- Contract schema: `ResponseEnvelope[list[APIKey]]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `true` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `read` |
| `pythonMcpExposure` | `never` |
