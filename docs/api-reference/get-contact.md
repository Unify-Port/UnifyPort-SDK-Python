<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getContact -->

[English](get-contact.md) | [简体中文](../zh-CN/api-reference/get-contact.md)

# `get_contact`

Explicit Python method for public Device API operation `getContact`.

- HTTP: `GET /v1/accounts/{account_id}/contacts/info`
- Python method: `get_contact`
- Node operationId: `getContact`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `contact_id` | `contact_id` | yes | `str` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `GetContactRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetContactResponse`
- Contract schema: `ResponseEnvelope[Contact]`

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
