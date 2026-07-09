"""Command-line interface for EchoNet contract validation and minimal ingestion."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

from .ingestion import ingest_file
from .validation import SchemaValidationError, validate_payload


def _iter_json_files(paths: Iterable[str]) -> list[Path]:
    files: list[Path] = []
    for raw_path in paths:
        path = Path(raw_path)
        if path.is_dir():
            files.extend(sorted(path.glob("*.json")))
        else:
            files.append(path)
    return files


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_command(args: argparse.Namespace) -> int:
    ok = True
    for path in _iter_json_files(args.paths):
        try:
            schema_name = validate_payload(_load_json(path), schema_name=args.schema)
            print(f"valid {path} [{schema_name}]")
        except (OSError, json.JSONDecodeError, SchemaValidationError, KeyError) as exc:
            ok = False
            print(f"invalid {path}: {exc}", file=sys.stderr)
    return 0 if ok else 1


def classify_command(args: argparse.Namespace) -> int:
    ok = True
    for path in _iter_json_files(args.paths):
        try:
            summary = ingest_file(path).to_dict()
            print(json.dumps(summary, indent=2, sort_keys=True))
        except (OSError, json.JSONDecodeError, SchemaValidationError, KeyError) as exc:
            ok = False
            print(f"failed {path}: {exc}", file=sys.stderr)
    return 0 if ok else 1


def ingest_command(args: argparse.Namespace) -> int:
    # For now, ingestion is validation + normalized routing summary. Persistence belongs in a later PR.
    return classify_command(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate and summarize EchoNet event packets.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate JSON files or directories of JSON files.")
    validate_parser.add_argument("paths", nargs="+", help="JSON files or directories to validate.")
    validate_parser.add_argument("--schema", choices=["echonet", "memory", "navigator", "aethernode", "handoff"], help="Force a specific schema instead of auto-routing.")
    validate_parser.set_defaults(func=validate_command)

    classify_parser = subparsers.add_parser("classify", help="Validate JSON files and emit routing summaries.")
    classify_parser.add_argument("paths", nargs="+", help="JSON files or directories to classify.")
    classify_parser.set_defaults(func=classify_command)

    ingest_parser = subparsers.add_parser("ingest", help="Validate JSON files and emit ingestion summaries.")
    ingest_parser.add_argument("paths", nargs="+", help="JSON files or directories to ingest.")
    ingest_parser.set_defaults(func=ingest_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
