# Website and Demo Telemetry

Status: Public-safe ingestion contract note

## Purpose

EchoPathXR.com is now an active public product surface. EchoNet should accept normalized events from the website, live demonstrations, pilot-intake flows, waitlists, and future early-access commerce without owning the website or exposing private user content.

## Event classes

### `demo.analytics`

Public-safe interaction with a demonstration.

Suggested fields:

- `event_name`: `page_view`, `media_start`, `media_complete`, `cta_click`, `demo_error`
- `demo_id`: stable public identifier such as `riverpaths-prototype`
- `session_id`: pseudonymous session identifier
- `page_path`
- `product_layer`: `smooth`, `pathing`, `memory`, `native`, `cognition`, `navigator`
- `prototype_status`
- `media_progress_pct`
- `cta_target`
- `error_code`
- `timestamp`

### `route.telemetry`

Bounded output from an interactive RiverPaths or Navigator surface.

Suggested fields:

- `route_id`
- `route_card_id`
- `demo_id`
- `result_status`
- `selected_path_source`
- `fallback_mode`
- `eta_proxy`
- `path_length`
- `smoothness_proxy`
- `runtime_ms`
- `reason_codes`

Do not include private kernel parameters or raw scene content.

### `conversion.intent`

A public CTA or product-interest signal.

Suggested fields:

- `intent_type`: `product_interest`, `pilot_interest`, `waitlist`, `documentation`, `contact`
- `source_page`
- `source_demo`
- `product_interest`
- `campaign_id`
- `session_id`
- `timestamp`

### `pilot.request`

A bounded projection of a pilot inquiry. Raw contact forms should remain in the website or CRM system. EchoNet receives only the minimum normalized summary needed for analytics and downstream workflow.

Suggested fields:

- `request_id`
- `pilot_type`
- `industry`
- `product_layer`
- `scope_band`
- `consent_to_contact`
- `source_page`
- `timestamp`

## Privacy and security rules

- Prefer hashed or pseudonymous identifiers.
- Do not ingest raw message bodies by default.
- Do not collect private environment scans, scene meshes, source code, or proprietary customer assets through analytics events.
- Keep analytics and research-consent flows distinct.
- Require explicit consent before connecting website activity to identifiable contact records.
- Project only validated events into sealed handoff or Reflection Ledger candidates.

## Initial sources

- RiverPaths prototype page
- Memory Layer page and visualizer
- Technology Layers page
- Live Demos / Demo Hub
- Pilots & Consulting
- Waitlist and early-access forms
- Shop product-interest and checkout events when commerce is active

## Implementation sequence

1. Validate example fixtures.
2. Reuse the existing `echonet_event` envelope where possible.
3. Add a dedicated schema only if current payload validation cannot express the event safely.
4. Build a local event-store stub.
5. Generate dashboard-ready mock streams.
6. Add sealed handoff only for events that meet policy and consent requirements.
