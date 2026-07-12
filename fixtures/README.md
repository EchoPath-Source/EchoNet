# EchoNet Fixture Catalog

This directory contains public-safe fixture packets for adapter development and contract testing.

Fixtures are grouped by adapter/domain and are intended to exercise the same schemas and ingestion path used by `examples/`, but with more realistic event variety.

## Directory map

```text
fixtures/
  memory_layer/
  navigator/
  aethernode/
  echochain/
  manifest.json
```

## Rules

- Use fake IDs only.
- Do not include raw user identity, raw room maps, raw conversations, raw sensor streams, or real location data.
- Public-safe packets must be anonymous and retain no raw payload.
- Internal fixtures may use hashed node/session/account IDs.
- EchoChain handoff fixtures must remain privacy projections, not raw telemetry dumps.

## Validation

Run:

```bash
echonet validate fixtures/
pytest
```

The fixture manifest records each fixture path, expected schema, domain, event type, and purpose.
