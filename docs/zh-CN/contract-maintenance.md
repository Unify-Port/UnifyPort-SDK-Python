# Contract 维护

[English](../contract-maintenance.md) | [简体中文](contract-maintenance.md)

## Baseline

初始 Python contract 与 `@unifyport/sdk-node` `v0.4.0` 发布的公开 contract 逐 byte 相同，SHA-256 为
`30e3bd1a0c0fd1f0df244a89786a2b19e2acd4cad377f3742805acd5d1b946ba`。

不要直接用内部 service OpenAPI 文件替换它；公开 contract 会有意移除 internal-only provider value 和
description。

## 更新流程

1. 选择已批准、已发布的公开 Node SDK tag，在 `parity/source.json` 中记录 tag、immutable commit、
   digest 与 surface 数量。
2. 用该 tag 的公开 contract 替换 `contracts/device.openapi.yaml`。
3. 对每个变化 operation 复核 mutability、retry safety、secret input/output 和 header policy。
4. 更新 `policy/operation-policies.json`；证据不足时使用更严格的默认值。
5. 运行 `python scripts/generate.py`，复核 manifest、models、methods 和两份 API reference。
6. 增加针对性的 runtime 与 contract regression test。
7. 运行全部验收，包括 parity 和 public artifact 检查。

必须执行：

```bash
python scripts/generate.py --check
python scripts/check_node_parity.py --node-repo ../unifyport-sdk-node --node-ref <tag>
ruff format --check .
ruff check .
mypy --strict src scripts typing_tests
pytest
python -m build
twine check dist/*
python scripts/check_public.py dist/*
pip-audit
```

不得直接 patch generated 文件；应修正 contract、policy 或 generator 后重新生成。真实 provider E2E 是
独立 release requirement；本地 contract/transport test 不能证明 provider 可用性或 deployed API 行为。
