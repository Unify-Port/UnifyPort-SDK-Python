<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createAccountAuthSession -->

[English](create-account-auth-session.md) | [简体中文](../zh-CN/api-reference/create-account-auth-session.md)

# `create_account_auth_session`

Explicit Python method for public Device API operation `createAccountAuthSession`.

- HTTP: `POST /v1/accounts/{account_id}/auth-sessions`
- Python method: `create_account_auth_session`
- Node operationId: `createAccountAuthSession`

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
- Python model: `CreateAccountAuthSessionRequestBody`
- Contract schema: `None`

## Success response

- Python model: `CreateAccountAuthSessionResponse`
- Contract schema: `ResponseEnvelope[ProviderAuthSession]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
