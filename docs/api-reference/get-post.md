<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getPost -->

[English](get-post.md) | [简体中文](../zh-CN/api-reference/get-post.md)

# `get_post`

Explicit Python method for public Device API operation `getPost`.

- HTTP: `POST /v1/accounts/{account_id}/posts/info`
- Python method: `get_post`
- Node operationId: `getPost`

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
- Python model: `GetPostRequestBody`
- Contract schema: `PostInfoRequest`

## Success response

- Python model: `GetPostResponse`
- Contract schema: `ResponseEnvelope[Post]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
