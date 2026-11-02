#!/usr/bin/env python3
"""Verify the pinned contract and operation policy against the approved Node SDK source."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "parity/source.json"
MANIFEST_PATH = ROOT / "parity/manifest.gen.json"
CONTRACT_PATH = ROOT / "contracts/device.openapi.yaml"
NODE_CONTRACT_PATH = "contracts/device.openapi.yaml"
NODE_CATALOG_PATH = "packages/sdk/src/generated/device/operation-catalog.ts"
NODE_PACKAGE_PATH = "packages/sdk/package.json"

JsonObject = dict[str, Any]
POLICY_PATTERN = re.compile(
    r'"operationId":\s*"([^"]+)".*?'
    r'"mutability":\s*"(read|write|destructive)".*?'
    r'"retryable":\s*(true|false).*?'
    r'"secretInput":\s*(true|false).*?'
    r'"secretOutput":\s*(true|false).*?'
    r'"mcpExposure":\s*"(read|write|destructive|never)"',
    re.DOTALL,
)


def _object(value: Any, description: str) -> JsonObject:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise ValueError(f"{description} must be an object")
    return cast(JsonObject, value)


def _load_json(path: Path) -> JsonObject:
    return _object(json.loads(path.read_text(encoding="utf-8")), str(path))


def _git_bytes(repository: Path, *arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        # Git stderr 可能包含本机路径，公开检查只返回稳定命令边界。
        raise RuntimeError(f"git command failed: {arguments[0]}")
    return result.stdout


def _git_text(repository: Path, *arguments: str) -> str:
    return _git_bytes(repository, *arguments).decode("utf-8").strip()


def _node_policies(catalog: str) -> dict[str, JsonObject]:
    policies: dict[str, JsonObject] = {}
    for match in POLICY_PATTERN.finditer(catalog):
        operation_id = match.group(1)
        if operation_id in policies:
            raise ValueError(f"duplicate Node catalog operation: {operation_id}")
        policies[operation_id] = {
            "mutability": match.group(2),
            "retryable": match.group(3) == "true",
            "secretInput": match.group(4) == "true",
            "secretOutput": match.group(5) == "true",
            "nodeMcpExposure": match.group(6),
        }
    return policies


def check_node_parity(node_repository: Path, node_ref: str) -> None:
    source = _load_json(SOURCE_PATH)
    manifest = _load_json(MANIFEST_PATH)
    source_node = _object(source.get("nodeSdk"), "source.nodeSdk")
    source_contract = _object(source.get("contract"), "source.contract")
    operations = _object(manifest.get("operations"), "manifest.operations")
    if not node_repository.is_dir():
        raise ValueError("Node SDK repository directory is missing")

    expected_ref = (
        source_node.get("ref")
        if source_node.get("baselineKind") == "approved-source"
        else source_node.get("tag")
    )
    # 批准源码与已发布 tag 分开固定，不能因工作分支变化而扩大基线。
    if node_ref != expected_ref:
        raise ValueError(f"node ref must match pinned source ref {expected_ref}")
    peeled_commit = _git_text(node_repository, "rev-parse", f"{node_ref}^{{commit}}")
    if peeled_commit != source_node.get("commit"):
        raise ValueError("Node ref target differs from parity/source.json")

    node_contract = _git_bytes(
        node_repository,
        "show",
        f"{node_ref}:{NODE_CONTRACT_PATH}",
    )
    local_contract = CONTRACT_PATH.read_bytes()
    local_sha = hashlib.sha256(local_contract).hexdigest()
    node_sha = hashlib.sha256(node_contract).hexdigest()
    expected_sha = source_contract.get("sha256")
    if local_sha != expected_sha or node_sha != expected_sha or node_contract != local_contract:
        raise ValueError("Node and Python contract bytes differ from the pinned baseline")
    if manifest.get("contractSha256") != expected_sha:
        raise ValueError("generated parity manifest has a different contract digest")

    node_package = _object(
        json.loads(
            _git_bytes(
                node_repository,
                "show",
                f"{node_ref}:{NODE_PACKAGE_PATH}",
            )
        ),
        "Node SDK package.json",
    )
    if node_package.get("name") != source_node.get("package"):
        raise ValueError("Node package name differs from parity/source.json")
    if node_package.get("version") != source_node.get("version"):
        raise ValueError("Node package version differs from parity/source.json")

    catalog = _git_bytes(
        node_repository,
        "show",
        f"{node_ref}:{NODE_CATALOG_PATH}",
    ).decode("utf-8")
    node_policies = _node_policies(catalog)
    if set(node_policies) != set(operations):
        raise ValueError("Node and Python operation sets differ")
    for operation_id, raw_operation in operations.items():
        operation = _object(raw_operation, f"manifest operation {operation_id}")
        node_policy = node_policies[operation_id]
        for field in (
            "mutability",
            "retryable",
            "secretInput",
            "secretOutput",
            "nodeMcpExposure",
        ):
            if operation.get(field) != node_policy.get(field):
                raise ValueError(f"Node/Python policy differs: {operation_id}.{field}")
        if operation.get("pythonMcpExposure") != "never":
            raise ValueError(f"Python MCP exposure is not disabled: {operation_id}")

    expected_operations = source_contract.get("operationCount")
    expected_schemas = source_contract.get("schemaCount")
    if (
        manifest.get("operationCount") != expected_operations
        or len(operations) != expected_operations
    ):
        raise ValueError("operation coverage count differs from pinned source")
    if manifest.get("schemaCount") != expected_schemas:
        raise ValueError("schema coverage count differs from pinned source")


def main() -> int:
    source = _load_json(SOURCE_PATH)
    source_node = _object(source.get("nodeSdk"), "source.nodeSdk")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--node-repo",
        type=Path,
        default=ROOT.parent / "UnifyPort-SDK-Nodejs",
    )
    parser.add_argument(
        "--node-ref",
        default=cast(str, source_node.get("ref") or source_node.get("tag")),
    )
    arguments = parser.parse_args()
    try:
        check_node_parity(arguments.node_repo.resolve(), arguments.node_ref)
    except (OSError, UnicodeError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"[parity:check] {error}", file=sys.stderr)
        return 1
    manifest = _load_json(MANIFEST_PATH)
    print(
        "[parity:check] "
        f"{manifest['operationCount']} operations, {manifest['schemaCount']} schemas, "
        f"and contract {str(manifest['contractSha256'])[:12]} match Node source "
        f"{str(source_node['commit'])[:7]} ({source_node.get('baselineKind', 'release-tag')})",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
