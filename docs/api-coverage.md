# API coverage

[English](api-coverage.md) | [简体中文](zh-CN/api-coverage.md)

| Surface | Count | Status |
| --- | ---: | --- |
| OpenAPI paths | 69 | Approved source snapshot |
| OpenAPI operations | 78 | 78 sync + 78 async generated methods |
| Component schemas | 218 | Generated Python model/type names |
| Tags | 13 | Preserved in operation metadata |
| Retryable operations | 19 | Exact allowlist |
| Destructive operations | 8 | Exact reviewed classification |
| Secret-input operations | 9 | Never granted implicit retry/MCP access |
| Secret-output operations | 16 | Redaction boundary documented |
| Node MCP-eligible operations | 4 | Recorded only for parity |
| Python MCP-exposed operations | 0 | MCP is outside package scope |

The generated [Device API reference](api-reference/README.md) is the authoritative per-operation index.
`parity/manifest.gen.json` contains the machine-readable mapping from all camelCase OpenAPI operation IDs
to public snake_case Python methods and all component schema names to Python model names.

Coverage here means contract, generated surface, and test coverage. It does not claim a live request was
made to every provider. Deployment and real-provider E2E are separate release evidence.
