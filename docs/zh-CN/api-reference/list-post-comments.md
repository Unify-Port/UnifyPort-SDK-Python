<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listPostComments -->

[English](../../api-reference/list-post-comments.md) | [简体中文](list-post-comments.md)

# `list_post_comments`

公开 Device API operation `listPostComments` 的 Python 显式方法。

- HTTP: `POST /v1/accounts/{account_id}/posts/comments/list`
- Python 方法: `list_post_comments`
- Node operationId: `listPostComments`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

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
- Python model: `ListPostCommentsRequestBody`
- Contract schema: `PostCommentListRequest`

## 成功响应

- Python model: `ListPostCommentsResponse`
- Contract schema: `ResponseEnvelope[PostCommentListResult]`

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
