"""Validation helpers for EchoNet event packets."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from jsonschema import Draft202012Validator

from .schemas import load_schemas, schema_for_payload, schema_registry


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str


class SchemaValidationError(ValueError):
    """Raised when an EchoNet packet fails schema validation."""

    def __init__(self, schema_name: str, issues: list[ValidationIssue]):
        self.schema_name = schema_name
        self.issues = issues
        rendered = "; ".join(f"{issue.path}: {issue.message}" for issue in issues)
        super().__init__(f"{schema_name} validation failed: {rendered}")


def _format_path(path: Any) -> str:
    parts = [str(part) for part in path]
    return "/".join(parts) if parts else "<root>"


def validate_payload(payload: dict, schema_name: str | None = None) -> str:
    """Validate a payload and return the schema key used.

    Args:
        payload: Parsed JSON object to validate.
        schema_name: Optional explicit schema key. When omitted, a schema is selected from schema_version/event_type.

    Raises:
        SchemaValidationError: if validation fails.
    """
    selected_schema = schema_name or schema_for_payload(payload)
    schemas = load_schemas()
    if selected_schema not in schemas:
        raise KeyError(f"Unknown EchoNet schema: {selected_schema}")

    validator = Draft202012Validator(schemas[selected_schema], registry=schema_registry())
    errors = sorted(validator.iter_errors(payload), key=lambda err: list(err.path))
    if errors:
        issues = [ValidationIssue(path=_format_path(error.path), message=error.message) for error in errors]
        raise SchemaValidationError(selected_schema, issues)
    return selected_schema
