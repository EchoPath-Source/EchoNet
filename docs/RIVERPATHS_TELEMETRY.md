# RiverPaths Telemetry

**Status:** adapter guidance note  
**Audience:** EchoPath demo builders, EchoNet adapter authors, product/pilot instrumentation planning  
**Purpose:** define the public-safe telemetry posture for RiverPaths and adjacent EchoPath route-generation demos

## 1. Why this document exists

RiverPaths is one of the earliest field-first public proofs in the EchoPath stack.

That means it has two jobs at once:

1. show that the route-generation experience is visually compelling;
2. emit telemetry that can later support replay, evidence, diagnostics, and sealed-event handoff.

This document makes the second job explicit.

## 2. RiverPaths role inside EchoNet

RiverPaths is treated as a route-telemetry source.

Its event stream should let EchoNet capture:

- path outcomes;
- route quality metrics;
- fallback and no-path posture;
- obstacle and replan behavior;
- tube and braid identifiers where available;
- enough stable structure to support later route cards, replay, audit, and ledger-compatible handoff.

## 3. Primary event type

RiverPaths should emit:

```text
event_type = route.telemetry
source.system = riverpaths
domain = RiverPaths
```

The current normalized specialization remains the Navigator telemetry schema because that schema already covers route, corridor, route-card, RiverPaths, and EchoPath decision-support telemetry.

## 4. Minimum payload fields

### Required for first-wave demos

- `route_event_type` — e.g. `route.requested`, `route.completed`, `route.failed`, `route.replanned`
- `planner` — e.g. `riverpaths`
- `status` — e.g. `path_found`, `no_path`, `fallback_used`, `abandoned`
- `start_anchor_id`
- `goal_anchor_id`
- `path_length`
- `mean_curvature`
- `max_curvature`
- `jerk`
- `replan_churn`

### Strongly recommended

- `route_card_id`
- `display_mode`
- `tube_ids`
- `braid_ids`
- `eta_proxy_local`
- `confidence_local`
- `obstacle_mode`
- `fallback_reason`

### Later but important

- `collision_count`
- `near_collision_count`
- `dynamic_obstacle_events`
- `seal_candidate`
- `replay_pointer`

## 5. Example route event categories

### Route requested

Use when a route generation request begins.

### Route completed

Use when a path is found and the relevant metrics are available.

### Route failed

Use when no route or no stable route is available.

### Route replanned

Use when dynamic obstacles or field changes force a new route.

### Route fallback

Use when a degraded or alternate display/behavior mode is used instead of the preferred route mode.

## 6. Instrumentation priorities

### Priority 1 — every meaningful run emits a normalized event

A public demo should not only render a path. It should emit an event record that can later be compared, replayed, and summarized.

### Priority 2 — preserve stable route identity

Where available, keep route-card IDs, tube IDs, and braid/lane identifiers stable across replans so later diagnostics and deconfliction analytics do not lose continuity.

### Priority 3 — preserve failure context

`no_path` and fallback cases are useful product evidence and should not be discarded.

### Priority 4 — public-safe by default

Do not send raw scene payloads, full geometry exports, or sensitive user identity unless a later internal mode explicitly requires them.

## 7. Public/private boundary

EchoNet should preserve:

- route IDs;
- anchor IDs;
- summary metrics;
- confidence and eta-style posture;
- fallback and anomaly notes;
- tube/braid identifiers if available.

EchoNet should not require:

- private kernel constants;
- protected weighting logic;
- raw full-scene geometry;
- personally identifying telemetry by default.

## 8. Relationship to replay and later ledger handoff

RiverPaths telemetry is not itself the full ledger or sealing layer.

But it should be shaped so later systems can do the following without changing event meaning:

- generate replay artifacts;
- compare runs over time;
- seal consequential route decisions;
- route selected high-value events into Reflection Ledger / governance-safe history.

## 9. Recommended implementation rule

```text
Every meaningful RiverPaths run should be both a demo event and a telemetry event.
```

That is the simplest path from public demo -> EchoNet analytics -> later replay and ledger compatibility.

## 10. Current references

- `schemas/navigator_telemetry_event.schema.json`
- `examples/navigator_route_event_example.json`
- `docs/NAVIGATOR_TELEMETRY.md`
- `docs/CLUSTER_AND_SIMULATION_BASELINE.md`
