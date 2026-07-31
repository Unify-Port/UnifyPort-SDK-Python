# Contract maintenance

[English](contract-maintenance.md) | [简体中文](zh-CN/contract-maintenance.md)

## Baseline

The initial Python contract is byte-for-byte identical to the public contract shipped by
`@unifyport/sdk-node` `v0.4.0`, with SHA-256
`30e3bd1a0c0fd1f0df244a89786a2b19e2acd4cad377f3742805acd5d1b946ba`.

Do not replace it directly with an internal service OpenAPI file. The public contract intentionally
removes internal-only provider values and descriptions.

## Update workflow

1. Select an approved, published public Node SDK tag and record its tag, immutable commit, digest, and
   surface counts in `parity/source.json`.
2. Replace `contracts/device.openapi.yaml` with that tag's public contract.
3. Review every changed operation for mutability, retry safety, secret input/output, and header policy.
4. Update `policy/operation-policies.json`; choose the restrictive default when evidence is incomplete.
5. Run `python scripts/generate.py` and review the manifest, models, methods, and both API references.
6. Add focused runtime and contract regression tests.
7. Run all validation gates, including parity and public artifact inspection.

Required checks:

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

Generated files must never be patched directly. Fix the contract, policy, or generator and regenerate.
Real-provider E2E validation remains a separate release requirement; local contract and transport tests
do not prove provider availability or deployed API behavior.
