<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: submitAccountPasskeyResponse -->

[English](submit-account-passkey-response.md) | [简体中文](../zh-CN/api-reference/submit-account-passkey-response.md)

# `submit_account_passkey_response`

Explicit Python method for public Device API operation `submitAccountPasskeyResponse`.

- HTTP: `POST /v1/accounts/{account_id}/auth/passkey-response`
- Python method: `submit_account_passkey_response`
- Node operationId: `submitAccountPasskeyResponse`

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

- Required: `yes`
- Python model: `SubmitAccountPasskeyResponseRequestBody`
- Contract schema: `PasskeyResponseRequest`

## Success response

- Python model: `SubmitAccountPasskeyResponseResponse`
- Contract schema: `ResponseEnvelope[FreeFormObject]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `true` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
