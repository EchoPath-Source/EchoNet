# Event Ingestion Contract

This document defines the first EchoNet ingestion contract. It is intentionally small enough to implement now and broad enough to support Memory Layer, RiverPaths, Navigator, AetherNode, website/demo, and EchoChain handoff events.

## Contract goals

- Every inbound event has a stable event ID, timestamp, source, domain, type, privacy classification, and payload.
- Every optional coherence feature is explicit and nullable.
- Raw sensitive payloads are not required for downstream analysis.
- All handoff candidates can later be sealed under `none`, `local`, `ledger`, or `council` modes.
- EchoChain-facing packets can be produced from projections rather than raw telemetry.

## Canonical packet

The canonical schema lives at `schemas/echonet_event.schema.json`.

```json
{
  "schema_version": "echonet.event.v0.1",
  "event_id": "evt_...",
  "timestamp": "2026-01-11T04:33:00Z",
  "source": {
    "system": "aethernode",
    "adapter": "aethernode_cluster_v0.1",
    "source_id": "cluster_alpha"
  },
  "domain": "AetherNode",
  "event_type": "cluster.coherence",
  "seal_mode": "local",
  "eta_proxy": 0.41,
  "coherence": {
    "r_value": 0.33,
    "spectral_entropy": 2.57,
    "concurrence_proxy": 0.41,
    "anomaly_score": 0.12,
    "anomaly_flag": false,
    "confidence": 0.86
  },
  "privacy": {
    "classification": "internal",
    "raw_payload_retention": "short_window",
    "identity_mode": "node_hash"
  },
  "payload": {}
}
```

## Event types

| Event type | Meaning |
|---|---|
| `memory.ingest` | Memory Layer anchor, zone, threshold, ledger export, or local-memory event. |
| `route.telemetry` | RiverPaths/EchoPath route telemetry, route outcome, fallback mode, path quality, or route-card event. |
| `navigator.decision` | Navigator decision-support event, route recommendation, context update, or operator interaction summary. |
| `aethernode.telemetry` | Single-node sensing packet from an AetherNode or simulated node. |
| `cluster.coherence` | Multi-node aggregate coherence/anomaly window. |
| `demo.analytics` | Public-safe website/demo event. |
| `sealed.handoff` | EchoNet projection prepared for EchoChain/Reflection Ledger. |
| `research.run` | Simulation or experiment summary packet. |

## Coherence fields

- `r_value`: Kuramoto-style phase order parameter or local proxy.
- `spectral_entropy`: entropy or disorder summary for the telemetry window.
- `concurrence_proxy`: SOC-inspired concurrence/coherence proxy where available.
- `anomaly_score`: normalized event-risk/anomaly estimate.
- `anomaly_flag`: boolean threshold crossing.
- `confidence`: data sufficiency and quality estimate.

## Seal modes

- `none`: stored as ordinary telemetry only.
- `local`: internally sealed by adapter/service; good for dev and low-risk telemetry.
- `ledger`: eligible for Reflection Ledger or EchoChain candidate processing.
- `council`: high-impact packet requiring WOSP/council-style review before policy, reward, or governance use.

## Validation rules

1. Reject events without `schema_version`, `event_id`, `timestamp`, `source`, `domain`, `event_type`, `privacy`, or `payload`.
2. Reject public events that include raw identity, raw location, raw conversation content, or raw sensor streams unless explicitly marked and approved.
3. Coherence metrics must be numeric or null; do not overload them with strings.
4. EchoChain handoff must use projected fields only and should not include raw private content.
5. Research claims must be marked as `research.run` and not presented as product telemetry proof.
