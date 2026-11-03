<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getActiveCall -->

[English](get-active-call.md) | [简体中文](../zh-CN/api-reference/get-active-call.md)

# `get_active_call`

Explicit Python method for public Device API operation `getActiveCall`.

- HTTP: `GET /v1/calls/active`
- Python method: `get_active_call`
- Node operationId: `getActiveCall`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `GetActiveCallRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetActiveCallResponse`
- Contract schema: `ResponseEnvelope[ActiveCallData | dict[str, JsonValue]]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
