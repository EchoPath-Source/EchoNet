from __future__ import annotations

import json
from pathlib import Path

import pytest

from echonet.cli import main
from echonet.ingestion import ingest_file, ingest_payload
from echonet.validation import SchemaValidationError, validate_payload

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_DIR = ROOT / "examples"


def load_example(name: str) -> dict:
    with (EXAMPLE_DIR / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_ingest_memory_example() -> None:
    event = ingest_file(EXAMPLE_DIR / "memory_layer_ingest_example.json")
    assert event.schema_name == "memory"
    assert event.event_type == "memory.ingest"
    assert event.domain == "MemoryLayer"
    assert event.source_system == "memory_layer"
    assert event.privacy_classification == "public_safe"


def test_ingest_route_example() -> None:
    event = ingest_file(EXAMPLE_DIR / "navigator_route_event_example.json")
    assert event.schema_name == "navigator"
    assert event.event_type == "route.telemetry"
    assert event.domain == "RiverPaths"
    assert event.confidence == 0.86


def test_ingest_aethernode_example() -> None:
    event = ingest_file(EXAMPLE_DIR / "aethernode_cluster_event_example.json")
    assert event.schema_name == "aethernode"
    assert event.event_type == "cluster.coherence"
    assert event.domain == "AetherNode"
    assert event.eta_proxy == 0.41


def test_ingest_handoff_example() -> None:
    event = ingest_file(EXAMPLE_DIR / "echonet_echochain_handoff_example.json")
    assert event.schema_name == "handoff"
    assert event.event_type == "sealed.handoff"
    assert event.domain == "EchoNet"
    assert event.source_system == "echonet"
    assert event.candidate_ping == "whisper"
    assert event.confidence == 0.86


def test_validate_payload_force_schema_rejects_wrong_adapter() -> None:
    route_packet = load_example("navigator_route_event_example.json")
    with pytest.raises(SchemaValidationError):
        validate_payload(route_packet, schema_name="memory")


def test_ingest_payload_reports_validation_error() -> None:
    packet = load_example("memory_layer_ingest_example.json")
    packet["privacy"]["identity_mode"] = "account_hash"
    with pytest.raises(SchemaValidationError):
        ingest_payload(packet)


def test_cli_validate_examples(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["validate", str(EXAMPLE_DIR)])
    assert code == 0
    captured = capsys.readouterr()
    assert "valid" in captured.out


def test_cli_classify_example(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["classify", str(EXAMPLE_DIR / "echonet_echochain_handoff_example.json")])
    assert code == 0
    captured = capsys.readouterr()
    assert '"candidate_ping": "whisper"' in captured.out
    assert '"schema_name": "handoff"' in captured.out
