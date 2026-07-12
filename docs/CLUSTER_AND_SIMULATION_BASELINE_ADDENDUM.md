# Cluster and Simulation Baseline Addendum

**Status:** addendum to `docs/CLUSTER_AND_SIMULATION_BASELINE.md`  
**Scope:** extended coherence propagation references from the Sequence / Echo Labs cross-thread sweep  
**Claim level:** simulation-derived contract reference, not empirical deployment proof

## Purpose

This addendum extends the current seed42 and 50-seed Monte Carlo baseline with the coherence-ridge and hop-decay parameters needed for future EchoNet fixtures, dashboard mock streams, and adapter tests.

The main baseline remains the canonical summary of the first repo scaffold. This file preserves additional simulation-envelope parameters without rewriting historical baseline text.

## Extended coherence propagation references

`docs/COHERENCE_PROPAGATION_ENVELOPE.md` preserves the current simulation-derived propagation envelope for cluster-window fixtures and dashboard mock-stream planning.

Current reference values from the extended simulation summaries:

- cluster size target: 4-5 nodes;
- useful hop limit: 3-5 hops;
- pulse duration `tau`: about 20;
- resonance frequency `omega`: about 0.05;
- multi-field coupling `r`: about 0.4;
- detuning tolerance `delta_omega`: less than or equal to 0.03;
- feedback gain `g`: 0.5-0.7, with about 0.6 as the working center;
- simulation noise sweeps: 0-0.30.

Use these values as schema/dashboard coverage targets, not as hard engineering limits or empirical field claims.

## Baseline classes

EchoNet should distinguish the following data classes in docs, fixtures, dashboards, and handoff packets:

| Class | Meaning | Claim posture |
|---|---|---|
| `seed42_reference` | Single controlled simulation reference run. | Contract/reference only. |
| `monte_carlo_reference` | Multi-seed simulation summary. | Reproducibility support, not deployment proof. |
| `propagation_envelope` | Higher-level coherence-ridge / hop-decay envelope. | Simulation-derived operating reference. |
| `mock_stream` | Synthetic stream for dashboards and adapter tests. | Developer fixture only. |
| `field_telemetry` | Future real AetherNode / deployment telemetry. | Requires privacy review, controls, and provenance. |

## Repository implication

EchoNet should preserve simulation outputs as contract references, not as hard scientific claims. Schemas should support metrics used in the baseline while allowing future implementations to replace mock/simulated metrics with real AetherNode telemetry.
