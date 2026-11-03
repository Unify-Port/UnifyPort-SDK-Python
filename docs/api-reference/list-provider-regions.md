<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listProviderRegions -->

[English](list-provider-regions.md) | [简体中文](../zh-CN/api-reference/list-provider-regions.md)

# `list_provider_regions`

Explicit Python method for public Device API operation `listProviderRegions`.

- HTTP: `GET /v1/providers/{provider}/regions`
- Python method: `list_provider_regions`
- Node operationId: `listProviderRegions`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `provider` | `provider` | yes | `ProviderInputName` |

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
- Python model: `ListProviderRegionsRequestBody`
- Contract schema: `None`

## Success response

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
