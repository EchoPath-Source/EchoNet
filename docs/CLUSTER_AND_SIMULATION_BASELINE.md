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

## Repository implication

EchoNet should preserve the simulation outputs as contract references, not as hard scientific claims. Schemas should support metrics used in the baseline while allowing future implementations to replace mock/simulated metrics with real AetherNode telemetry.
