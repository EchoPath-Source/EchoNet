# Public / Private Boundary

EchoNet sits between public demos, internal telemetry, private runtime systems, and future sealed ledgers. This repository must make those boundaries explicit from the beginning.

## Public-safe

May be published or used in public demos:

- Aggregated demo counts.
- Synthetic/mock telemetry.
- Schema examples with fake IDs.
- High-level route outcome summaries.
- Public-safe dashboards that do not expose raw location, raw identity, raw conversation, or private sensor streams.

## Internal

May be used inside Echo Labs repos and project files:

- Adapter contracts.
- Hashed node/session/account IDs.
- Coherence windows and summaries.
- Route IDs, tube IDs, route-card IDs.
- Memory threshold transitions.
- Simulation metrics and evaluation notes.

## Restricted

Requires explicit review before storage or sharing:

- Raw AetherNode sensor streams from real homes, venues, or operators.
- Raw location/time-linked telemetry.
- Relationship graphs or contribution trails tied to identifiable people.
- Raw memory logs, room maps, user/player behavior histories, or private conversations.
- EchoChain scoring features that could reveal social graph structure.

## Research-private

Requires research framing and should not be presented as product proof:

- Human/AI witness experiments.
- QRNG correlation studies.
- Active/sham resonance sessions.
- Consciousness, collapse, or observer-effect experiments.

## Rule of thumb

EchoNet may transport a projection of a sensitive event. It should not become the archive of raw sensitive experience unless a separate policy, consent model, and retention rule exists.
