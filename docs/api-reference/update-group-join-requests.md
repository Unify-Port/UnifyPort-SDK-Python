<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateGroupJoinRequests -->

[English](update-group-join-requests.md) | [简体中文](../zh-CN/api-reference/update-group-join-requests.md)

# `update_group_join_requests`

Explicit Python method for public Device API operation `updateGroupJoinRequests`.

- HTTP: `POST /v1/accounts/{account_id}/groups/join-requests/update`
- Python method: `update_group_join_requests`
- Node operationId: `updateGroupJoinRequests`

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
- Python model: `UpdateGroupJoinRequestsRequestBody`
- Contract schema: `GroupJoinRequestsUpdateRequest`

## Success response

- Python model: `UpdateGroupJoinRequestsResponse`
- Contract schema: `ResponseEnvelope[OkData]`

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
