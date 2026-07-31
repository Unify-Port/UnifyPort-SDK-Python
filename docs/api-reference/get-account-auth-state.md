<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getAccountAuthState -->

[English](get-account-auth-state.md) | [简体中文](../zh-CN/api-reference/get-account-auth-state.md)

# `get_account_auth_state`

Explicit Python method for public Device API operation `getAccountAuthState`.

- HTTP: `GET /v1/accounts/{account_id}/auth`
- Python method: `get_account_auth_state`
- Node operationId: `getAccountAuthState`

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
- Python model: `GetAccountAuthStateRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetAccountAuthStateResponse`
- Contract schema: `ResponseEnvelope[AccountSession]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
