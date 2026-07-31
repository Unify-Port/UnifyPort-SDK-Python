# 验收报告

[English](../acceptance-report.md) | [简体中文](acceptance-report.md)

本报告记录 `0.1.0` release candidate 在 2026-07-31 的本地验收证据，并区分 source/contract 验证、
registry 发布和真实 provider E2E。

## 冻结基线

| 项目 | 验收值 |
| --- | --- |
| Node SDK tag | `v0.4.0` |
| Node SDK commit | `03d9b371b9fecfb8dae0d9e1182de69874267286` |
| OpenAPI SHA-256 | `30e3bd1a0c0fd1f0df244a89786a2b19e2acd4cad377f3742805acd5d1b946ba` |
| OpenAPI 覆盖 | 55 paths、64 operations、70 component schemas、11 tags |
| 生成的 Python surface | 64 个 sync method 与 64 个 async method |
| Policy parity | 19 retryable、7 destructive、8 secret-input、12 secret-output |
| MCP surface | 记录 4 个 Node-eligible operation；Python 暴露 0 个 operation |

## 本地门禁

以下门禁已在 macOS、Python `3.12.13` 通过；GitHub Actions 另行定义 Python `3.11`、`3.12`、
`3.13` 的兼容矩阵。

| 门禁 | 结果 |
| --- | --- |
| `python scripts/generate.py --check` | generated artifact 为最新状态 |
| `python scripts/check_node_parity.py --node-repo ../unifyport-sdk-node --node-ref v0.4.0` | 64 operations、70 schemas 与 contract hash 一致 |
| `python scripts/check_docs.py` | 本地链接与双语 API reference 完整 |
| `python scripts/check_public.py` | source 公开边界扫描通过 |
| `ruff format --check .` 与 `ruff check .` | 174 个文件格式正确，lint 通过 |
| `mypy --strict src scripts typing_tests` | 23 个 source file 通过 |
| `npx --yes pyright@1.1.411 pyright_tests` | PEP 728 open `ProviderProfile` 类型通过 |
| `pytest` | 53 个测试通过；branch-aware coverage 87.92% |
| `python -m build` | 生成 `unifyport_sdk-0.1.0.tar.gz` 与 universal wheel |
| `twine check dist/*` | 两个 distribution 均通过 metadata/render 检查 |
| `python scripts/check_public.py dist/*` | source 与 archive 扫描通过 |
| `pip-audit` | 更新审计环境 installer 后未发现已知漏洞 |
| clean-wheel smoke | 全新 venv 的 sync/async `httpx.MockTransport` 调用及 public introspection 通过 |

contract 测试还验证了 `reply_token` 的 runtime `TypedDict` required/optional metadata、开放
`provider_profile` 边界的 PEP 728 extra-item metadata，以及精确的 `ProviderName` value。

## Release 边界

- 本 candidate 尚未发布到 PyPI；本报告也不代表已创建 release tag。
- 本地 mock-transport 测试不代表 deployed Device API 健康，也不代表真实 provider E2E 已完成。
- GitHub-hosted CI、package 发布和 provider/account 验证仍是相互独立的 release evidence。
