# Memory Layer Ingestion

EchoNet receives memory events from the EchoPath Memory Layer without owning the Memory Lite runtime.

## Purpose

The Memory Layer can emit public-safe telemetry when anchors, zones, thresholds, event histories, or ledger-export candidates change. EchoNet normalizes those signals so downstream dashboards, route diagnostics, and sealed-event systems can reason about memory without importing private runtime internals.

## Inbound examples

- Anchor created, updated, or decayed.
- Zone threshold crossed.
- NPC/agent response triggered by local memory.
- Danger/safe-route memory score changed.
- Memory Ledger Export candidate generated.
- Public demo session summary emitted.

## Payload shape

```json
{
  "memory_event_type": "anchor.updated",
  "anchor_id": "anchor_living_room_hash",
  "zone_id": "zone_hallway_hash",
  "channel": "danger|presence|hiding|sound|safe|route|total",
  "delta": 0.18,
  "threshold_before": "watch",
  "threshold_after": "investigate",
  "event_count_window": 7,
  "ledger_export_candidate": true
}
```

## Boundary

EchoNet may store event summaries, channel scores, hashed anchor/zone IDs, and threshold transitions. EchoNet should not store raw player/user behavior logs, private room maps, full event histories, or Memory Lite implementation state unless explicitly marked internal/restricted.

## Downstream uses

- Coherence-aware route weighting.
- Public demo proof summaries.
- Memory-driven sealed-event candidates.
- EchoChain topology/persistence features through projected `eta_proxy`, not raw private memory logs.
