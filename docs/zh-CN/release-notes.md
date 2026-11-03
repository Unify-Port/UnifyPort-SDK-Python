# Release notes

[English](../release-notes.md) | [简体中文](release-notes.md)

## 未发布 - Facebook

新增 facebook 渠道、四个标准回调接收类型，覆盖稀疏媒体和 session 授权。HTTP 方法、事件名及重试策略保持不变；穷举渠道的代码需处理新增值。详见 Facebook 渠道说明；不表示已发布或部署。

## 未发布

同步 78 个 HTTP 接口、218 个 schema、数字错误码及 Webhook 类型。版本未变更；详见[本次契约更新](contract-update.md)。

## 0.1.0

公开 UnifyPort Device API 的首个 Python SDK 实现：

- 基于 HTTPX 的同步与异步 client，生成 64 个 snake_case operation method。
- 基于 Node SDK `v0.4.0` 公开 contract 生成 70 个 schema type。
- 支持 typed/open `ProviderProfile` 标准字段和 optional `SendMessageResult.reply_token`。
- 提供确定性生成、Node parity manifest、双语 operation reference 与 public artifact gate。
- 提供 HTTPS/base-path confinement、credential isolation、allowlisted retry、total deadline、有限 response
  streaming、sanitized error 与有限 cursor pagination。

Python version 与 Node SDK version 相互独立。registry publish 和真实 provider E2E 是单独 release 动作，
本说明不声称已完成这两项。
