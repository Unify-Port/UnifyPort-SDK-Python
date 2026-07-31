<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: rotateApiKey -->

[English](../../api-reference/rotate-api-key.md) | [简体中文](rotate-api-key.md)

# `rotate_api_key`

公开 Device API operation `rotateApiKey` 的 Python 显式方法。

- HTTP: `POST /v1/api-keys/{key_id}/rotate`
- Python 方法: `rotate_api_key`
- Node operationId: `rotateApiKey`

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
- Python model: `RotateApiKeyRequestBody`
- Contract schema: `APIKeyCreateRequest`

## 成功响应

- Python model: `RotateApiKeyResponse`
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
