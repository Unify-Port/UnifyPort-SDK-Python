"""Lower public JSON Schema object compositions into structural typing variants."""

from __future__ import annotations

from copy import deepcopy
from itertools import product
from typing import Any

Schema = dict[str, Any]


def structural_schemas(schemas: Schema) -> Schema:
    output: Schema = {}

    def resolve(value: Schema) -> Schema:
        reference = value.get("$ref", "")
        if reference.startswith("#/components/schemas/"):
            return schemas[reference.rsplit("/", 1)[1]]  # type: ignore[no-any-return]
        return value

    def merge(left: Schema, right: Schema) -> Schema:
        result = deepcopy(left)
        for key, value in right.items():
            if key == "properties":
                fields = result.setdefault(key, {})
                for name, field in value.items():
                    previous = fields.get(name)
                    if previous is False or field is False:
                        fields[name] = False
                    elif isinstance(previous, dict) and isinstance(field, dict):
                        fields[name] = merge(resolve(previous), resolve(field))
                    else:
                        fields[name] = deepcopy(field)
            elif key == "required":
                result[key] = sorted(set(result.get(key, [])) | set(value))
            elif key == "enum" and key in result:
                result[key] = [item for item in result[key] if item in value]
            else:
                result[key] = deepcopy(value)
        return result

    def predicate(value: Schema) -> tuple[list[str], Any] | None:
        properties = value.get("properties", {})
        if len(properties) != 1:
            return None
        name, field = next(iter(properties.items()))
        if "const" in field:
            return [name], field["const"]
        child = predicate(field)
        return None if child is None else ([name, *child[0]], child[1])

    def expand(value: Schema, trail: frozenset[str] = frozenset()) -> list[Schema]:
        reference = value.get("$ref")
        if reference:
            if reference in trail:
                return [value]
            return expand(resolve(value), trail | {reference})
        common = {
            key: deepcopy(item)
            for key, item in value.items()
            if key not in {"allOf", "anyOf", "oneOf", "not"}
        }
        variants = [common]
        for clause in value.get("allOf", []):
            condition = predicate(clause["if"]) if "if" in clause else None
            branches = None
            if condition is not None:
                path, literal = condition
                field = value
                for name in path:
                    field = resolve(field)
                    if name not in field.get("required", []):
                        break
                    field = field.get("properties", {}).get(name, {})
                else:
                    field = resolve(field)
                    domain = (
                        [False, True] if field.get("type") == "boolean" else field.get("enum", [])
                    )
                    if literal in domain and len(domain) > 1:
                        branches = []
                        for values, constraint in [
                            ([literal], clause.get("then", {})),
                            ([item for item in domain if item != literal], clause.get("else", {})),
                        ]:
                            guard: Schema = {"enum": values}
                            for name in reversed(path):
                                guard = {
                                    "type": "object",
                                    "required": [name],
                                    "properties": {name: guard},
                                }
                            branches.extend(expand({"allOf": [guard, constraint]}, trail))
            if branches is None:
                branches = expand(clause, trail)
            variants = [merge(left, right) for left, right in product(variants, branches)]
        for keyword in ("oneOf", "anyOf"):
            if keyword in value:
                branches = [item for branch in value[keyword] for item in expand(branch, trail)]
                variants = [merge(left, right) for left, right in product(variants, branches)]
        negated = value.get("not", {})
        forbidden = [
            branch["required"][0]
            for branch in negated.get("anyOf", [])
            if list(branch) == ["required"] and len(branch["required"]) == 1
        ]
        if list(negated) == ["required"]:
            # not(required a,b) 是至少缺少一个，不能把两个字段都禁止。
            variants = [
                merge(item, {"properties": {name: False}})
                for item in variants
                for name in negated["required"]
            ]
        elif forbidden:
            variants = [
                merge(item, {"properties": dict.fromkeys(forbidden, False)}) for item in variants
            ]
        return variants

    def field_type(value: Any, name: str) -> Any:
        if not isinstance(value, dict) or "$ref" in value:
            return value
        if value.get("properties") or any(key in value for key in ("allOf", "anyOf", "oneOf")):
            name = "_" + name
            emit(name, value)
            return {"$ref": f"#/components/schemas/{name}"}
        result = deepcopy(value)
        if "items" in result:
            result["items"] = field_type(result["items"], name + "Item")
        return result

    def emit(name: str, value: Schema) -> None:
        variants = expand(value)
        # 条件分支先与共同字段相交，再命名嵌套 TypedDict，避免丢失 required/false/zero。
        if len(variants) > 1:
            names = []
            for index, variant in enumerate(variants, 1):
                child = f"{name}Variant{index}"
                emit(child, variant)
                names.append({"$ref": f"#/components/schemas/{child}"})
            output[name] = {"anyOf": names}
            return
        result = variants[0]
        for field, schema in list(result.get("properties", {}).items()):
            suffix = "".join(part[:1].upper() + part[1:] for part in field.split("_"))
            result["properties"][field] = field_type(schema, name + suffix)
        if "items" in result:
            result["items"] = field_type(result["items"], name + "Item")
        output[name] = result

    for name, schema in schemas.items():
        emit(name, schema)
    return output
