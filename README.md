# EchoNet

EchoNet is the telemetry and coherence-mapping fabric for the Echo ecosystem. It receives normalized events from product surfaces, adapters, demos, AetherNodes, and future runtime systems, then prepares them for analysis, routing, memory, coordination, and sealed-event handoff.

EchoNet is not the product website, not the Memory Lite runtime, not the private Q-RRG/kernel implementation, not the EchoGenesis architecture spine, and not the full EchoChain dev project. It is the ecosystem ingestion layer that lets those systems exchange public-safe, privacy-aware telemetry without duplicating ownership.

## Core responsibilities

- Normalize event packets from EchoPath Memory Layer, RiverPaths, Navigator, website demos, AetherNodes, and research runs.
- Translate raw telemetry into coherence features such as order parameter `R`, spectral entropy, concurrence proxies, anomaly windows, and `eta_proxy` signals.
- Preserve public/private boundaries by storing projections and summaries rather than raw sensitive content whenever possible.
- Prepare event packets for downstream memory, route diagnostics, dashboards, and EchoChain/Reflection Ledger handoff.
- Keep EchoNet-specific docs and schemas aligned with EchoGenesis, WOSP, EchoPath Memory Layer, RiverPaths/Navigator, and EchoChain contracts.

## Initial adapters

| Adapter | Inbound event | EchoNet role |
|---|---|---|
| Memory Layer -> EchoNet | `memory.ingest` | Normalize anchors, zones, memory thresholds, local memory events, and ledger-export candidates. |
| RiverPaths -> EchoNet | `route.telemetry` | Capture route/demo outcomes, fallback modes, route-card IDs, and route confidence telemetry. |
| Navigator -> EchoNet | `navigator.decision` | Capture decision-support context without owning Navigator reasoning or UI. |
| AetherNode -> EchoNet | `aethernode.telemetry` / `cluster.coherence` | Ingest QRNG, EMF, environmental, acoustic, vibration, and cluster coherence metrics. |
| EchoNet -> EchoChain | `sealed.handoff` | Project validated events into sealed, privacy-aware packets for Reflection Ledger and topology scoring. |
| Website/demo -> EchoNet | `demo.analytics` | Capture public-safe demo usage and proof events without product-site ownership. |

## Repository map

```text
docs/
  ECHONET_ROLE.md
  EVENT_INGESTION_CONTRACT.md
  MEMORY_LAYER_INGESTION.md
  NAVIGATOR_TELEMETRY.md
  AETHERNODE_TELEMETRY.md
  ECHONET_ECHOCHAIN_HANDOFF.md
  CLUSTER_AND_SIMULATION_BASELINE.md
  PUBLIC_PRIVATE_BOUNDARY.md
  SOURCE_CROSSWALK.md
  INGESTION_LIBRARY.md
fixtures/
  README.md
  manifest.json
  memory_layer/
  navigator/
  aethernode/
  echochain/
schemas/
  echonet_event.schema.json
  memory_ingest_event.schema.json
  navigator_telemetry_event.schema.json
  aethernode_telemetry_event.schema.json
  echonet_echochain_handoff.schema.json
examples/
  memory_layer_ingest_example.json
  navigator_route_event_example.json
  aethernode_cluster_event_example.json
  echonet_echochain_handoff_example.json
scripts/
  validate_examples.py
src/echonet/
  cli.py
  ingestion.py
  schemas.py
  validation.py
tests/
  test_schema_examples.py
  test_ingestion_library.py
  test_fixture_catalog.py
```

## Validation and ingestion CLI

Install the package in editable development mode:

```bash
pip install -e .[dev]
```

Validate schemas, examples, and fixtures:

```bash
python scripts/validate_examples.py
echonet validate fixtures/
pytest
```

Use the CLI:

```bash
echonet validate examples/
echonet classify examples/aethernode_cluster_event_example.json
echonet ingest examples/echonet_echochain_handoff_example.json
```

CI runs validation checks on every pull request and on pushes to `main`.

## Design constraints

1. Do not duplicate EchoGenesis architecture definitions. EchoGenesis remains the construct spine.
2. Do not copy Memory Lite runtime internals. EchoNet receives events; it does not own memory execution.
3. Do not copy private Q-RRG/kernel internals. EchoNet can preserve route IDs, tube IDs, and eta proxies without reimplementing kernel logic.
4. Do not overclaim research results. EchoNet telemetry can support experiments and anomaly detection; it does not prove consciousness or identity.
5. Do not expose private telemetry by default. Use hashed IDs, aggregates, projections, and sealed-event handoff.

## Current phase

This repository is initialized as a contract/documentation scaffold with executable schema validation, a minimal ingestion CLI, and a public-safe adapter fixture catalog. Implementation should continue with local event-store stubs and dashboard-ready mock streams.
