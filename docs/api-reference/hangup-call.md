<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: hangupCall -->

[English](hangup-call.md) | [简体中文](../zh-CN/api-reference/hangup-call.md)

# `hangup_call`

Explicit Python method for public Device API operation `hangupCall`.

- HTTP: `POST /v1/calls/{call_id}/hangup`
- Python method: `hangup_call`
- Node operationId: `hangupCall`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `call_id` | `call_id` | yes | `str` |

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
- Python model: `HangupCallRequestBody`
- Contract schema: `dict[str, JsonValue]`

## Success response

- Python model: `HangupCallResponse`
- Contract schema: `ResponseEnvelope[EndedCallData]`

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
