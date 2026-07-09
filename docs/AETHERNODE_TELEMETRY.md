# AetherNode Telemetry

AetherNodes are modular field-mapping devices that feed EchoNet with local and cluster-level telemetry.

## Purpose

AetherNodes are the physical/edge sensing layer for EchoNet. They may include QRNG, EMF, magnetic, temperature, humidity, vibration, acoustic, light, barometric, GPS/location class, and local edge-ML anomaly scoring. EchoNet receives their normalized output and converts it into coherence features, event windows, dashboards, and handoff candidates.

## Node-level payload

```json
{
  "node_event_type": "sensor.window",
  "node_id_hash": "node_alpha_hash",
  "cluster_id": "cluster_alpha",
  "window_start": "2026-01-11T04:33:00Z",
  "window_end": "2026-01-11T04:33:05Z",
  "sensor_profile": ["qrng", "emf", "magnetic", "temp", "vibration", "acoustic"],
  "qrng_entropy": 0.503,
  "emf_uT": 0.101,
  "magnetic_uT": null,
  "temperature_c": 21.4,
  "vibration_rms": 0.02,
  "acoustic_rms": 0.14,
  "local_coherence_raw": 0.30,
  "edge_anomaly_score": 0.08
}
```

## Cluster-level payload

```json
{
  "cluster_event_type": "coherence.window",
  "cluster_id": "cluster_alpha",
  "node_count": 5,
  "r_value": 0.33,
  "spectral_entropy": 2.57,
  "concurrence_proxy": 0.41,
  "anomaly_flag": false,
  "anomaly_score": 0.12,
  "eta_proxy": 0.41
}
```

## Current baseline from project files

The current simulation baseline uses 10 nodes, cluster size 5, `dt=0.1`, `t_max=100`, seed 42, strong intra-cluster coupling, sparse inter-cluster coupling, and a controlled anomaly window from 50-60 seconds. Monte Carlo results across 50 seeds report 6.5 percent hybrid path improvement, zero failure rate for both baseline and hybrid methods, and EchoNet anomaly detection around 0.76 seconds on average.

## Boundary

EchoNet can ingest and aggregate AetherNode telemetry. It should not claim that sensor readings prove consciousness, identity, or spiritual state. Research-facing experiments should remain clearly labeled and use active/sham sessions, baselines, Monte Carlo controls, and privacy review.
