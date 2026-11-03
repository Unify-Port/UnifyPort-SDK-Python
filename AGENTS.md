# AGENTS.md

本文件适用于整个仓库，约束自动化 agent 与维护者的协作方式。

## 语言与注释

- 默认使用简体中文协作；代码标识符、命令、配置键、协议字段和错误码保持英文。
- 英文是公开文档的默认入口；修改用户文档时同步更新完整的简体中文版本。
- 代码注释只用简短中文解释 why：边界、兼容性、外部限制或风险，不逐行翻译实现。

## 范围与来源

- 本仓库只覆盖公开的 UnifyPort Device API。
- `contracts/device.openapi.yaml` 是唯一协议生成输入；不得根据未公开实现推断字段或行为。
- `policy/operation-policies.json` 记录不能从 HTTP method 推导的重试、破坏性和 secret 分类。
- 不要手改 `src/unifyport/_generated/`；修改 contract、policy 或生成器后运行生成命令。
- 不提供 generic `raw_request`、MCP、Agent Skills 或 provider-specific orchestration。

## 安全不变量

- `X-Api-Key` 只能来自 client config，operation input 不得覆盖它。
- 默认只允许 HTTPS；显式 opt-in 的明文 HTTP 也仅限 loopback。
- 自动重试只适用于 policy allowlist；单次调用只能收紧全局 timeout 和 retry budget。
- redirect、跨 origin、base path 逃逸、无限分页和无上限响应体必须拒绝。
- 公开错误和 `ApiResult` 不得携带 raw HTTP response、credential、query、响应正文或底层异常文本。
- `provider_profile` 与 `reply_token` 按敏感输出处理；fixture、日志和文档不得包含真实 secret。

## 修改流程

1. 先检查 worktree、真实文件和既有测试，保留用户及其他 agent 的改动。
2. API 变化按 contract → policy → generated code → runtime/tests/docs 的顺序处理。
3. 新 operation 必须显式分类 auth、mutability、retry、secret input/output 与 parity。
4. 保持最小改动，不做无关重构或依赖升级。
5. 交付前运行并如实报告生成、格式、lint、type、test、build、artifact、audit 和 clean-install 门禁。

## 常用验收

```bash
python scripts/generate.py --check
python scripts/check_node_parity.py --node-repo ../UnifyPort-SDK-Nodejs --node-ref ce60499d7169c860ed3f64a686e04bff44316f35
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
```
