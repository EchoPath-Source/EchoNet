from __future__ import annotations

import json
from pathlib import Path

from echonet.ingestion import ingest_file
from echonet.validation import validate_payload

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_MANIFEST = ROOT / "fixtures" / "manifest.json"


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def manifest_entries() -> list[dict]:
    return load_json(FIXTURE_MANIFEST)["fixtures"]


def test_fixture_manifest_paths_exist() -> None:
    for entry in manifest_entries():
        assert (ROOT / entry["path"]).exists(), entry["path"]


def test_fixture_manifest_entries_validate_and_classify() -> None:
    for entry in manifest_entries():
        path = ROOT / entry["path"]
        payload = load_json(path)
        schema_name = validate_payload(payload)
        assert schema_name == entry["expected_schema"]

        summary = ingest_file(path)
        assert summary.schema_name == entry["expected_schema"]
        assert summary.domain == entry["domain"]
        assert summary.event_type == entry["event_type"]


def test_public_safe_fixtures_have_no_raw_retention() -> None:
    for entry in manifest_entries():
        payload = load_json(ROOT / entry["path"])
        privacy = payload.get("privacy")
        if privacy and privacy.get("classification") == "public_safe":
            assert privacy["raw_payload_retention"] == "none"
            assert privacy["identity_mode"] == "anonymous"


def test_handoff_fixtures_are_privacy_projections() -> None:
    for entry in manifest_entries():
        if entry["expected_schema"] != "handoff":
            continue
        payload = load_json(ROOT / entry["path"])
        assert payload["privacy_projection"]["raw_content_stored"] is False
        assert "raw_payload" not in payload
        assert "payload" not in payload


def test_fold_fixture_uses_council_seal() -> None:
    fold_fixture = load_json(ROOT / "fixtures/echochain/fold_ping_council_handoff.json")
    assert fold_fixture["candidate_ping"] == "fold"
    assert fold_fixture["seal_mode"] == "council"
