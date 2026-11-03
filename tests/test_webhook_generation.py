from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path
from types import ModuleType

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
NANOSECOND_TIMESTAMP = "2026-01-01T00:00:00.123456789Z"


@pytest.fixture
def generator(monkeypatch: pytest.MonkeyPatch) -> ModuleType:
    # 使用真实生成入口，避免只测试序列化 helper 而遗漏 YAML 加载阶段的精度损失。
    monkeypatch.syspath_prepend(str(ROOT / "scripts"))
    spec = importlib.util.spec_from_file_location(
        "unifyport_test_webhook_generator", ROOT / "scripts/generate.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("quote", ["", "'", '"'], ids=["plain", "single-quoted", "double-quoted"])
@pytest.mark.parametrize(
    "timestamp",
    [NANOSECOND_TIMESTAMP, "2026-01-01T08:00:00.000000010+08:00"],
    ids=["nanoseconds-utc", "nanoseconds-offset-trailing-zero"],
)
def test_webhook_artifacts_preserve_nanoseconds_for_every_yaml_quoting_style(
    generator: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    quote: str,
    timestamp: str,
) -> None:
    original = (ROOT / "contracts/device.openapi.yaml").read_text(encoding="utf-8")
    assert f"'{NANOSECOND_TIMESTAMP}'" in original
    contract = original.replace(f"'{NANOSECOND_TIMESTAMP}'", f"{quote}{timestamp}{quote}")
    contract_path = tmp_path / "contract.yaml"
    contract_path.write_text(contract, encoding="utf-8")
    source = json.loads((ROOT / "parity/source.json").read_text(encoding="utf-8"))
    source["contract"]["sha256"] = hashlib.sha256(contract.encode()).hexdigest()
    source_path = tmp_path / "source.json"
    source_path.write_text(json.dumps(source), encoding="utf-8")
    monkeypatch.setattr(generator, "CONTRACT_PATH", contract_path)
    monkeypatch.setattr(generator, "SOURCE_PATH", source_path)

    # 只在内存生成，验证两类公开回归输入；不改动批准契约或已签入产物。
    artifacts = generator.generate_artifacts()
    examples = json.loads(artifacts[ROOT / "tests/fixtures/webhook-examples.json"])
    index = next(
        index
        for index, case in enumerate(examples)
        if case["name"] == "facebookMessageReceived/inbound"
    )
    fixture = examples[index]["body"]
    typing_tree = ast.parse(artifacts[ROOT / "pyright_tests/webhook_examples.py"])
    declarations = [node for node in typing_tree.body if isinstance(node, ast.AnnAssign)]
    typed_example = ast.literal_eval(declarations[index].value)
    for body in [fixture, typed_example]:
        assert body["occurred_at"] == timestamp
        assert body["data"]["message"]["sent_at"] == timestamp


def test_contract_loader_preserves_scalar_types_without_changing_global_yaml_loader(
    generator: ModuleType, tmp_path: Path
) -> None:
    # 时间解析例外只作用于契约；其他调用方仍应使用原有 SafeLoader 行为。
    content = f"timestamp: {NANOSECOND_TIMESTAMP}\nflag: false\nsize: 0\nvalue: null\n"
    path = tmp_path / "contract.yaml"
    path.write_text(content, encoding="utf-8")
    parsed = generator._load_yaml(path)
    assert parsed == {
        "timestamp": NANOSECOND_TIMESTAMP,
        "flag": False,
        "size": 0,
        "value": None,
    }
    assert parsed["flag"] is False
    assert type(parsed["size"]) is int
    assert parsed["value"] is None
    assert isinstance(yaml.safe_load(content)["timestamp"], datetime)
    path.write_text("value: !!python/name:builtins.str\n", encoding="utf-8")
    with pytest.raises(yaml.constructor.ConstructorError):
        generator._load_yaml(path)
