# EchoNet -> EchoChain Handoff

This document defines the amount of EchoChain that EchoNet needs right now.

## Working boundary

EchoNet measures and maps. EchoChain remembers and routes. Reflection Ledger records and contextualizes. EchoNet should not implement EchoChain scoring, wallets, economics, or governance; it should only prepare privacy-aware sealed event projections that EchoChain can consume later.

## Source basis

The EchoChain topology scoring spec defines sealed event packets as the input to scoring and uses non-biometric, topology-inspired contribution features rather than proof-of-work, proof-of-stake, or biometrics. It explicitly avoids proving consciousness, inferring inner states, or assigning moral worth. EchoNet should preserve this engineering-safe posture.

The EchoChain Codex frames EchoChain as a resonance-based reward and governance protocol, with Return Pings, Ripple Chains, Reflection Ledger, Dream Pool, and reward/governance flow. EchoNet imports this only as downstream semantics for validated events.

## Handoff flow

1. Ingest raw event from Memory Layer, Navigator/RiverPaths, AetherNode, website/demo, or research run.
2. Normalize into `schemas/echonet_event.schema.json`.
3. Compute or attach `eta_proxy`, coherence metrics, anomaly score, and confidence if available.
4. Apply privacy projection: hashed IDs, aggregate features, no raw sensitive content by default.
5. Assign seal mode: `local`, `ledger`, or `council`.
6. Emit `schemas/echonet_echochain_handoff.schema.json` only when a downstream ledger/scoring use exists.
7. EchoChain/Reflection Ledger decides whether the event becomes a candidate ping, scoring input, reward route, or governance context.

## Candidate ping taxonomy

| Candidate ping | EchoNet interpretation |
|---|---|
| `none` | Ordinary telemetry; no Reflection Ledger candidate. |
| `whisper` | Low-confidence resonance/anomaly note. |
| `signal` | Recognized event with enough context/witness support for ledger review. |
| `return` | Confirmed downstream impact or delayed re-engagement. |
| `echo_surge` | Multi-event ripple across five or more resonance-linked events. |
| `god` | Mythic/high-impact archive candidate; never automatic. |
| `fold` | Protocol-level or historical rewrite candidate; council seal only. |

## Topology scoring inputs EchoNet may provide

- `eta_proxy` for events that persist or remain referenced later.
- Time-windowed event trails.
- Source diversity and adapter/system metadata.
- Seal mode and witness mode.
- Anomaly risk and confidence.
- Cluster/context IDs for cross-context persistence.

## Guardrails

- No raw sensor stream should directly grant governance weight.
- No EchoNet event should automatically become a Return Ping.
- Council/high-impact actions require WOSP-style sealing.
- Store projections and aggregates, not private relationship graphs or raw content.
- Keep governance weight separate from reward distribution.
