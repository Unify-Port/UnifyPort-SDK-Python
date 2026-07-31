<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->
<!-- operationId: getContact -->

[English](../../api-reference/get-contact.md) | [简体中文](get-contact.md)

# `get_contact`

公开 Device API operation `getContact` 的 Python 显式方法。

- HTTP: `GET /v1/accounts/{account_id}/contacts/info`
- Python 方法: `get_contact`
- Node operationId: `getContact`

## 参数

### Path 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `account_id` | `account_id` | 是 | `str` |

### Query 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `contact_id` | `contact_id` | 是 | `str` |

### Header 参数

| Wire 名称 | Python | 必填 | 类型 |
| --- | --- | --- | --- |
| `X-Request-Id` | `x_request_id` | 否 | `str` |

认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。

### Request body

- 必填: `否`
- Python model: `GetContactRequestBody`
- Contract schema: `None`

## 成功响应

- Python model: `GetContactResponse`
- Contract schema: `ResponseEnvelope[Contact]`

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
