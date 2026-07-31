#!/usr/bin/env python3
"""Validate local Markdown links and bilingual generated API coverage."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, cast
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "parity/manifest.gen.json"
SOURCE_PATH = ROOT / "parity/source.json"
ENGLISH_REFERENCE_DIR = ROOT / "docs/api-reference"
CHINESE_REFERENCE_DIR = ROOT / "docs/zh-CN/api-reference"
FENCED_CODE_PATTERN = re.compile(r"```.*?```", re.DOTALL)
INLINE_LINK_PATTERN = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
REFERENCE_LINK_PATTERN = re.compile(r"^\s*\[[^\]]+]:\s*(\S+)", re.MULTILINE)
OPERATION_MARKER_PATTERN = re.compile(r"<!--\s*operationId:\s*([A-Za-z0-9]+)\s*-->")

JsonObject = dict[str, Any]


def _object(value: Any, description: str) -> JsonObject:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise ValueError(f"{description} must be an object")
    return cast(JsonObject, value)


def _markdown_files() -> list[Path]:
    roots = sorted(ROOT.glob("*.md"))
    roots.extend(sorted((ROOT / "docs").rglob("*.md")))
    return [path for path in roots if path.is_file()]


def _link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    # Markdown title 不属于 URL；当前检查只需解析第一个非空 token。
    return target.split(maxsplit=1)[0] if target else ""


def _check_local_links() -> list[str]:
    failures: list[str] = []
    for document in _markdown_files():
        text = FENCED_CODE_PATTERN.sub("", document.read_text(encoding="utf-8"))
        targets = INLINE_LINK_PATTERN.findall(text)
        targets.extend(REFERENCE_LINK_PATTERN.findall(text))
        for raw_target in targets:
            target = _link_target(raw_target)
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            resolved = (
                ROOT / path_part.lstrip("/")
                if path_part.startswith("/")
                else document.parent / path_part
            ).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                failures.append(
                    f"{document.relative_to(ROOT)}: local link escapes repository: {target}"
                )
                continue
            if not resolved.exists():
                failures.append(
                    f"{document.relative_to(ROOT)}: missing local link target: {target}"
                )
    return failures


def _reference_coverage(
    directory: Path,
    operations: JsonObject,
    expected_count: int,
) -> tuple[dict[str, str], list[str]]:
    failures: list[str] = []
    mapping: dict[str, str] = {}
    markers: Counter[str] = Counter()
    pages = sorted(path for path in directory.glob("*.md") if path.name != "README.md")
    for page in pages:
        text = page.read_text(encoding="utf-8")
        found = OPERATION_MARKER_PATTERN.findall(text)
        if len(found) != 1:
            failures.append(f"{page.relative_to(ROOT)}: expected exactly one operation marker")
            continue
        operation_id = found[0]
        markers[operation_id] += 1
        mapping[operation_id] = page.name
        raw_operation = operations.get(operation_id)
        if not isinstance(raw_operation, dict):
            failures.append(f"{page.relative_to(ROOT)}: unknown operationId {operation_id}")
            continue
        operation = _object(raw_operation, operation_id)
        expected_fragments = (
            f"`{operation['method']} {operation['path']}`",
            f"`{operation['pythonMethod']}`",
            f"`{operation['responseSchema']}`",
            "`X-Request-Id`",
            "`retryable`",
            "`secretInput`",
            "`secretOutput`",
            "`pythonMcpExposure`",
        )
        for fragment in expected_fragments:
            if fragment not in text:
                failures.append(f"{page.relative_to(ROOT)}: missing generated field {fragment}")
    expected = set(operations)
    actual = set(mapping)
    if len(pages) != expected_count:
        failures.append(
            f"{directory.relative_to(ROOT)}: expected {expected_count} operation pages, "
            f"got {len(pages)}"
        )
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    duplicates = sorted(operation_id for operation_id, count in markers.items() if count != 1)
    if missing:
        failures.append(f"{directory.relative_to(ROOT)}: missing operations {missing!r}")
    if extra:
        failures.append(f"{directory.relative_to(ROOT)}: extra operations {extra!r}")
    if duplicates:
        failures.append(f"{directory.relative_to(ROOT)}: duplicate operations {duplicates!r}")
    return mapping, failures


def check_docs() -> None:
    manifest = _object(
        json.loads(MANIFEST_PATH.read_text(encoding="utf-8")),
        "parity manifest",
    )
    source = _object(
        json.loads(SOURCE_PATH.read_text(encoding="utf-8")),
        "parity source",
    )
    source_contract = _object(source.get("contract"), "source.contract")
    operations = _object(manifest.get("operations"), "manifest.operations")
    expected_count = source_contract.get("operationCount")
    if not isinstance(expected_count, int) or isinstance(expected_count, bool):
        raise ValueError("source operationCount must be an integer")
    if manifest.get("operationCount") != expected_count or len(operations) != expected_count:
        raise ValueError("manifest operation coverage differs from source baseline")
    failures = _check_local_links()
    english, english_failures = _reference_coverage(
        ENGLISH_REFERENCE_DIR, operations, expected_count
    )
    chinese, chinese_failures = _reference_coverage(
        CHINESE_REFERENCE_DIR, operations, expected_count
    )
    failures.extend(english_failures)
    failures.extend(chinese_failures)
    if english != chinese:
        failures.append("English and Simplified Chinese API reference sets differ")
    if failures:
        raise ValueError("\n".join(failures))


def main() -> int:
    try:
        check_docs()
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
        print(f"[docs:check] {error}", file=sys.stderr)
        return 1
    print(
        "[docs:check] local links and bilingual API references are valid",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
