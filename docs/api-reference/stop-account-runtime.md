<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: stopAccountRuntime -->

[English](stop-account-runtime.md) | [简体中文](../zh-CN/api-reference/stop-account-runtime.md)

# `stop_account_runtime`

Explicit Python method for public Device API operation `stopAccountRuntime`.

- HTTP: `POST /v1/accounts/{account_id}/runtime/stop`
- Python method: `stop_account_runtime`
- Node operationId: `stopAccountRuntime`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

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
- Python model: `StopAccountRuntimeRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `StopAccountRuntimeResponse`
- Contract schema: `ResponseEnvelope[RuntimeActionResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
