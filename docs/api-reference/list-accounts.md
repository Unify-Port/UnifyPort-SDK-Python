<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listAccounts -->

[English](list-accounts.md) | [简体中文](../zh-CN/api-reference/list-accounts.md)

# `list_accounts`

Explicit Python method for public Device API operation `listAccounts`.

- HTTP: `GET /v1/accounts`
- Python method: `list_accounts`
- Node operationId: `listAccounts`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| None | - | - | - |

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
- Python model: `ListAccountsRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListAccountsResponse`
- Contract schema: `ResponseEnvelope[list[Account]]`

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
