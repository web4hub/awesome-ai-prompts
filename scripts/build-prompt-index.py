#!/usr/bin/env python3
"""Build a deterministic registry and checksum manifest for APS prompt documents."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
PROMPT_ROOTS = (ROOT / "prompts", ROOT / "promptcards")
ID_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if value.lower() in {"null", "~"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")

    data: dict[str, Any] = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            items = [item.strip() for item in value[1:-1].split(",") if item.strip()]
            data[key] = [scalar(item) for item in items]
        elif value:
            data[key] = scalar(value)
    return data


def prompt_files() -> list[pathlib.Path]:
    return sorted(
        path
        for root in PROMPT_ROOTS
        if root.exists()
        for path in root.rglob("*.md")
        if path.is_file()
    )


def build() -> tuple[list[dict[str, Any]], dict[str, str]]:
    entries: list[dict[str, Any]] = []
    checksums: dict[str, str] = {}

    for path in prompt_files():
        text = path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(text)
        prompt_id = metadata.get("id")
        if not isinstance(prompt_id, str) or not ID_RE.fullmatch(prompt_id):
            raise ValueError(f"{path.relative_to(ROOT)}: invalid or missing id")

        relative = path.relative_to(ROOT).as_posix()
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        checksums[relative] = digest
        entries.append(
            {
                "id": prompt_id,
                "name": metadata.get("name") or metadata.get("title") or prompt_id,
                "version": metadata.get("version", ""),
                "author": metadata.get("author", ""),
                "ecosystem": metadata.get("ecosystem", ""),
                "target_engine": metadata.get("target_engine") or metadata.get("engine", ""),
                "tags": metadata.get("tags", []),
                "path": relative,
                "sha256": digest,
            }
        )

    entries.sort(key=lambda item: (item["id"], item["version"], item["path"]))
    return entries, dict(sorted(checksums.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when generated files are stale")
    args = parser.parse_args()

    entries, checksums = build()
    registry_dir = ROOT / "registry"
    registry_dir.mkdir(exist_ok=True)

    registry = {
        "apiVersion": "aps/v1",
        "kind": "PromptRegistry",
        "count": len(entries),
        "prompts": entries,
    }
    outputs = {
        registry_dir / "index.json": json.dumps(registry, indent=2, ensure_ascii=False) + "\n",
        registry_dir / "checksums.json": json.dumps(
            {"algorithm": "sha256", "files": checksums}, indent=2, ensure_ascii=False
        )
        + "\n",
    }

    stale = []
    for path, content in outputs.items():
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != content:
            stale.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.write_text(content, encoding="utf-8")

    if stale and args.check:
        print("Prompt registry is stale:")
        for path in stale:
            print(f" - {path}")
        return 1

    print(f"Prompt registry: {len(entries)} prompt(s) indexed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
