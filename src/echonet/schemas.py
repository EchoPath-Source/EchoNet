"""Schema loading utilities for EchoNet."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"

SCHEMA_FILES = {
    "echonet": "echonet_event.schema.json",
    "memory": "memory_ingest_event.schema.json",
    "navigator": "navigator_telemetry_event.schema.json",
    "aethernode": "aethernode_telemetry_event.schema.json",
    "handoff": "echonet_echochain_handoff.schema.json",
}

EVENT_TYPE_SCHEMA = {
    "memory.ingest": "memory",
    "route.telemetry": "navigator",
    "navigator.decision": "navigator",
    "aethernode.telemetry": "aethernode",
    "cluster.coherence": "aethernode",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=1)
def load_schemas() -> dict[str, dict]:
    return {name: load_json(SCHEMA_DIR / filename) for name, filename in SCHEMA_FILES.items()}


@lru_cache(maxsize=1)
def schema_registry() -> Registry:
    resources = []
    for name, schema in load_schemas().items():
        filename = SCHEMA_FILES[name]
        resources.append((schema["$id"], Resource.from_contents(schema)))
        resources.append((f"./{filename}", Resource.from_contents(schema)))
    return Registry().with_resources(resources)


def schema_for_payload(payload: dict) -> str:
    """Return the best schema key for a payload.

    EchoChain handoff packets use their own schema_version. Other EchoNet events are routed by event_type.
    Unknown event types fall back to the canonical EchoNet event schema.
    """
    if payload.get("schema_version") == "echonet.echochain_handoff.v0.1":
        return "handoff"
    event_type = payload.get("event_type")
    return EVENT_TYPE_SCHEMA.get(event_type, "echonet")
