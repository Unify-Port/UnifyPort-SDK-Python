<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateApiKeyStatus -->

[English](update-api-key-status.md) | [简体中文](../zh-CN/api-reference/update-api-key-status.md)

# `update_api_key_status`

Explicit Python method for public Device API operation `updateApiKeyStatus`.

- HTTP: `PATCH /v1/api-keys/{key_id}`
- Python method: `update_api_key_status`
- Node operationId: `updateApiKeyStatus`

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
- Python model: `UpdateApiKeyStatusRequestBody`
- Contract schema: `APIKeyStatusUpdateRequest`

## Success response

- Python model: `UpdateApiKeyStatusResponse`
- Contract schema: `ResponseEnvelope[APIKey]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `true` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `write` |
| `pythonMcpExposure` | `never` |
