from __future__ import annotations

import json
from pathlib import Path

from echonet.schemas import schema_for_payload
from echonet.validation import validate_payload

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "ai_witness_dataset_example.json"


def load_example() -> dict:
    with EXAMPLE.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def test_ai_witness_payload_selects_dataset_schema() -> None:
    payload = load_example()
    assert schema_for_payload(payload) == "ai_witness"


def test_ai_witness_example_validates_without_explicit_schema() -> None:
    payload = load_example()
    assert validate_payload(payload) == "ai_witness"
