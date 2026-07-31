<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: sendMessage -->

[English](send-message.md) | [简体中文](../zh-CN/api-reference/send-message.md)

# `send_message`

Explicit Python method for public Device API operation `sendMessage`.

- HTTP: `POST /v1/messages`
- Python method: `send_message`
- Node operationId: `sendMessage`

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
- Python model: `SendMessageRequestBody`
- Contract schema: `SendMessageRequest`

## Success response

- Python model: `SendMessageResponse`
- Contract schema: `ResponseEnvelope[SendMessageResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
