# Release notes

[English](../release-notes.md) | [简体中文](release-notes.md)


## 0.2.0 — 已准备，未发布

准备日期为 2026-11-03，不是发布日期。此 1.0 之前的 minor 版本包含相对 `0.1.0` 的响应/类型不兼容变化，升级前请阅读[迁移指南](migration.md)。

### 变化

- 同步 78 个 HTTP operation、225 个 component schema、24 个标准事件名及 `*`，提供 40 个专用 Webhook 接收方声明。57 个合成示例覆盖其中 29 个声明，不表示覆盖全部 40 个。
- 新增账号操作查询、托管授权/Passkey、联系人/关系、按需历史、帖子/评论及受内测权限限制的通话。更新账号分页、创建/更新输入、异步删除、余额/QR 元数据和消息/Webhook 联合类型。
- 新增 `facebook` provider、四个接收方声明和八个示例；Facebook 本身不新增 HTTP operation 或标准事件名。仅支持 session 授权及 E2EE 私聊的限制见 [Facebook](facebook.md)。
- 保持认证、凭证过滤和 19 个操作的重试白名单；增加经过验证的五位字符串错误字段 `numeric_code`，不暴露服务端正文。不启用新的自动写入重试或 MCP 能力。

Python 生成器完整保留带引号及不带引号的纳秒时间，不全局修改 SafeLoader；回归覆盖 UTC、时区偏移与尾部零。

### 版本与来源

`src/unifyport/__init__.py` 声明 `0.2.0`，Hatch 读取这一版本源生成 wheel/sdist metadata；独立的已安装 wheel smoke 预期版本同步为 `0.2.0`。

契约来自已批准的公开 [Node 源码 ce60499](https://github.com/Unify-Port/UnifyPort-SDK-Nodejs/commit/ce60499d7169c860ed3f64a686e04bff44316f35)。该不可变基线的 package metadata 为 `0.4.0`，类型为 `approved-source`；保留这一来源，不宣称 npm `0.5.0` 已发布。契约 SHA-256 为 `8190a34dc8ed60476f79e00b37d9dea418082886724ee6d64efa389f440adffc`。

支持环境：Python >=3.11，支持 HTTPX 同步与异步 client。

### 验证与剩余门禁

在源码目录运行：

```bash
python scripts/generate.py --check
python scripts/check_node_parity.py
python scripts/check_docs.py
ruff format --check .
ruff check .
mypy --strict src scripts typing_tests
npx --yes pyright@1.1.411 pyright_tests
pytest
python -m build
twine check dist/*
python scripts/check_public.py dist/*
python scripts/smoke_installed.py
pip-audit
git diff --check
```

审查精确 candidate diff 及包/归档内容，在干净 consumer 中安装本地产物并确认版本和公开 import。只安装新 wheel 后，使用干净环境的解释器加 `-I` 运行 `scripts/smoke_installed.py`。这些是准备门禁，不表示本说明中的命令或 release CI 已通过。

本次准备不执行 tag、registry 发布、GitHub Release、部署或真实账号 E2E。最终已审查 release commit 必须通过 CI；受控 staging/provider E2E 和发布后的 registry/module 解析仍是独立门禁。发布前重跑具有时效性的漏洞检查；回退限制见[迁移指南](migration.md)。

推送 `v*` tag 会启动 PyPI release workflow，并进入 `pypi` environment 门禁。推 tag 属于发布动作，需要单独授权。

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
