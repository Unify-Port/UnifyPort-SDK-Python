# API coverage

[English](../api-coverage.md) | [简体中文](api-coverage.md)

| Surface | 数量 | 状态 |
| --- | ---: | --- |
| OpenAPI paths | 69 | 已批准的公开源码快照 |
| OpenAPI operations | 78 | 78 个同步 + 78 个异步 generated method |
| Component schemas | 218 | 生成 Python model/type name |
| Tags | 13 | 保留在 operation metadata 中 |
| Retryable operations | 19 | 精确 allowlist |
| Destructive operations | 8 | 精确评审分类 |
| Secret-input operations | 9 | 不会隐式获得 retry/MCP 权限 |
| Secret-output operations | 16 | 已记录 redaction 边界 |
| Node MCP-eligible operations | 4 | 只用于 parity 记录 |
| Python MCP-exposed operations | 0 | MCP 不在 package scope 内 |

generated [Device API reference](api-reference/README.md) 是逐 operation 的权威索引。
`parity/manifest.gen.json` 包含全部 camelCase OpenAPI operation ID 到 public snake_case Python method
的 machine-readable mapping，以及全部 component schema 到 Python model name 的映射。

此处 coverage 指 contract、generated surface 和测试覆盖，不代表已对每个 provider 发起 live request。
deployment 与真实 provider E2E 属于独立 release evidence。
