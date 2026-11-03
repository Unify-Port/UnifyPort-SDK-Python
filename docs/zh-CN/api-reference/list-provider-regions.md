<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listProviderRegions -->

[English](../../api-reference/list-provider-regions.md) | [简体中文](list-provider-regions.md)

# `list_provider_regions`

公开 Device API operation `listProviderRegions` 的 Python 显式方法。

- HTTP: `GET /v1/providers/{provider}/regions`
- Python 方法: `list_provider_regions`
- Node operationId: `listProviderRegions`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `provider` | `provider` | 是 | `ProviderInputName` |

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
- Python model: `ListProviderRegionsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListProviderRegionsResponse`
- Contract schema: `ResponseEnvelope[ProviderRegionsResponse]`

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
