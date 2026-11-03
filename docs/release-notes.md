# Release notes

[English](release-notes.md) | [简体中文](zh-CN/release-notes.md)


## 0.2.0 — prepared, unreleased

Prepared on 2026-11-03; this is not a publication date. This pre-1.0 minor version includes breaking response/type changes from `0.1.0`. Read the [migration guide](migration.md) before upgrading.

### Changes

- Synchronizes 78 HTTP operations, 225 component schemas, 24 standard event names plus `*`, and 40 specialized Webhook receiver declarations. The 57 synthetic examples cover 29 receiver declarations, not all 40.
- Adds account-operation queries, hosted authorization/Passkey, contacts/membership, on-demand history, posts/comments and gated calls. Account pagination, creation/update inputs, asynchronous deletion, wallet/QR metadata and message/Webhook unions are updated.
- Adds the `facebook` provider and four receiver declarations with eight examples; Facebook itself adds no HTTP operations or standard event names. Session-only authorization and E2EE direct-message limits are documented in [Facebook](facebook.md).
- Keeps authentication, credential filtering and the 19-operation retry allowlist. Adds optional validated five-digit `numeric_code` error metadata without exposing server bodies. No new automatic write retries or MCP exposure are enabled.

The Python generator preserves quoted and unquoted nanosecond timestamps without changing SafeLoader globally; regression coverage includes UTC, offsets and trailing zeros.

### Version and provenance

`src/unifyport/__init__.py` declares `0.2.0`; Hatch reads that single version source for wheel/sdist metadata. The independent installed-wheel smoke expectation is also `0.2.0`.

The approved public contract comes from [Node source ce60499](https://github.com/Unify-Port/UnifyPort-SDK-Nodejs/commit/ce60499d7169c860ed3f64a686e04bff44316f35). Its package metadata was `0.4.0` with baseline kind `approved-source`; that immutable provenance remains unchanged and does not claim npm `0.5.0` has been published. Contract SHA-256: `8190a34dc8ed60476f79e00b37d9dea418082886724ee6d64efa389f440adffc`.

Supported runtime: Python >=3.11; sync and async HTTPX clients.

### Verification and remaining gates

Run from the source checkout:

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

Review the exact candidate diff and package/archive contents; install the local artifact into a clean consumer and confirm its version and public imports. Run `scripts/smoke_installed.py` with the clean environment's interpreter and `-I` after installing only the new wheel. These are preparation gates, not a statement that the listed commands or release CI have already passed.

No tag, registry publication, GitHub Release, deployment or real-account E2E is performed by this preparation. CI must pass on the final reviewed release commit. Controlled staging/provider E2E and post-publication registry/module resolution remain separate gates. Re-run time-sensitive vulnerability checks before release. Rollback constraints are documented in the [migration guide](migration.md).

Pushing a `v*` tag starts the PyPI release workflow, including the `pypi` environment gate. A tag push is a publishing action and requires separate authorization.

## 0.1.0

Initial Python SDK implementation for the public UnifyPort Device API:

- Sync and async HTTPX clients with 64 generated snake_case operation methods.
- 70 generated schema types based on the Node SDK `v0.4.0` public contract.
- Typed, open `ProviderProfile` standard fields and optional `SendMessageResult.reply_token` support.
- Deterministic generation, Node parity manifest, bilingual operation reference, and public artifact gate.
- HTTPS/base-path confinement, credential isolation, allowlisted retries, total deadlines, bounded response
  streaming, sanitized errors, and finite cursor pagination.

The Python version is independent from the Node SDK version. Registry publication and real-provider E2E
are separate release actions and are not asserted by these notes.
