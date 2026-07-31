<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createGroup -->

[English](create-group.md) | [简体中文](../zh-CN/api-reference/create-group.md)

# `create_group`

Explicit Python method for public Device API operation `createGroup`.

- HTTP: `POST /v1/accounts/{account_id}/groups/create`
- Python method: `create_group`
- Node operationId: `createGroup`

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
- Python model: `CreateGroupRequestBody`
- Contract schema: `GroupCreateRequest`

## Success response

- Python model: `CreateGroupResponse`
- Contract schema: `ResponseEnvelope[GroupCreateResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
