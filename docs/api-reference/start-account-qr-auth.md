<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: startAccountQrAuth -->

[English](start-account-qr-auth.md) | [简体中文](../zh-CN/api-reference/start-account-qr-auth.md)

# `start_account_qr_auth`

Explicit Python method for public Device API operation `startAccountQrAuth`.

- HTTP: `POST /v1/accounts/{account_id}/auth/qr/start`
- Python method: `start_account_qr_auth`
- Node operationId: `startAccountQrAuth`

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
- Python model: `StartAccountQrAuthRequestBody`
- Contract schema: `FreeFormObject`

## Success response

- Python model: `StartAccountQrAuthResponse`
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
