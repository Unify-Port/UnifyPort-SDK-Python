<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getAccountOperation -->

[English](get-account-operation.md) | [简体中文](../zh-CN/api-reference/get-account-operation.md)

# `get_account_operation`

Explicit Python method for public Device API operation `getAccountOperation`.

- HTTP: `GET /v1/account-operations/{operation_id}`
- Python method: `get_account_operation`
- Node operationId: `getAccountOperation`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `operation_id` | `operation_id` | yes | `str` |

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
- Python model: `GetAccountOperationRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetAccountOperationResponse`
- Contract schema: `ResponseEnvelope[AccountOperation]`

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
