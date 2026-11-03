<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listPostComments -->

[English](list-post-comments.md) | [简体中文](../zh-CN/api-reference/list-post-comments.md)

# `list_post_comments`

Explicit Python method for public Device API operation `listPostComments`.

- HTTP: `POST /v1/accounts/{account_id}/posts/comments/list`
- Python method: `list_post_comments`
- Node operationId: `listPostComments`

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
- Python model: `ListPostCommentsRequestBody`
- Contract schema: `PostCommentListRequest`

## Success response

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
