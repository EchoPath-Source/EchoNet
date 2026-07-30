# Q-RRG Route Telemetry Profile

**Status:** public-safe contract scaffold  
**Owner:** EchoNet  
**Purpose:** define how Q-RRG, EchoPath, and route experiments report evidence into EchoNet without exposing private kernel mechanisms.

## Boundary

EchoNet owns telemetry semantics, evidence labels, privacy projections, and research-export compatibility. EchoNet does not own Q-RRG route computation, field synthesis, ridge extraction, or production planner logic.

## Event class

Recommended event type:

```text
qrrg.simulation_result
```

The event may describe a synthetic simulation, replay benchmark, shadow-mode evaluation, or measured deployment. The evidence status must always be explicit.

## Required evidence labels

| Field | Meaning |
|---|---|
| `evidence_status` | `synthetic`, `replay`, `shadow`, or `measured` |
| `claim_level` | `observation`, `benchmark`, `pilot`, or `deployment` |
| `scenario_class` | Geometry or benchmark regime |
| `complete_route` | Whether the selected path actually connected the requested start and goal |
| `baseline_equivalent` | Whether compared planners solved the same task under equivalent constraints |
| `config_hash` | Stable identifier for the run configuration |
| `seed` | Random seed when applicable |

## Scenario classes

- `static_obstacle`
- `curved_ridge`
- `branching_ridge`
- `spiral_ridge`
- `dynamic_obstacle`
- `planner_comparison`
- `multi_agent_stress`
- `recorded_replay`
- `physical_pilot`

## Recommended metric families

### Environment and task

- grid or world dimensions;
- start and goal coordinates or hashed anchors;
- obstacle count and density;
- dynamic-obstacle state;
- frame or timestep;
- environment/version identifier.

### Connectivity

- complete-route flag;
- connected-component count;
- start-anchor distance;
- goal-anchor distance;
- ridge coverage;
- ridge count;
- extracted path count;
- selected path ID.

### Geometry and motion quality

- path length in steps;
- Euclidean or metric length;
- curvature statistic;
- heading-change or kink count;
- jerk proxy;
- obstacle clearance;
- route-to-prior-route displacement;
- tube or corridor identity continuity.

### Runtime and execution

- total runtime;
- field synthesis time;
- ridge extraction time;
- route-selection time;
- hardware/runtime label;
- implementation version;
- fallback mode;
- failure reason.

### Comparison integrity

Every baseline comparison should carry:

- baseline planner name and version;
- identical start-goal task flag;
- identical environment and constraints flag;
- complete route for each candidate;
- comparable timing scope;
- metric direction, such as lower-is-better or higher-is-better.

A report must not compare a complete baseline route to an incomplete ridge segment as though both solved the same task.

## Privacy and exposure rules

Public-safe route telemetry should use:

- hashed route, tube, environment, and actor identifiers;
- aggregate geometry metrics;
- configuration hashes instead of proprietary parameters;
- bounded reason codes;
- no raw sensor frames unless separately approved;
- no private field equations, weights, thresholds, or kernel constants.

## Current synthetic test mapping

| Test | Evidence status | Important caveat |
|---|---|---|
| Static obstacle | `synthetic` | Obstacle exclusion was encoded in the field/ridge structure |
| Curved and branching | `synthetic` | Segment discovery does not guarantee full route connectivity |
| Spiral ridge | `synthetic` | High-curvature scalar-field test only |
| Dynamic obstacle | `synthetic` | Field and ridges were recomputed for each position |
| A* comparison | `synthetic` | Q-RRG segment was not endpoint-complete; baseline equivalence is false |
| Multi-agent robustness | `synthetic` | Operating-envelope guidance, not physical fleet validation |

## Downstream use

EchoNet may use these events for:

- dashboard summaries;
- benchmark evidence packs;
- replay and anomaly analysis;
- AI-witness-ready exports;
- sealed handoff to Reflection Ledger;
- cross-run comparison after evidence-status filtering.

Downstream consumers must not silently upgrade `synthetic` observations into `measured` deployment claims.
