# Dashboard Mock Streams

**Status:** implementation-planning note  
**Scope:** local event-store stubs, mock streams, fixture-driven dashboards, and public-safe telemetry demos  
**Boundary:** mock streams are development artifacts, not live AetherNode measurements.

## Purpose

EchoNet needs dashboard-ready mock streams before real deployments are available. These streams should exercise the ingestion library, fixtures, schemas, and future local event store without implying that simulated data is measured field telemetry.

## Stream families

| Stream | Source adapter | Purpose |
|---|---|---|
| Single node sensor window | AetherNode | Show QRNG / EMF / environmental / acoustic / vibration summaries for one hashed node. |
| Cluster coherence window | AetherNode cluster | Show `R`, spectral entropy, concurrence proxy, anomaly score, and `eta_proxy`. |
| Coherence propagation window | AetherNode cluster-chain | Show hop-index behavior, decay posture, pulse timing, frequency ridge, coupling, and detuning. |
| Route telemetry window | RiverPaths / EchoPath / Navigator | Show route confidence, fallback mode, path telemetry, and route-card IDs. |
| Memory ingest window | Memory Layer | Show anchor, zone, threshold, and ledger-export candidate activity. |
| Handoff candidate stream | EchoNet -> EchoChain | Show public-safe projections ready for sealed-event handoff. |
| Demo analytics stream | Website / public demos | Show safe usage and proof events without raw private content. |

## Development sequence

```text
fixtures -> ingestion summaries -> local mock stream generator -> local event-store stub -> dashboard-ready JSON -> UI prototype
```

The first mock streams should be generated from committed fixtures. Later streams can be generated synthetically from bounded simulation presets.

## Public-safe projection rules

Mock streams should follow the same public/private boundary rules as real packets:

- use hashed node, cluster, route, user, and event identifiers;
- store aggregate windows instead of raw sensitive streams;
- preserve `claim_level` for simulation-derived or synthetic rows;
- avoid raw location trails unless explicitly authorized and redacted;
- do not include private sensor payloads in public examples;
- do not infer identity, consciousness, spiritual state, or psychological condition.

## Suggested stream payload shapes

### Single node sensor window

```text
source.system = aethernode
domain = AetherNode
event_type = aethernode.telemetry
node_event_type = sensor.window
node_id_hash
cluster_id
window_start
window_end
sensor_profile
qrng_entropy
emf_uT
temperature_c
vibration_rms
acoustic_rms
local_coherence_raw
edge_anomaly_score
claim_level
```

### Cluster coherence window

```text
source.system = aethernode
domain = AetherNode
event_type = cluster.coherence
cluster_event_type = coherence.window
cluster_id
node_count
window_start
window_end
r_value
spectral_entropy
concurrence_proxy
anomaly_flag
anomaly_score
eta_proxy
claim_level
```

### Coherence propagation window

```text
source.system = aethernode
domain = AetherNode
event_type = cluster.coherence
cluster_event_type = coherence.propagation_window
cluster_id
node_count
hop_index
pulse_tau
omega
field_coupling_r
detuning_delta
feedback_gain
noise_level
r_value
spectral_entropy
concurrence_proxy
eta_proxy
anomaly_score
simulation_label
claim_level = simulation_reference
```

## Dashboard panels

Initial panels should be simple and explainable:

1. **Cluster health** — `R`, entropy, eta, anomaly score.
2. **Propagation** — hop index, decay, ridge timing, detuning.
3. **Route overlay support** — route confidence and fallback events.
4. **Memory / ledger candidates** — memory thresholds and handoff candidates.
5. **Boundary / claim labels** — simulation, mock, demo, or measured deployment.

## Acceptance criteria for first dashboard-ready pass

- All mock rows validate through the ingestion path.
- Every row has a clear `claim_level` or equivalent label.
- Public-safe rows use anonymous / hashed identifiers.
- No dashboard panel labels simulated data as measured telemetry.
- Route, memory, AetherNode, and handoff streams can be displayed together without requiring private kernel internals.

## Next implementation steps

1. Add a small mock-stream generator after fixture schemas are stable.
2. Add a local event-store stub with append/read/query by event type.
3. Add a dashboard JSON export command.
4. Add sample dashboard snapshots generated only from committed public-safe fixtures.
