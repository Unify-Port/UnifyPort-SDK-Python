# API coverage

[English](api-coverage.md) | [简体中文](zh-CN/api-coverage.md)

| Surface | Count | Status |
| --- | ---: | --- |
| OpenAPI paths | 55 | Frozen from Node `v0.4.0` |
| OpenAPI operations | 64 | 64 sync + 64 async generated methods |
| Component schemas | 70 | Generated Python model/type names |
| Tags | 11 | Preserved in operation metadata |
| Retryable operations | 19 | Exact allowlist |
| Destructive operations | 7 | Exact reviewed classification |
| Secret-input operations | 8 | Never granted implicit retry/MCP access |
| Secret-output operations | 12 | Redaction boundary documented |
| Node MCP-eligible operations | 4 | Recorded only for parity |
| Python MCP-exposed operations | 0 | MCP is outside package scope |

The generated [Device API reference](api-reference/README.md) is the authoritative per-operation index.
`parity/manifest.gen.json` contains the machine-readable mapping from all camelCase OpenAPI operation IDs
to public snake_case Python methods and all component schema names to Python model names.

Coverage here means contract, generated surface, and test coverage. It does not claim a live request was
made to every provider. Deployment and real-provider E2E are separate release evidence.
