#!/usr/bin/env python3
"""Generate the public Python surface from the pinned Device API contract."""

from __future__ import annotations

import argparse
import hashlib
import json
import keyword
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import yaml  # type: ignore[import-untyped]
from schema_types import structural_schemas

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts/device.openapi.yaml"
POLICY_PATH = ROOT / "policy/operation-policies.json"
SOURCE_PATH = ROOT / "parity/source.json"
GENERATED_DIR = ROOT / "src/unifyport/_generated"
MANIFEST_PATH = ROOT / "parity/manifest.gen.json"
ENGLISH_REFERENCE_DIR = ROOT / "docs/api-reference"
CHINESE_REFERENCE_DIR = ROOT / "docs/zh-CN/api-reference"
HTTP_METHODS = ("get", "put", "post", "delete", "options", "head", "patch", "trace")
EXPECTED_POLICY_COUNTS = {
    "retryable": 19,
    "destructive": 8,
    "secretInput": 9,
    "secretOutput": 16,
    "mcpEligible": 4,
    "pythonMcpExposed": 0,
}

JsonObject = dict[str, Any]


@dataclass(frozen=True, slots=True)
class Parameter:
    name: str
    python_name: str
    required: bool
    schema: JsonObject


@dataclass(frozen=True, slots=True)
class Operation:
    operation_id: str
    python_method: str
    http_method: str
    path: str
    tag: str
    summary: str
    auth_required: bool
    mutability: str
    retryable: bool
    secret_input: bool
    secret_output: bool
    node_mcp_exposure: str
    path_params: tuple[Parameter, ...]
    query_params: tuple[Parameter, ...]
    header_params: tuple[Parameter, ...]
    request_body: JsonObject | None
    request_body_required: bool
    response_schema: JsonObject | None


def _object(value: Any, description: str) -> JsonObject:
    if not isinstance(value, dict) or not all(isinstance(key, str) for key in value):
        raise ValueError(f"{description} must be an object")
    return cast(JsonObject, value)


def _load_yaml(path: Path) -> JsonObject:
    # YAML 输入先收窄到 string-key object，避免生成逻辑默默接受异常节点。
    return _object(yaml.safe_load(path.read_text(encoding="utf-8")), str(path))


def _load_json(path: Path) -> JsonObject:
    return _object(json.loads(path.read_text(encoding="utf-8")), str(path))


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _resolve_ref(document: JsonObject, value: JsonObject) -> JsonObject:
    ref = value.get("$ref")
    if ref is None:
        return value
    if not isinstance(ref, str) or not ref.startswith("#/"):
        raise ValueError(f"only local OpenAPI refs are supported: {ref!r}")
    current: Any = document
    for segment in ref[2:].split("/"):
        key = segment.replace("~1", "/").replace("~0", "~")
        current = _object(current, ref).get(key)
        if current is None:
            raise ValueError(f"unable to resolve OpenAPI ref: {ref}")
    return _resolve_ref(document, _object(current, ref))


def _ref_name(schema: JsonObject | None) -> str | None:
    if schema is None:
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
        return ref.rsplit("/", 1)[-1]
    return None


def _snake_case(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9]+", "_", value)
    acronym_boundary = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", normalized)
    word_boundary = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", acronym_boundary)
    return re.sub(r"_+", "_", word_boundary).strip("_").lower()


def _python_name(value: str) -> str:
    normalized = re.sub(r"\W", "_", _snake_case(value))
    if not normalized or normalized[0].isdigit():
        normalized = f"parameter_{normalized}"
    return f"{normalized}_" if keyword.iskeyword(normalized) else normalized


def _operation_model_prefix(operation: Operation) -> str:
    return "".join(part.capitalize() for part in operation.python_method.split("_"))


def _python_literal(value: Any) -> str:
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    return repr(value)


def _json_schema(content: Any) -> JsonObject | None:
    if not isinstance(content, dict):
        return None
    media = content.get("application/json")
    if not isinstance(media, dict):
        media = next(
            (
                candidate
                for media_type, candidate in content.items()
                if isinstance(media_type, str)
                and media_type.endswith("+json")
                and isinstance(candidate, dict)
            ),
            None,
        )
    if not isinstance(media, dict) or not isinstance(media.get("schema"), dict):
        return None
    return _object(media["schema"], "JSON content schema")


def _collect_parameters(
    document: JsonObject,
    values: list[Any],
) -> dict[str, list[Parameter]]:
    groups: dict[str, list[Parameter]] = {"path": [], "query": [], "header": []}
    for raw in values:
        parameter = _resolve_ref(document, _object(raw, "operation parameter"))
        location = parameter.get("in")
        name = parameter.get("name")
        if location not in groups or not isinstance(name, str):
            continue
        schema = parameter.get("schema")
        groups[cast(str, location)].append(
            Parameter(
                name=name,
                python_name=_python_name(name),
                required=parameter.get("required") is True,
                schema=_object(schema, f"{name} schema") if isinstance(schema, dict) else {},
            )
        )
    return groups


def _success_schema(document: JsonObject, operation: JsonObject) -> JsonObject | None:
    responses = _object(operation.get("responses", {}), "operation responses")
    schemas: list[JsonObject] = []
    for status in sorted(responses):
        if not re.fullmatch(r"2\d\d", status):
            continue
        response = _resolve_ref(document, _object(responses[status], f"response {status}"))
        schema = _json_schema(response.get("content"))
        schemas.append(schema if schema is not None else {"type": "null"})
    # 成功状态的空响应必须进入联合类型，不能把 202 accepted 与 204 混为一谈。
    if not schemas or schemas == [{"type": "null"}]:
        return None
    return schemas[0] if len(schemas) == 1 else {"anyOf": schemas}


def _collect_operations(
    document: JsonObject,
    policy: JsonObject,
) -> list[Operation]:
    paths = _object(document.get("paths"), "paths")
    operations: list[Operation] = []
    seen: set[str] = set()
    retry = set(cast(list[str], policy.get("retryAllowlist", [])))
    secret_input = set(cast(list[str], policy.get("secretInput", [])))
    secret_output = set(cast(list[str], policy.get("secretOutput", [])))
    mutability_overrides = _object(policy.get("mutabilityOverrides", {}), "mutabilityOverrides")
    node_mcp = _object(policy.get("nodeMcpExposure", {}), "nodeMcpExposure")
    header_allowlist = cast(list[str], policy.get("headerAllowlist", []))
    synthetic_headers = tuple(
        Parameter(
            name=name,
            python_name=_python_name(name),
            required=False,
            schema={"type": "string"},
        )
        for name in header_allowlist
    )

    for path, raw_path_item in paths.items():
        path_item = _object(raw_path_item, f"path {path}")
        path_parameters = path_item.get("parameters", [])
        if not isinstance(path_parameters, list):
            raise ValueError(f"{path} parameters must be an array")
        for method in HTTP_METHODS:
            raw_operation = path_item.get(method)
            if raw_operation is None:
                continue
            operation = _object(raw_operation, f"{method.upper()} {path}")
            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str) or not operation_id or operation_id in seen:
                raise ValueError("operationId must be present and unique")
            seen.add(operation_id)
            operation_parameters = operation.get("parameters", [])
            if not isinstance(operation_parameters, list):
                raise ValueError(f"{operation_id} parameters must be an array")
            parameter_groups = _collect_parameters(
                document, [*path_parameters, *operation_parameters]
            )
            explicit_headers = tuple(parameter_groups["header"])
            if any(
                parameter.name.lower() in {"x-api-key", "authorization"}
                for parameter in explicit_headers
            ):
                raise ValueError(f"{operation_id} exposes an authentication header")
            header_by_lower = {parameter.name.lower(): parameter for parameter in explicit_headers}
            for parameter in synthetic_headers:
                header_by_lower.setdefault(parameter.name.lower(), parameter)

            raw_body = operation.get("requestBody")
            request_body_node = (
                _resolve_ref(document, _object(raw_body, f"{operation_id} requestBody"))
                if isinstance(raw_body, dict)
                else None
            )
            request_body_schema = (
                _json_schema(request_body_node.get("content"))
                if request_body_node is not None
                else None
            )
            default_mutability = (
                "read"
                if method in {"get", "head", "options"}
                else "destructive"
                if method == "delete"
                else "write"
            )
            mutability = cast(str, mutability_overrides.get(operation_id, default_mutability))
            tags = operation.get("tags", [])
            tag = (
                tags[0] if isinstance(tags, list) and tags and isinstance(tags[0], str) else "Other"
            )
            summary = operation.get("summary")
            operations.append(
                Operation(
                    operation_id=operation_id,
                    python_method=_snake_case(operation_id),
                    http_method=method.upper(),
                    path=path,
                    tag=tag,
                    summary=summary if isinstance(summary, str) else operation_id,
                    auth_required=(operation.get("security", document.get("security", [])) != []),
                    mutability=mutability,
                    retryable=operation_id in retry,
                    secret_input=operation_id in secret_input,
                    secret_output=operation_id in secret_output,
                    node_mcp_exposure=cast(str, node_mcp.get(operation_id, "never")),
                    path_params=tuple(parameter_groups["path"]),
                    query_params=tuple(parameter_groups["query"]),
                    header_params=tuple(header_by_lower.values()),
                    request_body=request_body_schema,
                    request_body_required=(
                        request_body_node is not None and request_body_node.get("required") is True
                    ),
                    response_schema=_success_schema(document, operation),
                )
            )

    operations.sort(key=lambda item: item.operation_id)
    _validate_policy(operations, policy)
    return operations


def _validate_policy(operations: list[Operation], policy: JsonObject) -> None:
    operation_ids = {operation.operation_id for operation in operations}
    configured: set[str] = set()
    for key in ("retryAllowlist", "secretInput", "secretOutput"):
        values = policy.get(key, [])
        if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
            raise ValueError(f"{key} must be a string array")
        configured.update(cast(list[str], values))
    for key in ("mutabilityOverrides", "nodeMcpExposure"):
        configured.update(_object(policy.get(key, {}), key))
    unknown = configured - operation_ids
    if unknown:
        raise ValueError(f"policy references unknown operations: {sorted(unknown)!r}")
    if policy.get("authenticationHeadersExposed") is not False:
        raise ValueError("authentication headers must not be exposed")
    headers = policy.get("headerAllowlist")
    if headers != ["X-Request-Id"]:
        raise ValueError("headerAllowlist must contain only X-Request-Id")
    python_mcp = _object(policy.get("pythonMcp"), "pythonMcp")
    if python_mcp.get("enabled") is not False or python_mcp.get("eligibleOperations") != []:
        raise ValueError("Python SDK must not expose MCP operations")

    counts = {
        "retryable": sum(operation.retryable for operation in operations),
        "destructive": sum(operation.mutability == "destructive" for operation in operations),
        "secretInput": sum(operation.secret_input for operation in operations),
        "secretOutput": sum(operation.secret_output for operation in operations),
        "mcpEligible": sum(operation.node_mcp_exposure != "never" for operation in operations),
        "pythonMcpExposed": 0,
    }
    if counts != EXPECTED_POLICY_COUNTS:
        raise ValueError(f"operation policy counts differ from Node v0.4.0: {counts!r}")


def _schema_type(
    schema: JsonObject | bool | None,
    *,
    model_prefix: str = "",
    quote_refs: bool = False,
) -> str:
    if schema is None:
        return "None"
    if schema is False:
        return "Never"
    if schema is True:
        return "JsonValue"
    if schema.get("x-python-never"):
        return "Never"
    for composition in ("oneOf", "anyOf"):
        variants = schema.get(composition)
        if isinstance(variants, list) and variants:
            alternatives = [
                _schema_type(part, model_prefix=model_prefix, quote_refs=quote_refs)
                for part in variants
            ]
            return (
                "Union[" + ", ".join(alternatives) + "]" if quote_refs else " | ".join(alternatives)
            )
    ref_name = _ref_name(schema)
    if ref_name is not None:
        reference = f"{model_prefix}{ref_name}"
        return _python_literal(reference) if quote_refs else reference
    enum = schema.get("enum")
    if isinstance(enum, list) and enum:
        return f"Literal[{', '.join(_python_literal(value) for value in enum)}]"
    const = schema.get("const")
    if "const" in schema:
        return f"Literal[{_python_literal(const)}]"
    schema_type = schema.get("type")
    if isinstance(schema_type, list):
        return " | ".join(
            _schema_type(
                {**schema, "type": item},
                model_prefix=model_prefix,
                quote_refs=quote_refs,
            )
            for item in schema_type
        )
    if schema_type == "string":
        return "str"
    if schema_type == "integer":
        return "int"
    if schema_type == "number":
        return "float"
    if schema_type == "boolean":
        return "bool"
    if schema_type == "null":
        return "None"
    if schema_type == "array":
        items = schema.get("items")
        item_schema = _object(items, "array items") if isinstance(items, dict) else {}
        item_type = _schema_type(
            item_schema,
            model_prefix=model_prefix,
            quote_refs=quote_refs,
        )
        return f"list[{item_type}]"
    if schema_type == "object":
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            value_type = _schema_type(
                _object(additional, "additionalProperties"),
                model_prefix=model_prefix,
                quote_refs=quote_refs,
            )
            return f"dict[str, {value_type}]"
        return "dict[str, JsonValue]"
    all_of = schema.get("allOf")
    if isinstance(all_of, list) and all_of:
        refs = [_ref_name(_object(part, "allOf item")) for part in all_of if isinstance(part, dict)]
        named = [f"{model_prefix}{name}" for name in refs if name is not None]
        if quote_refs:
            named = [_python_literal(name) for name in named]
        return named[0] if len(named) == 1 else "dict[str, JsonValue]"
    return "JsonValue"


def _flatten_schema(
    name: str,
    schema: JsonObject,
    schemas: JsonObject,
    trail: frozenset[str] = frozenset(),
) -> tuple[dict[str, JsonObject], set[str], dict[str, tuple[str, ...]]]:
    if name in trail:
        raise ValueError(f"recursive allOf schema: {name}")
    properties: dict[str, JsonObject] = {}
    required: set[str] = set()
    dependencies: dict[str, tuple[str, ...]] = {}
    all_of = schema.get("allOf", [])
    if isinstance(all_of, list):
        for raw_part in all_of:
            part = _object(raw_part, f"{name}.allOf")
            ref_name = _ref_name(part)
            if ref_name is not None:
                base = _object(schemas.get(ref_name), f"schema {ref_name}")
                base_properties, base_required, base_dependencies = _flatten_schema(
                    ref_name, base, schemas, trail | {name}
                )
                properties.update(base_properties)
                required.update(base_required)
                dependencies.update(base_dependencies)
            else:
                nested_properties, nested_required, nested_dependencies = _flatten_schema(
                    name, part, schemas, trail
                )
                properties.update(nested_properties)
                required.update(nested_required)
                dependencies.update(nested_dependencies)
    raw_properties = schema.get("properties", {})
    if isinstance(raw_properties, dict):
        for property_name, raw_property in raw_properties.items():
            if isinstance(property_name, str) and isinstance(raw_property, (dict, bool)):
                properties[property_name] = (
                    raw_property
                    if isinstance(raw_property, dict)
                    else ({"x-python-never": True} if raw_property is False else {})
                )
    raw_required = schema.get("required", [])
    if isinstance(raw_required, list):
        required.update(value for value in raw_required if isinstance(value, str))
    raw_dependencies = schema.get("dependentRequired", {})
    if isinstance(raw_dependencies, dict):
        for key, values in raw_dependencies.items():
            if isinstance(key, str) and isinstance(values, list):
                dependencies[key] = tuple(value for value in values if isinstance(value, str))
    return properties, required, dependencies


def _generated_header(source: str) -> str:
    return (
        '"""Generated from '
        + source
        + '; edit the contract, policy, or generator instead."""\n\n'
        + "# 此文件由生成链维护，手改会在 generate --check 中被拒绝。\n"
    )


def _typed_dict_definition(name: str, parameters: tuple[Parameter, ...]) -> list[str]:
    if all(
        parameter.name.isidentifier() and not keyword.iskeyword(parameter.name)
        for parameter in parameters
    ):
        lines = [f"class {name}(TypedDict, total=False):"]
        if not parameters:
            lines.append("    pass")
        for parameter in parameters:
            wrapper = "Required" if parameter.required else "NotRequired"
            lines.append(f"    {parameter.name}: {wrapper}[{_schema_type(parameter.schema)}]")
        return [*lines, "", ""]
    lines = [f"{name} = TypedDict(", f"    {_python_literal(name)},", "    {"]
    for parameter in parameters:
        wrapper = "Required" if parameter.required else "NotRequired"
        lines.append(
            f"        {_python_literal(parameter.name)}: "
            f"{wrapper}[{_schema_type(parameter.schema)}],"
        )
    return [*lines, "    },", "    total=False,", ")", "", ""]


def _generate_models(schemas: JsonObject, operations: list[Operation]) -> str:
    lines = [
        _generated_header("contracts/device.openapi.yaml"),
        "from types import MappingProxyType",
        "from typing import (",
        "    Final,",
        "    Generic,",
        "    Literal,",
        "    Never,",
        "    NotRequired,",
        "    Required,",
        "    TypeAlias,",
        "    TypeVar,",
        "    Union,",
        ")",
        "",
        "from typing_extensions import TypedDict",
        "",
        "JsonScalar: TypeAlias = bool | float | int | str | None",
        'JsonValue: TypeAlias = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]',
        "",
        'ResponseT = TypeVar("ResponseT")',
        "",
        "",
        "class ResponseEnvelope(TypedDict, Generic[ResponseT], total=False):",
        "    request_id: NotRequired[str]",
        "    client_request_id: NotRequired[str]",
        "    data: Required[ResponseT]",
        "",
        "",
    ]
    dependencies: dict[str, dict[str, tuple[str, ...]]] = {}
    aliases: list[tuple[str, str]] = []
    definitions = structural_schemas(schemas)
    for name in sorted(definitions):
        schema = _object(definitions[name], f"schema {name}")
        ref_name = _ref_name(schema)
        enum = schema.get("enum")
        properties, required, dependent_required = _flatten_schema(name, schema, definitions)
        if dependent_required:
            dependencies[name] = dependent_required
        if ref_name is not None:
            # alias 延后到全部 class 之后，避免运行时赋值早于被引用 model。
            aliases.append((name, ref_name))
            continue
        if isinstance(enum, list) and enum:
            lines.append(f"{name}: TypeAlias = Literal[")
            lines.extend(f"    {_python_literal(value)}," for value in enum)
            lines.extend(["]", "", ""])
            continue
        if "anyOf" in schema or "oneOf" in schema:
            aliases.append((name, _schema_type(schema, quote_refs=True)))
            continue
        if not properties:
            lines.extend([f"{name}: TypeAlias = {_schema_type(schema)}", "", ""])
            continue
        if any(not field.isidentifier() or keyword.iskeyword(field) for field in properties):
            # 带连字符的 provider key 必须保留原名，函数式 TypedDict 不会把协议键改写成标识符。
            lines.extend([f"{name} = TypedDict(", f"    {_python_literal(name)},", "    {"])
            for field in sorted(properties):
                wrapper = "Required" if field in required else "NotRequired"
                annotation = _schema_type(properties[field], quote_refs=True)
                lines.append(f"        {_python_literal(field)}: {wrapper}[{annotation}],")
            lines.extend(["    },", "    total=False,", ")", "", ""])
            continue
        if schema.get("additionalProperties") is True:
            lines.extend(
                [
                    "# mypy 2.3 尚未识别 PEP 728；unused-ignore 避免 checker 升级后产生漂移。",
                    # 格式化后忽略标记仍要落在 class 首行，mypy 的诊断不会定位到右括号。
                    f"class {name}(  # type: ignore[call-arg, unused-ignore]",
                    "    TypedDict, total=False, extra_items=JsonValue",
                    "):",
                ]
            )
        else:
            lines.append(f"class {name}(TypedDict, total=False):")
        for property_name in sorted(properties):
            wrapper = "Required" if property_name in required else "NotRequired"
            annotation = _schema_type(properties[property_name], quote_refs=True)
            lines.append(f"    {property_name}: {wrapper}[{annotation}]")
        lines.extend(["", ""])

    for name, ref_name in aliases:
        lines.extend([f"{name}: TypeAlias = {ref_name}", "", ""])

    operation_model_names: list[str] = []
    for operation in operations:
        prefix = _operation_model_prefix(operation)
        path_name = f"{prefix}Path"
        query_name = f"{prefix}Query"
        body_name = f"{prefix}RequestBody"
        response_name = f"{prefix}Response"
        operation_model_names.extend([path_name, query_name, body_name, response_name])
        lines.extend(_typed_dict_definition(path_name, operation.path_params))
        lines.extend(_typed_dict_definition(query_name, operation.query_params))
        lines.extend(
            [
                f"{body_name}: TypeAlias = {_schema_type(operation.request_body)}",
                "",
                "",
                f"{response_name}: TypeAlias = {_response_type(operation.response_schema)}",
                "",
                "",
            ]
        )

    schema_names = tuple(sorted(schemas))
    lines.extend(["SCHEMA_NAMES: Final = ("])
    lines.extend(f"    {_python_literal(name)}," for name in schema_names)
    lines.extend([")", "", ""])
    lines.extend(
        [
            "DEPENDENT_REQUIRED: Final[MappingProxyType[str, "
            "MappingProxyType[str, tuple[str, ...]]]] = MappingProxyType(",
            "    {",
        ]
    )
    for schema_name, fields in sorted(dependencies.items()):
        lines.extend(
            [
                f"        {_python_literal(schema_name)}: MappingProxyType(",
                "            {",
            ]
        )
        for field_name, required_fields in sorted(fields.items()):
            values = ", ".join(_python_literal(value) for value in required_fields)
            suffix = "," if len(required_fields) == 1 else ""
            lines.append(f"                {_python_literal(field_name)}: ({values}{suffix}),")
        lines.extend(["            }", "        ),"])
    lines.extend(
        [
            "    }",
            ")",
            "",
            "",
            "__all__ = [",
            '    "DEPENDENT_REQUIRED",',
            '    "ResponseEnvelope",',
            '    "SCHEMA_NAMES",',
            '    "JsonScalar",',
            '    "JsonValue",',
            *[f"    {_python_literal(name)}," for name in sorted(definitions)],
            *[f"    {_python_literal(name)}," for name in operation_model_names],
            "]",
            "",
        ]
    )
    return "\n".join(lines)


def _response_type(schema: JsonObject | None, *, model_prefix: str = "") -> str:
    if schema is None:
        return "None"
    alternatives = schema.get("anyOf")
    if isinstance(alternatives, list):
        return " | ".join(
            _response_type(_object(part, "response variant"), model_prefix=model_prefix)
            for part in alternatives
        )
    all_of = schema.get("allOf")
    if isinstance(all_of, list):
        has_meta = any(
            _ref_name(_object(part, "response allOf")) == "ResponseMeta" for part in all_of
        )
        for raw_part in all_of:
            part = _object(raw_part, "response allOf")
            properties = part.get("properties")
            if (
                has_meta
                and isinstance(properties, dict)
                and isinstance(properties.get("data"), dict)
            ):
                data_type = _schema_type(
                    _object(properties["data"], "response data"),
                    model_prefix=model_prefix,
                )
                return f"{model_prefix}ResponseEnvelope[{data_type}]"
    return _schema_type(schema, model_prefix=model_prefix)


def _parameter_schema_label(parameter: Parameter) -> str:
    return _schema_type(parameter.schema)


def _body_schema_label(schema: JsonObject | None) -> str | None:
    if schema is None:
        return None
    return _ref_name(schema) or _schema_type(schema)


def _generate_operations(operations: list[Operation]) -> str:
    lines = [
        _generated_header("contracts/device.openapi.yaml and policy/operation-policies.json"),
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping",
        "from dataclasses import dataclass",
        "from types import MappingProxyType",
        "from typing import Final, Literal",
        "",
        "",
        "@dataclass(frozen=True, slots=True)",
        "class ParameterSpec:",
        "    name: str",
        "    python_name: str",
        "    required: bool",
        "    schema: str",
        "",
        "",
        "@dataclass(frozen=True, slots=True)",
        "class OperationSpec:",
        "    operation_id: str",
        "    python_method: str",
        "    http_method: str",
        "    path: str",
        "    tag: str",
        "    summary: str",
        "    auth_required: bool",
        '    mutability: Literal["read", "write", "destructive"]',
        "    retryable: bool",
        "    destructive: bool",
        "    secret_input: bool",
        "    secret_output: bool",
        '    node_mcp_exposure: Literal["read", "write", "destructive", "never"]',
        "    mcp_eligible: bool",
        "    python_mcp_exposed: bool",
        "    path_params: tuple[ParameterSpec, ...]",
        "    query_params: tuple[ParameterSpec, ...]",
        "    header_params: tuple[ParameterSpec, ...]",
        "    request_body: str | None",
        "    request_body_required: bool",
        "    response_schema: str",
        "",
        "",
        "OPERATIONS: Final[Mapping[str, OperationSpec]] = MappingProxyType(",
        "    {",
    ]

    def append_parameter_tuple(
        field: str,
        parameters: tuple[Parameter, ...],
    ) -> None:
        if not parameters:
            lines.append(f"            {field}=(),")
            return
        lines.append(f"            {field}=(")
        for parameter in parameters:
            lines.extend(
                [
                    "                ParameterSpec(",
                    f"                    name={_python_literal(parameter.name)},",
                    f"                    python_name={_python_literal(parameter.python_name)},",
                    f"                    required={parameter.required!r},",
                    "                    schema="
                    f"{_python_literal(_parameter_schema_label(parameter))},",
                    "                ),",
                ]
            )
        lines.append("            ),")

    for operation in operations:
        operation_prefix = _operation_model_prefix(operation)
        lines.extend(
            [
                f"        {_python_literal(operation.operation_id)}: OperationSpec(",
                f"            operation_id={_python_literal(operation.operation_id)},",
                f"            python_method={_python_literal(operation.python_method)},",
                f"            http_method={_python_literal(operation.http_method)},",
                f"            path={_python_literal(operation.path)},",
                f"            tag={_python_literal(operation.tag)},",
                f"            summary={_python_literal(operation.summary)},",
                f"            auth_required={operation.auth_required!r},",
                f"            mutability={_python_literal(operation.mutability)},",
                f"            retryable={operation.retryable!r},",
                f"            destructive={operation.mutability == 'destructive'!r},",
                f"            secret_input={operation.secret_input!r},",
                f"            secret_output={operation.secret_output!r},",
                f"            node_mcp_exposure={_python_literal(operation.node_mcp_exposure)},",
                f"            mcp_eligible={operation.node_mcp_exposure != 'never'!r},",
                "            python_mcp_exposed=False,",
            ]
        )
        append_parameter_tuple("path_params", operation.path_params)
        append_parameter_tuple("query_params", operation.query_params)
        append_parameter_tuple("header_params", operation.header_params)
        request_body = (
            f"{operation_prefix}RequestBody" if operation.request_body is not None else None
        )
        lines.extend(
            [
                f"            request_body={_python_literal(request_body)},",
                f"            request_body_required={operation.request_body_required!r},",
                f"            response_schema={_python_literal(operation_prefix + 'Response')},",
                "        ),",
            ]
        )
    lines.extend(
        [
            "    }",
            ")",
            "",
            "",
            "PYTHON_METHODS: Final[Mapping[str, str]] = MappingProxyType(",
            "    {",
            *[
                f"        {_python_literal(operation.python_method)}: "
                f"{_python_literal(operation.operation_id)},"
                for operation in operations
            ],
            "    }",
            ")",
            "",
            "",
            "NODE_OPERATION_IDS: Final = (",
            *[f"    {_python_literal(operation.operation_id)}," for operation in operations],
            ")",
            "",
            "",
            (
                '__all__ = ["NODE_OPERATION_IDS", "OPERATIONS", "PYTHON_METHODS", '
                '"OperationSpec", "ParameterSpec"]'
            ),
            "",
        ]
    )
    return "\n".join(lines)


def _method_signature(operation: Operation, *, asynchronous: bool) -> list[str]:
    parameters = [*operation.path_params, *operation.query_params, *operation.header_params]
    required = [parameter for parameter in parameters if parameter.required]
    optional = [parameter for parameter in parameters if not parameter.required]
    operation_prefix = _operation_model_prefix(operation)
    body_type = (
        f"_models.{operation_prefix}RequestBody" if operation.request_body is not None else None
    )
    response_type = f"_models.{operation_prefix}Response"
    prefix = "async def" if asynchronous else "def"
    lines = [f"    {prefix} {operation.python_method}(", "        self,", "        *,"]
    for parameter in required:
        annotation = _schema_type(parameter.schema, model_prefix="_models.")
        lines.append(f"        {parameter.python_name}: {annotation},")
    if body_type is not None and operation.request_body_required:
        lines.append(f"        body: {body_type},")
    for parameter in optional:
        annotation = _schema_type(parameter.schema, model_prefix="_models.")
        lines.append(f"        {parameter.python_name}: {annotation} | None = None,")
    if body_type is not None and not operation.request_body_required:
        lines.append(f"        body: {body_type} | None = None,")
    lines.extend(
        [
            "        options: RequestOptions | Mapping[str, Any] | None = None,",
            f"    ) -> ApiResult[{response_type}]:",
            f'        """{operation.summary}"""',
        ]
    )
    path_expression = (
        "{"
        + ", ".join(
            f"{_python_literal(parameter.name)}: {parameter.python_name}"
            for parameter in operation.path_params
        )
        + "}"
        if operation.path_params
        else "None"
    )
    if operation.query_params:
        lines.append("        query = {")
        for parameter in operation.query_params:
            lines.append(f"            {_python_literal(parameter.name)}: {parameter.python_name},")
        lines.extend(
            [
                "        }",
                (
                    "        query_params = {name: value for name, value in "
                    "query.items() if value is not None} or None"
                ),
            ]
        )
    else:
        lines.append("        query_params = None")
    if operation.header_params:
        lines.append("        request_headers = {")
        for parameter in operation.header_params:
            lines.append(f"            {_python_literal(parameter.name)}: {parameter.python_name},")
        lines.extend(
            [
                "        }",
                "        header_params = {",
                (
                    "            name: value for name, value in "
                    "request_headers.items() if value is not None"
                ),
                "        } or None",
            ]
        )
    else:
        lines.append("        header_params = None")
    await_prefix = "await " if asynchronous else ""
    body_expression = "body" if operation.request_body is not None else "None"
    lines.extend(
        [
            f"        return {await_prefix}self._execute_operation(",
            f"            {_python_literal(operation.operation_id)},",
            f"            path_params={path_expression},",
            "            query=query_params,",
            f"            body={body_expression},",
            "            headers=header_params,",
            "            options=options,",
            "        )",
            "",
        ]
    )
    return lines


def _generate_methods(operations: list[Operation], *, asynchronous: bool) -> str:
    class_name = "AsyncDeviceMethodsMixin" if asynchronous else "SyncDeviceMethodsMixin"
    execute_prefix = "async def" if asynchronous else "def"
    lines = [
        _generated_header("contracts/device.openapi.yaml"),
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping",
        "from typing import TYPE_CHECKING, Any",
        "",
        "# public annotation 必须在运行时可解析，供 get_type_hints 等 introspection 使用。",
        "from unifyport.config import RequestOptions",
        "from unifyport.result import ApiResult",
        "",
        "from . import models as _models",
        "",
        "# recursive JsonValue 会按 method module namespace 求值，因此保留运行时名称。",
        "from .models import JsonValue  # noqa: F401",
        "",
        "# 联合别名里的 ForwardRef 按方法 namespace 解析，补齐生成模型名称以支持 introspection。",
        "globals().update({name: getattr(_models, name) for name in _models.__all__})",
        "",
        "",
        f"class {class_name}:",
        "    if TYPE_CHECKING:",
        "",
        f"        {execute_prefix} _execute_operation(",
        "            self,",
        "            operation_id: str,",
        "            *,",
        "            path_params: Mapping[str, object] | None = None,",
        "            query: Mapping[str, object] | None = None,",
        "            body: object | None = None,",
        "            headers: Mapping[str, str] | None = None,",
        "            options: RequestOptions | Mapping[str, Any] | None = None,",
        "        ) -> ApiResult[Any]: ...",
        "",
    ]
    for operation in operations:
        lines.extend(_method_signature(operation, asynchronous=asynchronous))
    lines.extend(["", f'__all__ = ["{class_name}"]', ""])
    return "\n".join(lines)


def _generate_init() -> str:
    return "\n".join(
        [
            _generated_header("the pinned Device API contract"),
            "from .async_methods import AsyncDeviceMethodsMixin",
            "from .operations import (",
            "    NODE_OPERATION_IDS,",
            "    OPERATIONS,",
            "    PYTHON_METHODS,",
            "    OperationSpec,",
            "    ParameterSpec,",
            ")",
            "from .sync_methods import SyncDeviceMethodsMixin",
            "",
            "__all__ = [",
            '    "AsyncDeviceMethodsMixin",',
            '    "NODE_OPERATION_IDS",',
            '    "OPERATIONS",',
            '    "PYTHON_METHODS",',
            '    "OperationSpec",',
            '    "ParameterSpec",',
            '    "SyncDeviceMethodsMixin",',
            "]",
            "",
        ]
    )


def _parameter_manifest(parameter: Parameter) -> JsonObject:
    return {
        "name": parameter.name,
        "pythonName": parameter.python_name,
        "required": parameter.required,
        "schema": _parameter_schema_label(parameter),
    }


def _schema_kind(schema: JsonObject) -> str:
    if _ref_name(schema) is not None:
        return "alias"
    if isinstance(schema.get("enum"), list):
        return "enum"
    if isinstance(schema.get("allOf"), list):
        return "allOf"
    return cast(str, schema.get("type", "unknown"))


def _generate_manifest(
    source: JsonObject,
    contract_sha: str,
    operations: list[Operation],
    schemas: JsonObject,
) -> str:
    manifest_operations: JsonObject = {}
    for operation in operations:
        manifest_operations[operation.operation_id] = {
            "operationId": operation.operation_id,
            "pythonMethod": operation.python_method,
            "method": operation.http_method,
            "path": operation.path,
            "tag": operation.tag,
            "summary": operation.summary,
            "authRequired": operation.auth_required,
            "mutability": operation.mutability,
            "retryable": operation.retryable,
            "destructive": operation.mutability == "destructive",
            "secretInput": operation.secret_input,
            "secretOutput": operation.secret_output,
            "nodeMcpExposure": operation.node_mcp_exposure,
            "mcpEligible": operation.node_mcp_exposure != "never",
            "pythonMcpExposure": "never",
            "pathParameters": [
                _parameter_manifest(parameter) for parameter in operation.path_params
            ],
            "queryParameters": [
                _parameter_manifest(parameter) for parameter in operation.query_params
            ],
            "headerParameters": [
                _parameter_manifest(parameter) for parameter in operation.header_params
            ],
            "requestBody": (
                {
                    "required": operation.request_body_required,
                    "schema": _body_schema_label(operation.request_body),
                    "pythonModel": f"{_operation_model_prefix(operation)}RequestBody",
                }
                if operation.request_body is not None
                else None
            ),
            "responseSchema": f"{_operation_model_prefix(operation)}Response",
            "responseContractType": _response_type(operation.response_schema),
        }
    manifest_schemas: JsonObject = {}
    for name in sorted(schemas):
        schema = _object(schemas[name], f"schema {name}")
        _, _, dependencies = _flatten_schema(name, schema, schemas)
        manifest_schemas[name] = {
            "pythonModel": name,
            "kind": _schema_kind(schema),
            "dependentRequired": {
                field: list(values) for field, values in sorted(dependencies.items())
            },
        }
    manifest = {
        "schemaVersion": 1,
        "nodeSdk": source["nodeSdk"],
        "contractSha256": contract_sha,
        "operationCount": len(operations),
        "schemaCount": len(schemas),
        "policyCounts": EXPECTED_POLICY_COUNTS,
        "pythonMcp": {
            "enabled": False,
            "exposedOperationCount": 0,
        },
        "operations": manifest_operations,
        "schemas": manifest_schemas,
    }
    return json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"


def _reference_filename(operation: Operation) -> str:
    return f"{operation.python_method.replace('_', '-')}.md"


def _parameter_rows(parameters: tuple[Parameter, ...], *, chinese: bool) -> list[str]:
    if not parameters:
        empty = "无" if chinese else "None"
        return [f"| {empty} | - | - | - |"]
    rows: list[str] = []
    for parameter in parameters:
        required = (
            ("是" if parameter.required else "否")
            if chinese
            else ("yes" if parameter.required else "no")
        )
        rows.append(
            "| "
            f"`{parameter.name}` | `{parameter.python_name}` | {required} | "
            f"`{_parameter_schema_label(parameter)}` |"
        )
    return rows


def _generate_reference_page(operation: Operation, *, chinese: bool) -> str:
    filename = _reference_filename(operation)
    prefix = _operation_model_prefix(operation)
    body_contract = _body_schema_label(operation.request_body) or "None"
    response_contract = _response_type(operation.response_schema)
    if chinese:
        navigation = f"[English](../../api-reference/{filename}) | [简体中文]({filename})"
        intro = f"公开 Device API operation `{operation.operation_id}` 的 Python 显式方法。"
        labels = {
            "method": "HTTP",
            "python": "Python 方法",
            "node": "Node operationId",
            "parameters": "参数",
            "path": "Path 参数",
            "query": "Query 参数",
            "headers": "Header 参数",
            "body": "Request body",
            "name": "Wire 名称",
            "required": "必填",
            "schema": "类型",
            "response": "成功响应",
            "policy": "Policy",
        }
        auth_note = "认证 header 不属于 operation 输入；`X-Api-Key` 只能来自 client config。"
    else:
        navigation = f"[English]({filename}) | [简体中文](../zh-CN/api-reference/{filename})"
        intro = (
            f"Explicit Python method for public Device API operation `{operation.operation_id}`."
        )
        labels = {
            "method": "HTTP",
            "python": "Python method",
            "node": "Node operationId",
            "parameters": "Parameters",
            "path": "Path parameters",
            "query": "Query parameters",
            "headers": "Header parameters",
            "body": "Request body",
            "name": "Wire name",
            "required": "Required",
            "schema": "Type",
            "response": "Success response",
            "policy": "Policy",
        }
        auth_note = (
            "Authentication headers are not operation inputs; `X-Api-Key` comes only from "
            "client configuration."
        )
    body_required = (
        "是"
        if chinese and operation.request_body_required
        else "否"
        if chinese
        else "yes"
        if operation.request_body_required
        else "no"
    )
    policy_rows = [
        ("retryable", operation.retryable),
        ("destructive", operation.mutability == "destructive"),
        ("secretInput", operation.secret_input),
        ("secretOutput", operation.secret_output),
        ("Node MCP eligible", operation.node_mcp_exposure != "never"),
        ("Python MCP exposed", False),
    ]
    lines = [
        "<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->",
        f"<!-- operationId: {operation.operation_id} -->",
        "",
        navigation,
        "",
        f"# `{operation.python_method}`",
        "",
        intro,
        "",
        f"- {labels['method']}: `{operation.http_method} {operation.path}`",
        f"- {labels['python']}: `{operation.python_method}`",
        f"- {labels['node']}: `{operation.operation_id}`",
        "",
        f"## {labels['parameters']}",
        "",
        f"### {labels['path']}",
        "",
        f"| {labels['name']} | Python | {labels['required']} | {labels['schema']} |",
        "| --- | --- | --- | --- |",
        *_parameter_rows(operation.path_params, chinese=chinese),
        "",
        f"### {labels['query']}",
        "",
        f"| {labels['name']} | Python | {labels['required']} | {labels['schema']} |",
        "| --- | --- | --- | --- |",
        *_parameter_rows(operation.query_params, chinese=chinese),
        "",
        f"### {labels['headers']}",
        "",
        f"| {labels['name']} | Python | {labels['required']} | {labels['schema']} |",
        "| --- | --- | --- | --- |",
        *_parameter_rows(operation.header_params, chinese=chinese),
        "",
        auth_note,
        "",
        f"### {labels['body']}",
        "",
        f"- {labels['required']}: `{body_required}`",
        f"- Python model: `{prefix}RequestBody`",
        f"- Contract schema: `{body_contract}`",
        "",
        f"## {labels['response']}",
        "",
        f"- Python model: `{prefix}Response`",
        f"- Contract schema: `{response_contract}`",
        "",
        f"## {labels['policy']}",
        "",
        "| Flag | Value |",
        "| --- | --- |",
        *[f"| `{name}` | `{'true' if value else 'false'}` |" for name, value in policy_rows],
        f"| `mutability` | `{operation.mutability}` |",
        f"| `nodeMcpExposure` | `{operation.node_mcp_exposure}` |",
        "| `pythonMcpExposure` | `never` |",
        "",
    ]
    return "\n".join(lines)


def _generate_reference_index(operations: list[Operation], *, chinese: bool) -> str:
    if chinese:
        navigation = "[English](../../api-reference/README.md) | [简体中文](README.md)"
        title = "Device API Reference"
        description = "每个公开 operation 都映射到一个静态 snake_case Python 方法。"
    else:
        navigation = "[English](README.md) | [简体中文](../zh-CN/api-reference/README.md)"
        title = "Device API Reference"
        description = "Every public operation maps to one static snake_case Python method."
    lines = [
        "<!-- 此页由 scripts/generate.py 生成；请修改 contract、policy 或 generator。 -->",
        "",
        navigation,
        "",
        f"# {title}",
        "",
        description,
        "",
        "| Python method | Node operationId | HTTP |",
        "| --- | --- | --- |",
    ]
    for operation in operations:
        lines.append(
            f"| [`{operation.python_method}`]({_reference_filename(operation)}) | "
            f"`{operation.operation_id}` | `{operation.http_method} {operation.path}` |"
        )
    lines.append("")
    return "\n".join(lines)


def generate_artifacts() -> dict[Path, str]:
    document = _load_yaml(CONTRACT_PATH)
    policy = _load_json(POLICY_PATH)
    source = _load_json(SOURCE_PATH)
    contract_bytes = CONTRACT_PATH.read_bytes()
    contract_sha = _sha256(contract_bytes)
    source_contract = _object(source.get("contract"), "source.contract")
    if source_contract.get("sha256") != contract_sha:
        raise ValueError("contract hash differs from parity/source.json")
    operations = _collect_operations(document, policy)
    components = _object(document.get("components"), "components")
    schemas = _object(components.get("schemas"), "components.schemas")
    expected_operations = source_contract.get("operationCount")
    expected_schemas = source_contract.get("schemaCount")
    if len(operations) != expected_operations or len(schemas) != expected_schemas:
        raise ValueError(
            f"contract coverage differs from source manifest: {len(operations)} operations, "
            f"{len(schemas)} schemas"
        )
    artifacts = {
        GENERATED_DIR / "__init__.py": _generate_init(),
        GENERATED_DIR / "models.py": _generate_models(schemas, operations),
        GENERATED_DIR / "operations.py": _generate_operations(operations),
        GENERATED_DIR / "sync_methods.py": _generate_methods(operations, asynchronous=False),
        GENERATED_DIR / "async_methods.py": _generate_methods(operations, asynchronous=True),
        MANIFEST_PATH: _generate_manifest(source, contract_sha, operations, schemas),
    }
    artifacts[ENGLISH_REFERENCE_DIR / "README.md"] = _generate_reference_index(
        operations, chinese=False
    )
    artifacts[CHINESE_REFERENCE_DIR / "README.md"] = _generate_reference_index(
        operations, chinese=True
    )
    for operation in operations:
        filename = _reference_filename(operation)
        artifacts[ENGLISH_REFERENCE_DIR / filename] = _generate_reference_page(
            operation, chinese=False
        )
        artifacts[CHINESE_REFERENCE_DIR / filename] = _generate_reference_page(
            operation, chinese=True
        )
    # 复杂联合与 PEP 728 注解交给固定版本格式化器，生成检查和普通格式检查使用同一结果。
    for path, content in list(artifacts.items()):
        if path.suffix == ".py":
            result = subprocess.run(
                [sys.executable, "-m", "ruff", "format", "--stdin-filename", str(path), "-"],
                input=content,
                text=True,
                capture_output=True,
                cwd=ROOT,
                check=False,
            )
            if result.returncode != 0:
                raise RuntimeError("unable to format generated Python source")
            artifacts[path] = result.stdout
    return artifacts


def _write_or_check(artifacts: dict[Path, str], *, check: bool) -> int:
    stale: list[Path] = []
    for path, expected in artifacts.items():
        actual = path.read_text(encoding="utf-8") if path.is_file() else None
        if actual == expected:
            continue
        stale.append(path)
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8", newline="\n")
            print(f"[generate] {path.relative_to(ROOT)}", file=sys.stderr)
    generated_directories = (
        (GENERATED_DIR, "*.py"),
        (ENGLISH_REFERENCE_DIR, "*.md"),
        (CHINESE_REFERENCE_DIR, "*.md"),
    )
    for directory, pattern in generated_directories:
        expected_generated = {path for path in artifacts if path.parent == directory}
        if not directory.is_dir():
            continue
        for path in directory.glob(pattern):
            if path in expected_generated:
                continue
            stale.append(path)
            if not check:
                path.unlink()
                print(f"[generate] removed {path.relative_to(ROOT)}", file=sys.stderr)
    if check and stale:
        print("generated artifacts are stale; run python scripts/generate.py:", file=sys.stderr)
        for path in sorted(set(stale)):
            print(f"- {path.relative_to(ROOT)}", file=sys.stderr)
        return 1
    if check:
        print("[generate:check] generated artifacts are current", file=sys.stderr)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    arguments = parser.parse_args()
    return _write_or_check(generate_artifacts(), check=arguments.check)


if __name__ == "__main__":
    raise SystemExit(main())
