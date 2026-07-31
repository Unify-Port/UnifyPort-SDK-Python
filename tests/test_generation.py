from __future__ import annotations

import importlib.util
import inspect
import io
import json
import stat
import subprocess
import sys
import tarfile
import zipfile
from collections.abc import Mapping
from pathlib import Path
from types import ModuleType
from typing import Any, cast, get_args, get_origin, get_type_hints

import pytest

from unifyport import (
    ApiResult,
    AsyncUnifyPortDeviceClient,
    RequestOptions,
    UnifyPortDeviceClient,
    models,
)
from unifyport._generated import (
    NODE_OPERATION_IDS,
    OPERATIONS,
    PYTHON_METHODS,
    AsyncDeviceMethodsMixin,
    SyncDeviceMethodsMixin,
)
from unifyport._generated.models import SCHEMA_NAMES

ROOT = Path(__file__).resolve().parents[1]


def load_public_checker() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "unifyport_test_check_public",
        ROOT / "scripts/check_public.py",
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    # dataclass 会按 module name 回查 namespace，执行前必须先登记。
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def resolve_model_annotation(annotation: object) -> object:
    def marker() -> None:
        pass

    # expected 也按 model canonical namespace 解析，避免把 ForwardRef 字符串当作期望值。
    marker.__annotations__ = {"return": annotation}
    return cast(object, get_type_hints(marker, globalns=vars(models))["return"])


def test_generated_artifacts_are_deterministic() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/generate.py", "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "generated artifacts are current" in result.stderr


def test_generated_operation_and_schema_coverage_is_complete() -> None:
    assert len(NODE_OPERATION_IDS) == 64
    assert len(OPERATIONS) == 64
    assert len(PYTHON_METHODS) == 64
    assert len(SCHEMA_NAMES) == 70
    assert tuple(OPERATIONS) == NODE_OPERATION_IDS
    assert set(PYTHON_METHODS.values()) == set(NODE_OPERATION_IDS)


def test_every_operation_has_static_sync_and_async_methods() -> None:
    for operation_id, spec in OPERATIONS.items():
        assert PYTHON_METHODS[spec.python_method] == operation_id
        sync_method = getattr(SyncDeviceMethodsMixin, spec.python_method)
        async_method = getattr(AsyncDeviceMethodsMixin, spec.python_method)
        assert inspect.isfunction(sync_method)
        assert inspect.iscoroutinefunction(async_method)
        for method in (sync_method, async_method):
            signature = inspect.signature(method)
            assert "headers" not in signature.parameters
            assert signature.parameters["x_request_id"].annotation == "str | None"
            assert signature.parameters["x_request_id"].default is None
            assert cast(str, signature.return_annotation).startswith("ApiResult[_models.")
            assert cast(str, signature.return_annotation).endswith("Response]")


def test_every_public_operation_annotation_is_runtime_resolvable() -> None:
    expected_options = RequestOptions | Mapping[str, Any] | None
    for spec in OPERATIONS.values():
        expected_response = resolve_model_annotation(getattr(models, spec.response_schema))
        for client_type in (UnifyPortDeviceClient, AsyncUnifyPortDeviceClient):
            # public introspection 必须解析真实对象，不能把 postponed annotation 字符串泄漏给框架。
            hints = get_type_hints(getattr(client_type, spec.python_method))
            assert hints["options"] == expected_options
            assert get_origin(hints["return"]) is ApiResult
            assert get_args(hints["return"]) == (expected_response,)


def test_generated_manifest_preserves_node_and_python_method_mapping() -> None:
    manifest = json.loads((ROOT / "parity/manifest.gen.json").read_text(encoding="utf-8"))
    assert manifest["operationCount"] == 64
    assert manifest["schemaCount"] == 70
    assert manifest["policyCounts"] == {
        "retryable": 19,
        "destructive": 7,
        "secretInput": 8,
        "secretOutput": 12,
        "mcpEligible": 4,
        "pythonMcpExposed": 0,
    }
    assert manifest["pythonMcp"] == {"enabled": False, "exposedOperationCount": 0}
    for operation_id, spec in OPERATIONS.items():
        operation = manifest["operations"][operation_id]
        assert operation["operationId"] == operation_id
        assert operation["pythonMethod"] == spec.python_method
        assert operation["responseSchema"] == spec.response_schema
        assert operation["pythonMcpExposure"] == "never"
        assert operation["headerParameters"] == [
            {
                "name": "X-Request-Id",
                "pythonName": "x_request_id",
                "required": False,
                "schema": "str",
            }
        ]


def test_generated_policy_counts_match_node_release() -> None:
    assert sum(operation.retryable for operation in OPERATIONS.values()) == 19
    assert sum(operation.destructive for operation in OPERATIONS.values()) == 7
    assert sum(operation.secret_input for operation in OPERATIONS.values()) == 8
    assert sum(operation.secret_output for operation in OPERATIONS.values()) == 12
    assert sum(operation.mcp_eligible for operation in OPERATIONS.values()) == 4
    assert not any(operation.python_mcp_exposed for operation in OPERATIONS.values())


def test_generated_bilingual_reference_has_one_page_per_operation() -> None:
    english = {
        path.name for path in (ROOT / "docs/api-reference").glob("*.md") if path.name != "README.md"
    }
    chinese = {
        path.name
        for path in (ROOT / "docs/zh-CN/api-reference").glob("*.md")
        if path.name != "README.md"
    }
    assert len(english) == 64
    assert chinese == english


def test_public_scanner_rejects_zip_symlinks_and_large_entries(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    check_public = load_public_checker()
    monkeypatch.setattr(check_public, "MAX_SCANNED_FILE_BYTES", 4)
    archive_path = tmp_path / "unsafe.whl"
    with zipfile.ZipFile(archive_path, "w") as archive:
        symlink = zipfile.ZipInfo("package/link")
        symlink.create_system = 3
        symlink.external_attr = (stat.S_IFLNK | 0o777) << 16
        archive.writestr(symlink, "target")
        archive.writestr("package/large.txt", "12345")

    _, findings = check_public.scan_public_paths([archive_path])
    assert {finding.rule for finding in findings} == {
        "archive symlink",
        "file exceeds public scan byte limit",
    }


def test_public_scanner_rejects_tar_symlinks_and_large_entries(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    check_public = load_public_checker()
    monkeypatch.setattr(check_public, "MAX_SCANNED_FILE_BYTES", 4)
    archive_path = tmp_path / "unsafe.tar.gz"
    with tarfile.open(archive_path, "w:gz") as archive:
        symlink = tarfile.TarInfo("package/link")
        symlink.type = tarfile.SYMTYPE
        symlink.linkname = "target"
        archive.addfile(symlink)
        large = tarfile.TarInfo("package/large.txt")
        large.size = 5
        archive.addfile(large, io.BytesIO(b"12345"))

    _, findings = check_public.scan_public_paths([archive_path])
    assert {finding.rule for finding in findings} == {
        "archive symlink",
        "file exceeds public scan byte limit",
    }
