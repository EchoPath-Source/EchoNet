# Minimal Ingestion Library

The first EchoNet runtime layer is intentionally small: validate an event packet, select the correct schema, and emit a normalized routing summary.

This is not a server, database, dashboard, EchoChain scorer, Memory Lite runtime, Navigator implementation, or Q-RRG/kernel implementation.

## Install locally

```bash
pip install -e .[dev]
```

## Validate examples

```bash
echonet validate examples/
```

You can also force a schema:

```bash
echonet validate examples/memory_layer_ingest_example.json --schema memory
```

## Classify packets

```bash
echonet classify examples/aethernode_cluster_event_example.json
```

Example output:

```json
{
  "candidate_ping": null,
  "confidence": 0.86,
  "domain": "AetherNode",
  "eta_proxy": 0.41,
  "event_id": "evt_cluster_seed42_0001",
  "event_type": "cluster.coherence",
  "privacy_classification": "internal",
  "schema_name": "aethernode",
  "seal_mode": "local",
  "source_system": "aethernode"
}
```

## Ingest packets

```bash
echonet ingest examples/echonet_echochain_handoff_example.json
```

For now, `ingest` validates and emits a normalized routing summary. Persistence, queues, HTTP endpoints, and dashboards belong in later PRs.

## Python API

```python
from echonet import ingest_file, validate_payload

summary = ingest_file("examples/memory_layer_ingest_example.json")
print(summary.to_dict())
```

## Schema routing

The library automatically chooses the most specific schema:

| Packet | Schema key |
|---|---|
| `memory.ingest` | `memory` |
| `route.telemetry` | `navigator` |
| `navigator.decision` | `navigator` |
| `aethernode.telemetry` | `aethernode` |
| `cluster.coherence` | `aethernode` |
| `echonet.echochain_handoff.v0.1` | `handoff` |
| unknown generic EchoNet event | `echonet` |

## Validation posture

The library inherits the tightened v0.1 contract rules:

- public-safe events must be anonymous and retain no raw payload;
- adapter-specific events must match their source system, domain, and event type;
- EchoChain handoff packets are privacy projections, not raw telemetry dumps;
- `candidate_ping: fold` requires `seal_mode: council`;
- nested handoff objects reject unknown fields.
