# 安全边界

[English](../security.md) | [简体中文](security.md)

## Credential

- Device API 使用 `X-Api-Key`，它只能在构造 client 时提供。
- string 或 credential provider 在每个 logical operation 中只解析一次；retry 复用该值，且 public
  result/error 不保存它。
- operation header 使用独立 allowlist；generated method 不能注入 `Authorization`、`Cookie` 或
  `X-Api-Key`。
- config 的 repr 会同时隐藏 API key 与 base URL。

## Request 边界

- 默认必须使用 HTTPS；只有 `allow_insecure_http=True` 且 host 为 loopback 时才允许 HTTP。
- 拒绝包含 user info、query 或 fragment 的 base URL。
- 最终 request 必须与配置保持同 origin，并位于配置的 base path 之下。
- 禁止跟随 redirect；redirect response 会作为非成功 API response 处理。
- `transport=` 是仅供测试或受控集成使用的可信 dependency-injection point。它会收到包括
  `X-Api-Key` 在内的完整 request，也能自行执行 I/O。origin、base-path、proxy 和 redirect 防护约束的是
  SDK 生成的 request，无法约束 custom transport 内的任意代码；不得接受不可信来源提供的 transport。

## Retry 与 timeout

只有 policy allowlist 中的 19 个 operation 可以 retry。候选条件为网络失败和 HTTP `408`、`429`、
`502`、`503`、`504`。backoff 使用 full jitter；合法 `Retry-After` 也不能超过配置的 delay cap。单次
operation 可以关闭或减少 retry，但不能给其他 operation 增加 retry 能力。

配置的 timeout 是完整 logical deadline，覆盖 credential resolve、所有 attempt、response streaming 和
backoff。单次 timeout 只能缩短这个 deadline。可协作取消的 HTTP 工作和 async credential provider 会在
deadline 到达时取消；Python 无法安全抢占任意阻塞的 sync credential callback 或 custom transport。如果它们
在 deadline 后才返回，SDK 会报告 timeout，且不会再用过期 credential 发起后续请求。外部 async task 取消
继续使用原生 `asyncio.CancelledError` 控制流。

## Response 与错误

- request 固定使用 `Accept-Encoding: identity`；任何非 identity `Content-Encoding` response 都会在
  body 读取前被拒绝，防止 HTTP client 在 byte budget 检查前透明解压并膨胀单个 chunk。
- response body 默认 streaming limit 为 8 MiB，配置上限为 64 MiB。
- 无效或超限内容抛出 `UnifyPortResponseParseError`，且不保留正文。
- API error 只公开已校验的 `status`、有限长度 diagnostic `code` 和有限长度 request ID。
- transport exception text、raw response、headers、body、带 query 的 URL 和服务端 message/details 都不会
  进入 public error。
- `ApiResult` 只携带 `data`、`status` 和可选 `request_id`，不含 raw response handle。

## 敏感 contract 字段

12 个 `secretOutput` operation 都必须按敏感数据处理。特别是 account response 可能含
`provider_profile`，`send_message` 可能含 optional opaque `reply_token`。8 个 `secretInput` operation
覆盖 credential、session、endpoint secret 和可复用 reply capability。不要完整记录、snapshot 或转发这些
operation 的输入输出。

## 明确不提供的能力

本 package 不提供 MCP exposure、通用 raw request、provider-specific orchestration、推测的 webhook
签名逻辑、analytics identifier propagation 或 credential logging hook。相关新增必须经过独立的公开 contract
与安全评审。
