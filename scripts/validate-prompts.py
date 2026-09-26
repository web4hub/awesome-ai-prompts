#!/usr/bin/env python3
"""Validate APS-1.0 prompt frontmatter using only the Python standard library."""

from __future__ import annotations

import ast
import pathlib
import re
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPT_ROOTS = [ROOT / "prompts", ROOT / "promptcards"]
REQUIRED = ("id", "name", "version", "author", "ecosystem", "target_engine", "tags")
SEMVER = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")

    data: dict[str, object] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key, value = key.strip(), value.strip()
        if not key:
            continue
        try:
            parsed = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            if value.startswith("[") and value.endswith("]"):
                parsed = [item.strip().strip("\"'") for item in value[1:-1].split(",") if item.strip()]
            else:
                parsed = value.strip("\"'")
        data[key] = parsed
    return data


def validate_file(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    try:
        data = parse_frontmatter(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"{path.relative_to(ROOT)}: {exc}"]

    missing = [key for key in REQUIRED if key not in data]
    if missing:
        errors.append(f"{path.relative_to(ROOT)}: missing required fields: {', '.join(missing)}")

    prompt_id = data.get("id")
    if isinstance(prompt_id, str) and not ID.fullmatch(prompt_id):
        errors.append(f"{path.relative_to(ROOT)}: invalid id {prompt_id!r}")

    version = data.get("version")
    if isinstance(version, str) and not SEMVER.fullmatch(version):
        errors.append(f"{path.relative_to(ROOT)}: invalid semver version {version!r}")

    tags = data.get("tags")
    if not isinstance(tags, list) or not tags or not all(isinstance(tag, str) and tag.strip() for tag in tags):
        errors.append(f"{path.relative_to(ROOT)}: tags must be a non-empty list of strings")

    for key in ("name", "author", "ecosystem", "target_engine"):
        value = data.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path.relative_to(ROOT)}: {key} must be a non-empty string")

    return errors


def main() -> int:
    files = sorted(
        path for root in PROMPT_ROOTS if root.exists()
        for path in root.rglob("*.md")
        if path.is_file()
    )

    if not files:
        print("APS validation: no prompt Markdown files found; nothing to validate.")
        return 0

    errors: list[str] = []
    ids: defaultdict[str, list[pathlib.Path]] = defaultdict(list)

    for path in files:
        errors.extend(validate_file(path))
        try:
            data = parse_frontmatter(path.read_text(encoding="utf-8"))
            prompt_id = data.get("id")
            if isinstance(prompt_id, str):
                ids[prompt_id].append(path)
        except (OSError, ValueError):
            pass

    for prompt_id, paths in ids.items():
        if len(paths) > 1:
            joined = ", ".join(str(path.relative_to(ROOT)) for path in paths)
            errors.append(f"duplicate prompt id {prompt_id!r}: {joined}")

    if errors:
        print("APS validation failed:")
        print("\n".join(f" - {error}" for error in errors))
        return 1

    print(f"APS validation passed: {len(files)} prompt file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
