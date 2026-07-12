# AI Witness Dataset Protocol

**Status:** scaffold / protocol note  
**Purpose:** define how EchoNet packages research-facing AI-witness exports while preserving claim boundaries, privacy posture, calibration context, and sealed-event compatibility.

## Why this exists

EchoNet already preserves telemetry, anomaly packaging, and privacy-aware handoff. This protocol adds a narrower question:

> What must be present before a synchronized telemetry export is considered suitable for AI-witness benchmarking, comparison, or sealed research-event generation?

This protocol is intentionally conservative. It is designed to prevent stronger claims from being implied by under-described datasets.

## AI witness definition

Within EchoNet, an **AI witness** is a reproducible model or evaluation pipeline that:

- observes synchronized physical and/or runtime telemetry windows,
- compares active and control-like conditions,
- estimates uncertainty,
- produces bounded summaries,
- and can emit a privacy-aware, auditable output.

It does **not** by itself prove consciousness, intention effects, nonlocal causation, spiritual state, or universal field claims.

## Required metadata families

Every AI-witness-ready export should preserve these metadata families when applicable.

### 1. Dataset identity

- `dataset_id`
- `dataset_version`
- `generated_at`
- `protocol_version`
- `claim_level`

### 2. Condition labeling

At least one explicit condition label should be present:

- `active`
- `baseline`
- `sham`
- `decoy`
- `holdout`
- `unknown`

If only `unknown` is available, the export may still be useful for anomaly clustering, but not for stronger active-vs-control claims.

### 3. Source coverage

- `source_class` (for example: aethernode, simulation, runtime, mixed)
- `sensor_modalities`
- `node_count`
- `cluster_count`
- `coverage_window_start`
- `coverage_window_end`
- `sampling_notes`

### 4. Calibration and transform context

- `calibration_version`
- `algorithm_version`
- `normalization_notes`
- `projection_mode`
- `privacy_mode`

### 5. Bounded feature families

Examples include:

- `order_parameter_r`
- `spectral_entropy`
- `concurrence_proxy`
- `eta_proxy`
- `anomaly_score`
- `anomaly_flag`
- `route_stability_delta`
- `tube_id_count`
- `memory_event_count`

Not all fields are mandatory in every export, but missing fields should be absent by design rather than implied.

### 6. Covariates and confidence

- `confidence`
- `confidence_method`
- `covariates` (environment, weather, device-health, site class, schedule notes, etc.)
- `limitations`

### 7. Governance / handoff

- `seal_mode`
- `event_id` if a sealed event was produced
- `downstream_targets`

## Claim levels

Use one of the following bounded labels:

- `simulation_reference`
- `research_export`
- `runtime_observation`
- `pilot_measurement`
- `sealed_research_event`

Do not silently upgrade one label into another in downstream dashboards or summaries.

## Minimum protocol rule

An export should not be treated as AI-witness-ready unless it includes:

1. dataset identity,
2. explicit condition labeling,
3. source coverage,
4. calibration or algorithm version,
5. privacy mode,
6. at least one bounded confidence field,
7. and a stated claim level.

## Privacy rule

Default posture:

- prefer hashed IDs,
- avoid raw personally identifying content,
- preserve projections and summaries rather than raw sensitive streams where possible,
- document whether the export is public-safe, internal-only, or sealed.

## Relationship to EchoGenesis and Vision Codex

- **EchoGenesis** owns the broader governance and witness/sealing architecture.
- **EchoNet** owns the dataset/export semantics and telemetry packaging.
- **Vision Codex** may describe AI witness as a bounded research/application milestone, but should not redefine this protocol.

## Suggested next implementation step

This scaffold is designed to pair with:

- `schemas/ai_witness_dataset.schema.json`
- `examples/ai_witness_dataset_example.json`

Those files can remain lightweight at first; the direct repo thread can harden them into validation-ready artifacts from here.
