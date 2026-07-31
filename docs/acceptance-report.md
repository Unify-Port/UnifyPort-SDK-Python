# Acceptance report

[English](acceptance-report.md) | [简体中文](zh-CN/acceptance-report.md)

This report records the local acceptance evidence for the `0.1.0` release candidate on 2026-07-31.
It distinguishes source/contract verification from registry publication and real-provider E2E.

## Frozen baseline

| Item | Accepted value |
| --- | --- |
| Node SDK tag | `v0.4.0` |
| Node SDK commit | `03d9b371b9fecfb8dae0d9e1182de69874267286` |
| OpenAPI SHA-256 | `30e3bd1a0c0fd1f0df244a89786a2b19e2acd4cad377f3742805acd5d1b946ba` |
| OpenAPI coverage | 55 paths, 64 operations, 70 component schemas, 11 tags |
| Generated Python surface | 64 sync methods and 64 async methods |
| Policy parity | 19 retryable, 7 destructive, 8 secret-input, 12 secret-output |
| MCP surface | 4 Node-eligible operations recorded; 0 Python operations exposed |

## Local gates

The gates below passed with Python `3.12.13` on macOS. GitHub Actions separately defines the supported
Python `3.11`, `3.12`, and `3.13` compatibility matrix.

| Gate | Result |
| --- | --- |
| `python scripts/generate.py --check` | Generated artifacts are current |
| `python scripts/check_node_parity.py --node-repo ../unifyport-sdk-node --node-ref v0.4.0` | 64 operations, 70 schemas, and contract hash match |
| `python scripts/check_docs.py` | Local links and bilingual API references are valid |
| `python scripts/check_public.py` | Source public-boundary scan passed |
| `ruff format --check .` and `ruff check .` | 174 files formatted; lint passed |
| `mypy --strict src scripts typing_tests` | 23 source files passed |
| `npx --yes pyright@1.1.411 pyright_tests` | PEP 728 open `ProviderProfile` typing passed |
| `pytest` | 53 tests passed; 87.92% branch-aware coverage |
| `python -m build` | Built `unifyport_sdk-0.1.0.tar.gz` and universal wheel |
| `twine check dist/*` | Both distributions passed metadata/render checks |
| `python scripts/check_public.py dist/*` | Source and archive scan passed |
| `pip-audit` | No known vulnerabilities after updating the audit environment's installer |
| Clean-wheel smoke | Fresh venv passed sync/async `httpx.MockTransport` calls and public introspection |

The contract tests also verify runtime `TypedDict` required/optional metadata for `reply_token`, PEP 728
extra-item metadata for the open `provider_profile` boundary, and the exact `ProviderName` values.

## Release boundaries

- The candidate has not been published to PyPI and no release tag is implied by this report.
- The local mock-transport suite does not claim deployed Device API health or real-provider E2E.
- GitHub-hosted CI results, package publication, and provider/account validation remain separate release
  evidence.
