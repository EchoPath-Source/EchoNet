"""Minimal EchoNet ingestion primitives.

This module validates packets and returns a normalized ingestion summary. It does not persist events,
run a server, compute Q-RRG/kernel internals, or perform EchoChain scoring.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .validation import validate_payload


@dataclass(frozen=True)
class IngestedEvent:
    event_id: str
    schema_name: str
    domain: str
    event_type: str
    source_system: str
    seal_mode: str | None
    privacy_classification: str | None
    eta_proxy: float | None
    confidence: float | None
    candidate_ping: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _coherence_confidence(payload: dict) -> float | None:
    coherence = payload.get("coherence")
    if isinstance(coherence, dict):
        confidence = coherence.get("confidence")
        return confidence if isinstance(confidence, (int, float)) else None
    return None


def _handoff_confidence(payload: dict) -> float | None:
    scoring_inputs = payload.get("scoring_inputs")
    if isinstance(scoring_inputs, dict):
        confidence = scoring_inputs.get("confidence")
        return confidence if isinstance(confidence, (int, float)) else None
    return None


def classify_event(payload: dict) -> dict[str, Any]:
    """Return routing metadata for a valid EchoNet or handoff packet."""
    schema_name = validate_payload(payload)
    if schema_name == "handoff":
        return {
            "schema_name": schema_name,
            "event_id": payload["event_id"],
            "domain": payload["context"]["domain"],
            "event_type": "sealed.handoff",
            "source_system": "echonet",
            "seal_mode": payload["seal_mode"],
            "privacy_classification": "projected",
            "eta_proxy": payload.get("eta_proxy"),
            "confidence": _handoff_confidence(payload),
            "candidate_ping": payload.get("candidate_ping"),
        }

    source = payload.get("source", {})
    privacy = payload.get("privacy", {})
    return {
        "schema_name": schema_name,
        "event_id": payload["event_id"],
        "domain": payload["domain"],
        "event_type": payload["event_type"],
        "source_system": source.get("system"),
        "seal_mode": payload.get("seal_mode"),
        "privacy_classification": privacy.get("classification"),
        "eta_proxy": payload.get("eta_proxy"),
        "confidence": _coherence_confidence(payload),
        "candidate_ping": None,
    }


def ingest_payload(payload: dict) -> IngestedEvent:
    """Validate and summarize an EchoNet payload."""
    return IngestedEvent(**classify_event(payload))


def ingest_file(path: str | Path) -> IngestedEvent:
    """Validate and summarize an EchoNet JSON file."""
    json_path = Path(path)
    with json_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return ingest_payload(payload)
