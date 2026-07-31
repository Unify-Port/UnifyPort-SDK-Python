<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: updateApiKeyStatus -->

[English](../../api-reference/update-api-key-status.md) | [简体中文](update-api-key-status.md)

# `update_api_key_status`

公开 Device API operation `updateApiKeyStatus` 的 Python 显式方法。

- HTTP: `PATCH /v1/api-keys/{key_id}`
- Python 方法: `update_api_key_status`
- Node operationId: `updateApiKeyStatus`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `key_id` | `key_id` | 是 | `str` |

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
- Python model: `UpdateApiKeyStatusRequestBody`
- Contract schema: `APIKeyStatusUpdateRequest`

## 成功响应

- Python model: `UpdateApiKeyStatusResponse`
- Contract schema: `ResponseEnvelope[APIKey]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `true` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `write` |
| `pythonMcpExposure` | `never` |
