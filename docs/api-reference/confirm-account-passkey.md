<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: confirmAccountPasskey -->

[English](confirm-account-passkey.md) | [简体中文](../zh-CN/api-reference/confirm-account-passkey.md)

# `confirm_account_passkey`

Explicit Python method for public Device API operation `confirmAccountPasskey`.

- HTTP: `POST /v1/accounts/{account_id}/auth/passkey-confirm`
- Python method: `confirm_account_passkey`
- Node operationId: `confirmAccountPasskey`

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
- Python model: `ConfirmAccountPasskeyRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ConfirmAccountPasskeyResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

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
