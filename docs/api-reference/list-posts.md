<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listPosts -->

[English](list-posts.md) | [简体中文](../zh-CN/api-reference/list-posts.md)

# `list_posts`

Explicit Python method for public Device API operation `listPosts`.

- HTTP: `GET /v1/accounts/{account_id}/posts`
- Python method: `list_posts`
- Node operationId: `listPosts`

## Parameters

### Path parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `account_id` | `account_id` | yes | `str` |

### Query parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `cursor` | `cursor` | no | `str` |
| `limit` | `limit` | no | `int` |

### Header parameters

| Wire name | Python | Required | Type |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | no | `str` |

Authentication headers are not operation inputs; `X-Api-Key` comes only from client configuration.

### Request body

- Required: `no`
- Python model: `ListPostsRequestBody`
- Contract schema: `None`

## Success response

- Python model: `ListPostsResponse`
- Contract schema: `ResponseEnvelope[PostListResult]`

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
