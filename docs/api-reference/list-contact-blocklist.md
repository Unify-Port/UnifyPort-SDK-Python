<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listContactBlocklist -->

[English](list-contact-blocklist.md) | [简体中文](../zh-CN/api-reference/list-contact-blocklist.md)

# `list_contact_blocklist`

Explicit Python method for public Device API operation `listContactBlocklist`.

- HTTP: `GET /v1/accounts/{account_id}/contacts/blocklist`
- Python method: `list_contact_blocklist`
- Node operationId: `listContactBlocklist`

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
- Python model: `ListContactBlocklistRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListContactBlocklistResponse`
- Contract schema: `ResponseEnvelope[ContactBlocklistResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
