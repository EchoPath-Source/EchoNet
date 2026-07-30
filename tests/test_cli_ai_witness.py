from __future__ import annotations

from echonet.cli import main


def test_cli_validates_ai_witness_example_with_explicit_schema() -> None:
    result = main([
        "validate",
        "examples/ai_witness_dataset_example.json",
        "--schema",
        "ai_witness",
    ])
    assert result == 0
