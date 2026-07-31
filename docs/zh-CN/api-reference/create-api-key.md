<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: createApiKey -->

[English](../../api-reference/create-api-key.md) | [简体中文](create-api-key.md)

# `create_api_key`

公开 Device API operation `createApiKey` 的 Python 显式方法。

- HTTP: `POST /v1/api-keys`
- Python 方法: `create_api_key`
- Node operationId: `createApiKey`

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

- 必填: `是`
- Python model: `CreateApiKeyRequestBody`
- Contract schema: `APIKeyCreateRequest`

## 成功响应

- Python model: `CreateApiKeyResponse`
- Contract schema: `ResponseEnvelope[APIKeyCreateResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `true` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
