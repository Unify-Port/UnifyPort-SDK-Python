# API coverage

[English](../api-coverage.md) | [简体中文](api-coverage.md)

| Surface | 数量 | 状态 |
| --- | ---: | --- |
| OpenAPI paths | 55 | 冻结自 Node `v0.4.0` |
| OpenAPI operations | 64 | 64 个同步 + 64 个异步 generated method |
| Component schemas | 70 | 生成 Python model/type name |
| Tags | 11 | 保留在 operation metadata 中 |
| Retryable operations | 19 | 精确 allowlist |
| Destructive operations | 7 | 精确评审分类 |
| Secret-input operations | 8 | 不会隐式获得 retry/MCP 权限 |
| Secret-output operations | 12 | 已记录 redaction 边界 |
| Node MCP-eligible operations | 4 | 只用于 parity 记录 |
| Python MCP-exposed operations | 0 | MCP 不在 package scope 内 |

generated [Device API reference](api-reference/README.md) 是逐 operation 的权威索引。
`parity/manifest.gen.json` 包含全部 camelCase OpenAPI operation ID 到 public snake_case Python method
的 machine-readable mapping，以及全部 component schema 到 Python model name 的映射。

此处 coverage 指 contract、generated surface 和测试覆盖，不代表已对每个 provider 发起 live request。
deployment 与真实 provider E2E 属于独立 release evidence。
