<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: replyPostComment -->

[English](reply-post-comment.md) | [简体中文](../zh-CN/api-reference/reply-post-comment.md)

# `reply_post_comment`

Explicit Python method for public Device API operation `replyPostComment`.

- HTTP: `POST /v1/accounts/{account_id}/posts/comments/reply`
- Python method: `reply_post_comment`
- Node operationId: `replyPostComment`

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
- Python model: `ReplyPostCommentRequestBody`
- Contract schema: `PostCommentReplyRequest`

## Success response

- Python model: `ReplyPostCommentResponse`
- Contract schema: `ResponseEnvelope[PostCommentReplyResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `false` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `write` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
