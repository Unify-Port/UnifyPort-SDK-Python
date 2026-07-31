<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listApiKeys -->

[English](../../api-reference/list-api-keys.md) | [简体中文](list-api-keys.md)

# `list_api_keys`

公开 Device API operation `listApiKeys` 的 Python 显式方法。

- HTTP: `GET /v1/api-keys`
- Python 方法: `list_api_keys`
- Node operationId: `listApiKeys`

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
- Python model: `ListApiKeysRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListApiKeysResponse`
- Contract schema: `ResponseEnvelope[list[APIKey]]`

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
