# CI Validation Gate

EchoNet CI must validate schemas/examples, run the full pytest suite, and exercise CLI validation paths on Python 3.11 and 3.12.

The current verification target includes automatic and explicit validation of `examples/ai_witness_dataset_example.json` against the `ai_witness` schema. Dataset envelopes are validated but are not classified as event-ingestion packets.
