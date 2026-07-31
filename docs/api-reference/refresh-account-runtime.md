<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: refreshAccountRuntime -->

[English](refresh-account-runtime.md) | [简体中文](../zh-CN/api-reference/refresh-account-runtime.md)

# `refresh_account_runtime`

Explicit Python method for public Device API operation `refreshAccountRuntime`.

- HTTP: `POST /v1/accounts/{account_id}/runtime/refresh`
- Python method: `refresh_account_runtime`
- Node operationId: `refreshAccountRuntime`

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
- Python model: `RefreshAccountRuntimeRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `RefreshAccountRuntimeResponse`
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
