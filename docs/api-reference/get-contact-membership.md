<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getContactMembership -->

[English](get-contact-membership.md) | [简体中文](../zh-CN/api-reference/get-contact-membership.md)

# `get_contact_membership`

Explicit Python method for public Device API operation `getContactMembership`.

- HTTP: `GET /v1/accounts/{account_id}/contacts/membership`
- Python method: `get_contact_membership`
- Node operationId: `getContactMembership`

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
- Python model: `GetContactMembershipRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetContactMembershipResponse`
- Contract schema: `ResponseEnvelope[ContactMembership]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
