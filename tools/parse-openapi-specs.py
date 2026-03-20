#!/usr/bin/env python3
"""Extract all endpoint definitions from an OpenAPI JSON file into a directory of JSON files and a markdown index file."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

# First download the OpenAPI JSON file from https://api.laji.fi/openapi-json

INPUT_FILE = Path(__file__).with_name("openapi-json.json")
OUTPUT_DIR = Path(__file__).with_name("references")
MARKDOWN_INDEX_FILE = Path(__file__).with_name("ENDPOINTS.md")
HTTP_METHODS = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}
EXCLUDED_ENDPOINT_PREFIXES = [
    "/trait",
    "/news",
    "/logger",
    "/feedback",
    "/html-to-pdf",
    "/publications",
    "/geo-convert",
    "geo-convert", # legacy
    "/google-maps",
    "/coordinates",
    ]


def _resolve_json_pointer(document: dict[str, Any], pointer: str) -> Any:
    """Resolve a local JSON pointer like '#/components/schemas/Foo'."""
    if not pointer.startswith("#/"):
        raise ValueError(f"Unsupported ref format: {pointer}")

    current: Any = document
    for token in pointer[2:].split("/"):
        # RFC 6901 unescaping.
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(current, dict) and token in current:
            current = current[token]
        else:
            raise KeyError(f"Reference not found: {pointer}")
    return current


def _collect_refs(value: Any, refs: set[str]) -> None:
    """Recursively collect local $ref values from nested JSON data."""
    if isinstance(value, dict):
        ref = value.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/"):
            refs.add(ref)
        for nested in value.values():
            _collect_refs(nested, refs)
    elif isinstance(value, list):
        for item in value:
            _collect_refs(item, refs)


def _merge_component_subset(
    components_subset: dict[str, dict[str, Any]], pointer: str, value: Any
) -> None:
    """Store a referenced component object under components.<section>.<name>."""
    parts = pointer[2:].split("/")
    if len(parts) < 3 or parts[0] != "components":
        return

    section, name = parts[1], parts[2]
    components_subset.setdefault(section, {})
    if name not in components_subset[section]:
        components_subset[section][name] = copy.deepcopy(value)


def _sanitize_path_for_filename(path: str) -> str:
    """Build a stable, readable filename chunk from an endpoint path."""
    cleaned = path.strip("/")
    if not cleaned:
        return "root"
    return cleaned.replace("/", "_")


def _write_markdown_index(
    endpoint_records: list[tuple[str, str, str]], output_dir: Path, markdown_path: Path
) -> None:
    """Write only parsing-friendly rows for LLM/tool consumption."""
    lines = ["METHOD | ENDPOINT_PATH | REFERENCE_FILE"]

    for method, endpoint_path, filename in endpoint_records:
        rel_path = (output_dir / filename).relative_to(markdown_path.parent)
        lines.append(f"{method} | {endpoint_path} | {rel_path.as_posix()}")

    with markdown_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def _extract_operation_payload(
    spec: dict[str, Any], endpoint_path: str, method: str, operation: dict[str, Any]
) -> dict[str, Any]:
    path_item = spec.get("paths", {}).get(endpoint_path, {})
    refs_to_process: list[str] = []
    seen_refs: set[str] = set()
    _collect_refs(operation, seen_refs)
    _collect_refs(path_item.get("parameters", []), seen_refs)
    refs_to_process.extend(sorted(seen_refs))

    components_subset: dict[str, dict[str, Any]] = {}
    processed_refs: set[str] = set()

    # Resolve refs recursively so nested schema refs are included as well.
    while refs_to_process:
        ref = refs_to_process.pop()
        if ref in processed_refs:
            continue
        processed_refs.add(ref)

        referenced_value = _resolve_json_pointer(spec, ref)
        _merge_component_subset(components_subset, ref, referenced_value)

        nested_refs: set[str] = set()
        _collect_refs(referenced_value, nested_refs)
        for nested_ref in nested_refs:
            if nested_ref not in processed_refs:
                refs_to_process.append(nested_ref)

    return {
        "openapi": spec.get("openapi"),
        "info": spec.get("info"),
        "target": {"path": endpoint_path, "method": method.upper()},
        "pathItem": {"parameters": path_item.get("parameters", [])},
        "operation": operation,
        "components": components_subset,
        "resolvedRefs": sorted(processed_refs),
    }


def extract_all_endpoints(
    input_path: Path = INPUT_FILE,
    output_dir: Path = OUTPUT_DIR,
    markdown_index_path: Path = MARKDOWN_INDEX_FILE,
) -> list[Path]:
    with input_path.open("r", encoding="utf-8") as f:
        spec = json.load(f)

    paths_obj = spec.get("paths", {})
    if not isinstance(paths_obj, dict):
        raise ValueError("OpenAPI spec does not contain a valid 'paths' object.")

    output_dir.mkdir(parents=True, exist_ok=True)
    written_files: list[Path] = []
    endpoint_records: list[tuple[str, str, str]] = []

    for endpoint_path, path_item in paths_obj.items():
        if not isinstance(path_item, dict):
            continue
        if any(endpoint_path.startswith(prefix) for prefix in EXCLUDED_ENDPOINT_PREFIXES):
            continue

        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                continue

            extracted = _extract_operation_payload(spec, endpoint_path, method, operation)
            filename = f"{method.lower()}_{_sanitize_path_for_filename(endpoint_path)}.json"
            output_path = output_dir / filename

            with output_path.open("w", encoding="utf-8") as f:
                json.dump(extracted, f, indent=2, ensure_ascii=False)
                f.write("\n")

            written_files.append(output_path)
            endpoint_records.append((method.upper(), endpoint_path, filename))
    _write_markdown_index(endpoint_records, output_dir=output_dir, markdown_path=markdown_index_path)

    return written_files


if __name__ == "__main__":
    outputs = extract_all_endpoints()
    print(f"Wrote {len(outputs)} endpoint files to: {OUTPUT_DIR}")
    print(f"Wrote markdown endpoint index to: {MARKDOWN_INDEX_FILE}")
