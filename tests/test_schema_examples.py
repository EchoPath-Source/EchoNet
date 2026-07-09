from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = ROOT / "examples"

SCHEMA_PATHS = {
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


@pytest.fixture(scope="session")
def schemas() -> dict[str, dict]:
    return {name: load_json(path) for name, path in SCHEMA_PATHS.items()}


@pytest.fixture(scope="session")
def registry(schemas: dict[str, dict]) -> Registry:
    resources = []
    for name, schema in schemas.items():
        resources.append((schema["$id"], Resource.from_contents(schema)))
        resources.append((f"./{SCHEMA_PATHS[name].name}", Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def validate(schema: dict, instance: dict, registry: Registry) -> None:
    Draft202012Validator(schema, registry=registry).validate(instance)


@pytest.mark.parametrize("schema_name", SCHEMA_PATHS.keys())
def test_schema_is_valid(schema_name: str, schemas: dict[str, dict]) -> None:
    Draft202012Validator.check_schema(schemas[schema_name])


@pytest.mark.parametrize("example_name,schema_name", EXAMPLE_SCHEMA_MAP.items())
def test_examples_validate(example_name: str, schema_name: str, schemas: dict[str, dict], registry: Registry) -> None:
    validate(schemas[schema_name], load_json(EXAMPLE_DIR / example_name), registry)


def test_memory_schema_rejects_route_packet(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "navigator_route_event_example.json")
    with pytest.raises(ValidationError):
        validate(schemas["memory"], packet, registry)


def test_navigator_schema_accepts_echopath_source_system(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "navigator_route_event_example.json")
    packet["source"]["system"] = "echopath"
    packet["domain"] = "EchoPath"
    validate(schemas["navigator"], packet, registry)


def test_aethernode_schema_rejects_memory_packet(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "memory_layer_ingest_example.json")
    with pytest.raises(ValidationError):
        validate(schemas["aethernode"], packet, registry)


def test_fold_ping_requires_council_seal(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "echonet_echochain_handoff_example.json")
    packet["candidate_ping"] = "fold"
    packet["seal_mode"] = "ledger"
    with pytest.raises(ValidationError):
        validate(schemas["handoff"], packet, registry)
    packet["seal_mode"] = "council"
    validate(schemas["handoff"], packet, registry)


def test_handoff_rejects_extra_privacy_projection_fields(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "echonet_echochain_handoff_example.json")
    packet["privacy_projection"]["raw_private_payload"] = {"should": "fail"}
    with pytest.raises(ValidationError):
        validate(schemas["handoff"], packet, registry)


def test_handoff_accepts_confidence_scoring_input(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "echonet_echochain_handoff_example.json")
    packet["scoring_inputs"]["confidence"] = 0.91
    validate(schemas["handoff"], packet, registry)


def test_public_safe_requires_anonymous_no_raw_retention(schemas: dict[str, dict], registry: Registry) -> None:
    packet = load_json(EXAMPLE_DIR / "memory_layer_ingest_example.json")
    validate(schemas["echonet"], packet, registry)

    identity_retaining = copy.deepcopy(packet)
    identity_retaining["privacy"]["identity_mode"] = "account_hash"
    with pytest.raises(ValidationError):
        validate(schemas["echonet"], identity_retaining, registry)

    raw_retaining = copy.deepcopy(packet)
    raw_retaining["privacy"]["raw_payload_retention"] = "short_window"
    with pytest.raises(ValidationError):
        validate(schemas["echonet"], raw_retaining, registry)
