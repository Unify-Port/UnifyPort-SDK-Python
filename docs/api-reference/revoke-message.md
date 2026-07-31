<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: revokeMessage -->

[English](revoke-message.md) | [简体中文](../zh-CN/api-reference/revoke-message.md)

# `revoke_message`

Explicit Python method for public Device API operation `revokeMessage`.

- HTTP: `POST /v1/messages/revoke`
- Python method: `revoke_message`
- Node operationId: `revokeMessage`

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
- Python model: `RevokeMessageRequestBody`
- Contract schema: `MessageRevokeRequest`

## Success response

- Python model: `RevokeMessageResponse`
- Contract schema: `ResponseEnvelope[OkData]`

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
