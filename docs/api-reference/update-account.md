<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateAccount -->

[English](update-account.md) | [简体中文](../zh-CN/api-reference/update-account.md)

# `update_account`

Explicit Python method for public Device API operation `updateAccount`.

- HTTP: `PATCH /v1/accounts/{account_id}`
- Python method: `update_account`
- Node operationId: `updateAccount`

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
- Python model: `UpdateAccountRequestBody`
- Contract schema: `AccountRequest`

## Success response

- Python model: `UpdateAccountResponse`
- Contract schema: `ResponseEnvelope[Account]`

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
