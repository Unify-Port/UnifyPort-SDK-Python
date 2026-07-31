<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listContacts -->

[English](list-contacts.md) | [简体中文](../zh-CN/api-reference/list-contacts.md)

# `list_contacts`

Explicit Python method for public Device API operation `listContacts`.

- HTTP: `GET /v1/accounts/{account_id}/contacts`
- Python method: `list_contacts`
- Node operationId: `listContacts`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `cursor` | `cursor` | no | `str` |
| `limit` | `limit` | no | `int` |
| `q` | `q` | no | `str` |
| `updated_since` | `updated_since` | no | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `ListContactsRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListContactsResponse`
- Contract schema: `ResponseEnvelope[ContactListResult]`

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
