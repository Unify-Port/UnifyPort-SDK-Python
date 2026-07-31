<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: importAccountAuthSession -->

[English](import-account-auth-session.md) | [简体中文](../zh-CN/api-reference/import-account-auth-session.md)

# `import_account_auth_session`

Explicit Python method for public Device API operation `importAccountAuthSession`.

- HTTP: `POST /v1/accounts/{account_id}/auth/session`
- Python method: `import_account_auth_session`
- Node operationId: `importAccountAuthSession`

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
- Python model: `ImportAccountAuthSessionRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `ImportAccountAuthSessionResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
