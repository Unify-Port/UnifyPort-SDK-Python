<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getWorkspace -->

[English](../../api-reference/get-workspace.md) | [简体中文](get-workspace.md)

# `get_workspace`

公开 Device API operation `getWorkspace` 的 Python 显式方法。

- HTTP: `GET /v1/workspace`
- Python 方法: `get_workspace`
- Node operationId: `getWorkspace`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| 无 | - | - | - |

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

- 必填: `否`
- Python model: `GetWorkspaceRequestBody`
- Contract schema: `None`

## 成功响应

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
