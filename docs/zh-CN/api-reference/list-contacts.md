<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: listContacts -->

[English](../../api-reference/list-contacts.md) | [简体中文](list-contacts.md)

# `list_contacts`

公开 Device API operation `listContacts` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/contacts`
- Python 方法: `list_contacts`
- Node operationId: `listContacts`

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
| `q` | `q` | 否 | `str` |
| `updated_since` | `updated_since` | 否 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `ListContactsRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `ListContactsResponse`
- Contract schema: `ResponseEnvelope[ContactListResult]`

## Policy

| Flag | Value |
| --- | --- |
| `retryable` | `true` |
| `destructive` | `false` |
| `secretInput` | `false` |
| `secretOutput` | `false` |
| `Node MCP eligible` | `false` |
| `Python MCP exposed` | `false` |
| `mutability` | `read` |
| `nodeMcpExposure` | `never` |
| `pythonMcpExposure` | `never` |
