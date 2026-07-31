<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: startAccountRuntime -->

[English](start-account-runtime.md) | [简体中文](../zh-CN/api-reference/start-account-runtime.md)

# `start_account_runtime`

Explicit Python method for public Device API operation `startAccountRuntime`.

- HTTP: `POST /v1/accounts/{account_id}/runtime/start`
- Python method: `start_account_runtime`
- Node operationId: `startAccountRuntime`

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
- Python model: `StartAccountRuntimeRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `StartAccountRuntimeResponse`
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
