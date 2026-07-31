<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: cancelAccountAuth -->

[English](cancel-account-auth.md) | [简体中文](../zh-CN/api-reference/cancel-account-auth.md)

# `cancel_account_auth`

Explicit Python method for public Device API operation `cancelAccountAuth`.

- HTTP: `POST /v1/accounts/{account_id}/auth/cancel`
- Python method: `cancel_account_auth`
- Node operationId: `cancelAccountAuth`

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
- Python model: `CancelAccountAuthRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `CancelAccountAuthResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

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
