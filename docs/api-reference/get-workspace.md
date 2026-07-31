<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getWorkspace -->

[English](get-workspace.md) | [简体中文](../zh-CN/api-reference/get-workspace.md)

# `get_workspace`

Explicit Python method for public Device API operation `getWorkspace`.

- HTTP: `GET /v1/workspace`
- Python method: `get_workspace`
- Node operationId: `getWorkspace`

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
- Python model: `GetWorkspaceRequestBody`
- Contract schema: `None`

## Success response

- Python model: `GetWorkspaceResponse`
- Contract schema: `ResponseEnvelope[Workspace]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `true` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `read` |
| `pythonMcpExposure` | `never` |
