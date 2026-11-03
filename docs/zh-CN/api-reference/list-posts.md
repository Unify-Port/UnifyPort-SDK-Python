<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listPosts -->

[English](../../api-reference/list-posts.md) | [简体中文](list-posts.md)

# `list_posts`

公开 Device API operation `listPosts` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/posts`
- Python 方法: `list_posts`
- Node operationId: `listPosts`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `cursor` | `cursor` | 否 | `str` |
| `limit` | `limit` | 否 | `int` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListPostsRequestBody`
- Contract schema: `None`

## 成功响应

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
