#!/usr/bin/env python3
"""Validate EchoNet schemas and examples.

This script intentionally stays dependency-light so it can run locally and in CI.
"""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = ROOT / "examples"

SCHEMA_FILES = {
    "echonet": SCHEMA_DIR / "echonet_event.schema.json",
    "memory": SCHEMA_DIR / "memory_ingest_event.schema.json",
    "navigator": SCHEMA_DIR / "navigator_telemetry_event.schema.json",
    "aethernode": SCHEMA_DIR / "aethernode_telemetry_event.schema.json",
    "handoff": SCHEMA_DIR / "echonet_echochain_handoff.schema.json",
}

EXAMPLE_SCHEMA_MAP = {
    "memory_layer_ingest_example.json": "memory",
    "navigator_route_event_example.json": "navigator",
    "aethernode_cluster_event_example.json": "aethernode",
    "echonet_echochain_handoff_example.json": "handoff",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def schema_registry() -> tuple[dict[str, dict], Registry]:
    schemas = {name: load_json(path) for name, path in SCHEMA_FILES.items()}
    resources = []
    for name, schema in schemas.items():
        resources.append((schema["$id"], Resource.from_contents(schema)))
        resources.append((f"./{SCHEMA_FILES[name].name}", Resource.from_contents(schema)))
    return schemas, Registry().with_resources(resources)


def validate_instance(schema: dict, instance: dict, registry: Registry) -> None:
    validator = Draft202012Validator(schema, registry=registry)
    errors = sorted(validator.iter_errors(instance), key=lambda err: list(err.path))
    if errors:
        rendered = "\n".join(f"- {'/'.join(map(str, error.path)) or '<root>'}: {error.message}" for error in errors)
        raise AssertionError(rendered)


def main() -> None:
    schemas, registry = schema_registry()
    for schema in schemas.values():
        Draft202012Validator.check_schema(schema)

    for example_name, schema_name in EXAMPLE_SCHEMA_MAP.items():
        instance = load_json(EXAMPLE_DIR / example_name)
        validate_instance(schemas[schema_name], instance, registry)
        print(f"validated {example_name} against {schema_name}")


if __name__ == "__main__":
    main()
