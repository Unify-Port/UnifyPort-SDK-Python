<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateWorkspace -->

[English](update-workspace.md) | [简体中文](../zh-CN/api-reference/update-workspace.md)

# `update_workspace`

Explicit Python method for public Device API operation `updateWorkspace`.

- HTTP: `PATCH /v1/workspace`
- Python method: `update_workspace`
- Node operationId: `updateWorkspace`

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

- Required: `yes`
- Python model: `UpdateWorkspaceRequestBody`
- Contract schema: `WorkspaceUpdateRequest`

## Success response

- Python model: `UpdateWorkspaceResponse`
- Contract schema: `ResponseEnvelope[Workspace]`

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
