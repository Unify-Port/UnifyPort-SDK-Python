<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: setGroupJoinApprovalMode -->

[English](set-group-join-approval-mode.md) | [简体中文](../zh-CN/api-reference/set-group-join-approval-mode.md)

# `set_group_join_approval_mode`

Explicit Python method for public Device API operation `setGroupJoinApprovalMode`.

- HTTP: `POST /v1/accounts/{account_id}/groups/join-approval-mode`
- Python method: `set_group_join_approval_mode`
- Node operationId: `setGroupJoinApprovalMode`

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
- Python model: `SetGroupJoinApprovalModeRequestBody`
- Contract schema: `GroupJoinApprovalModeRequest`

## Success response

- Python model: `SetGroupJoinApprovalModeResponse`
- Contract schema: `ResponseEnvelope[OkData]`

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
