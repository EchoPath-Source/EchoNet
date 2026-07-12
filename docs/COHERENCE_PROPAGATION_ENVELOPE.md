# Coherence Propagation Envelope

**Status:** simulation-derived reference envelope  
**Scope:** EchoNet / AetherNode coherence telemetry, cluster-window fixtures, and dashboard mock-stream planning  
**Claim level:** internal simulation reference; not empirical proof of consciousness, identity, or physical field causation

## Purpose

This document preserves the current coherence-propagation operating envelope derived from internal Echo Labs / SoCT / EchoNet simulation summaries. It is intended to guide EchoNet schemas, fixtures, dashboards, and adapter tests without promoting the simulation outputs into empirical claims.

EchoNet should use this envelope as a reference for what metrics and ranges must be representable:

- cluster-level order parameter `R`;
- spectral entropy;
- concurrence or coherence proxies;
- anomaly windows;
- hop-index decay;
- pulse-window and resonance-ridge metadata;
- route / field / eta proxy handoff fields.

## Reference envelope

| Parameter | Current reference range | EchoNet interpretation |
|---|---:|---|
| Cluster size | 4-5 nodes | Preferred resonant cell size for simulated cluster windows. |
| Hop limit | 3-5 hops | Useful coherence propagation range before decay dominates. |
| Pulse duration `tau` | about 20 | Reference pulse window for resonance-ridge fixtures. |
| Frequency `omega` | about 0.05 | Reference resonance-ridge frequency from simulation summaries. |
| Field coupling `r` | about 0.4 | Multi-field reinforcement reference point. |
| Detuning tolerance `delta_omega` | <= 0.03 | Suggested threshold for stable simulated coherence windows. |
| Feedback gain `g` | 0.5-0.7 | Reference stabilization band; about 0.6 is the central working value. |
| Noise | 0-0.30 in simulation sweeps | Use as a declared simulation/control parameter, not as a real-world sensor truth. |

## Metric families to preserve

EchoNet event packets and dashboard mock streams should be able to preserve the following fields when available:

```text
cluster_id
node_count
window_start
window_end
hop_index
r_value
spectral_entropy
concurrence_proxy
eta_proxy
pulse_tau
omega
field_coupling_r
detuning_delta
feedback_gain
noise_level
anomaly_flag
anomaly_score
simulation_label
claim_level
```

These fields do not all need to be required in the base event schema. Adapter-specific packets may expose them as optional metrics, nested metadata, or dashboard-ready projections.

## Interpretation rules

1. Treat this envelope as a **simulation reference**, not a deployed AetherNode measurement envelope.
2. Use it to validate that schemas and dashboards can represent coherence windows, not to claim real-world confirmation.
3. Keep raw sensor streams separate from public-safe projections.
4. Use hashed node and cluster identifiers in fixtures and public examples.
5. Preserve `claim_level` or equivalent metadata whenever simulation-derived rows are promoted into examples, dashboards, or reports.

## Relationship to existing baseline

This document extends `docs/CLUSTER_AND_SIMULATION_BASELINE.md`.

The existing baseline preserves:

- the 10-node / two-cluster seed42 setup;
- Kuramoto-style synchronization assumptions;
- core metrics such as `R`, spectral entropy, concurrence proxy, disturbance, anomaly flags, and path telemetry deltas;
- the 50-seed Monte Carlo summary.

This propagation envelope adds the higher-level coherence-ridge and hop-decay parameters needed for future fixtures and dashboards.

## Boundary

EchoNet may ingest and aggregate coherence telemetry. It should not claim that these values prove consciousness, identity, spiritual state, or physical field causation. Research-facing experiments should remain labeled, controlled, and reproducible, with baseline/sham comparisons and privacy review before any stronger claim is made.
