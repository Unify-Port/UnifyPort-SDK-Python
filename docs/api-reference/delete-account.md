<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: deleteAccount -->

[English](delete-account.md) | [简体中文](../zh-CN/api-reference/delete-account.md)

# `delete_account`

Explicit Python method for public Device API operation `deleteAccount`.

- HTTP: `DELETE /v1/accounts/{account_id}`
- Python method: `delete_account`
- Node operationId: `deleteAccount`

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
- Python model: `DeleteAccountRequestBody`
- Contract schema: `None`

## Success response

- Python model: `DeleteAccountResponse`
- Contract schema: `None`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `true` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `destructive` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
