<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateGroupJoinRequests -->

[English](../../api-reference/update-group-join-requests.md) | [简体中文](update-group-join-requests.md)

# `update_group_join_requests`

公开 Device API operation `updateGroupJoinRequests` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/groups/join-requests/update`
- Python 方法: `update_group_join_requests`
- Node operationId: `updateGroupJoinRequests`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `是`
- Python model: `UpdateGroupJoinRequestsRequestBody`
- Contract schema: `GroupJoinRequestsUpdateRequest`

## 成功响应

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
