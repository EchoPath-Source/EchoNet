# Cluster and Simulation Baseline

This document captures the current EchoNet simulation and cluster assumptions that should inform the first repo scaffold.

## Cluster pattern

- Pilot topology: 10 nodes split into two 5-node clusters.
- Cluster size target: 4-5 nodes per resonant cell.
- Intra-cluster connectivity: dense/fully connected in the seed42 run.
- Inter-cluster connectivity: sparse random 50 percent in the seed42 run.
- Phase model: Kuramoto-style synchronization.
- Target behavior: maintain useful coherence without over-locking.
- Core metrics: order parameter `R`, spectral entropy, concurrence proxy, disturbance, anomaly flag, and path telemetry deltas.

## Seed42 run parameters

- `N`: 10
- `cluster_size`: 5
- `dt`: 0.1
- `t_max`: 100.0
- `seed`: 42
- `K_intra`: 0.8
- `K_inter`: 0.05
- `inter_sparsity`: 0.5
- anomaly node: 0
- anomaly window: 50.0-60.0 seconds
- frequency shift: 2.0

## Monte Carlo baseline

The 50-seed Monte Carlo summary reports:

- Hybrid path improvement: 6.5 percent before, during, and after anomaly.
- Zero failure rate for both A* and hybrid methods across all 50 trials.
- EchoNet anomaly detection mean around 0.76 seconds, with wide variance and a 95 percent CI up to 5 seconds.
- 5000 total data points analyzed across 50 seeds and 100 timesteps.

## Extended coherence propagation envelope

The extended simulation thread adds a separate reference envelope for coherence propagation and ridge-window behavior. Keep this as a simulation-derived planning reference, not as empirical proof.

See: `docs/COHERENCE_PROPAGATION_ENVELOPE.md`

Reference parameters preserved there include:

- cluster size target: 4-5 nodes;
- useful hop limit: 3-5 hops;
- pulse duration `tau` around 20;
- resonance-ridge frequency `omega` around 0.05;
- field coupling `r` around 0.4;
- detuning tolerance `delta_omega <= 0.03`;
- feedback gain `g` around 0.5-0.7;
- noise / detuning / hop-decay posture for fixtures and dashboard mock streams.

## Repository implication

EchoNet should preserve the simulation outputs as contract references, not as hard scientific claims. Schemas should support metrics used in the baseline while allowing future implementations to replace mock/simulated metrics with real AetherNode telemetry.

The current implementation path should remain:

```text
simulation references -> public-safe fixtures -> ingestion validation -> local mock streams -> dashboard-ready summaries -> measured deployment telemetry
```

Do not collapse those phases into one claim. A real AetherNode deployment can be compared against these references only after instrumentation, privacy review, and baseline/sham controls are defined.
