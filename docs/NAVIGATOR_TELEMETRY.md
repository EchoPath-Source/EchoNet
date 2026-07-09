# Navigator and RiverPaths Telemetry

EchoNet receives route/demo telemetry from RiverPaths, EchoPath, and Navigator without owning route computation or user-facing product logic.

## Purpose

Navigator and RiverPaths can emit normalized route events when routes are requested, solved, re-planned, bridged, rejected, or rendered in public demos. EchoNet packages those events for analysis and later cross-system learning.

## Inbound examples

- Route found / no path / fallback used.
- Kernel path vs demo fallback mode.
- Start/goal anchors and tolerance diagnostics.
- Route-card ID emitted.
- Tube ID or corridor ID referenced.
- Curvature, jerk, path length, churn, or jitter summary.
- Operator decision-support action.

## Payload shape

```json
{
  "route_event_type": "route.completed",
  "route_card_id": "route_card_2026_001",
  "planner": "riverpaths|navigator|echopath_smooth|kernel_service",
  "display_mode": "kernel_path",
  "status": "path_found",
  "start_anchor_id": "start_hash",
  "goal_anchor_id": "goal_hash",
  "tube_ids": ["tube_a", "tube_b"],
  "path_length": 25.63,
  "mean_curvature": 0.065,
  "max_curvature": 0.198,
  "jerk": 0.098,
  "replan_churn": 0,
  "fallback_reason": null
}
```

## Boundary

EchoNet stores telemetry and IDs. It does not implement routing, route smoothing, bridge diagnostics, Q-RRG ridge extraction, or Navigator UI. Kernel-private logic stays private; EchoNet receives only public-safe route summaries and stable identifiers.

## Downstream uses

- Route reliability analytics.
- Coherence-aware path comparison.
- Memory-route correlation.
- EchoChain handoff only when route events become contribution, governance, or sealed witness events.
