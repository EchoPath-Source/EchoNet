# EchoNet Role

EchoNet is the coherence/telemetry fabric and event-ingestion layer across the Echo ecosystem.

## Canonical role

EchoNet receives normalized events from product surfaces, adapters, demos, runtime systems, AetherNodes, and research pilots. It converts those inputs into privacy-aware telemetry packets and coherence features that can be used by dashboards, memory systems, route diagnostics, sealed ledgers, and later governance/reward layers.

## What EchoNet owns

- Event ingestion contracts.
- Cross-system telemetry normalization.
- Coherence feature packaging: `R`, spectral entropy, concurrence proxies, anomaly score, disturbance, churn, confidence, and `eta_proxy`.
- AetherNode and cluster telemetry adapters.
- Memory Layer ingestion adapters.
- Navigator/RiverPaths route telemetry adapters.
- EchoNet -> EchoChain sealed-event handoff projection.
- Public/private boundary rules for EchoNet payloads.

## What EchoNet does not own

- EchoGenesis construct definitions and ecosystem architecture.
- Q-RRG/kernel route computation.
- EchoPath Memory Lite runtime behavior.
- RiverPaths product demos or frontend pages.
- EchoChain scoring implementation or wallet economics.
- SoCT proof claims or consciousness-collapse claims.

## Relationship to adjacent systems

| System | Relationship |
|---|---|
| EchoGenesis | Defines architecture spine, construct placement, WOSP, and cross-construct governance. EchoNet implements telemetry contracts referenced by the spine. |
| AetherNodes | Physical/edge sensing nodes that produce QRNG, EMF, magnetic, temp, vibration, acoustic, and environment covariate streams. |
| EchoPath Memory Layer | Emits memory events and threshold transitions to EchoNet; remains owner of memory runtime. |
| RiverPaths / Navigator | Emit route/demo telemetry; remain owners of pathing, planner, route-card, and decision-support behavior. |
| EchoChain / Reflection Ledger | Receives sealed, privacy-projected events from EchoNet; remains owner of scoring, pings, and reward/governance routing. |

## Working principle

EchoNet measures and maps. EchoGenesis defines. EchoPath navigates. Memory Layer remembers local history. EchoChain routes value and governance. Reflection Ledger archives meaning. EchoNet should make these handoffs possible without becoming any of those systems.
