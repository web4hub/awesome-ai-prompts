#!/usr/bin/env python3
"""Run repository-level APS validation and registry consistency checks."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run_validator() -> int:
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate-prompts.py")],
        cwd=ROOT,
        check=False,
    ).returncode


def check_registry() -> int:
    registry = ROOT / "registry" / "index.json"
    checksums = ROOT / "registry" / "checksums.json"
    if not registry.exists() or not checksums.exists():
        print("Repository validation failed: registry files are missing.")
        return 1

    try:
        index = json.loads(registry.read_text(encoding="utf-8"))
        manifest = json.loads(checksums.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Repository validation failed: invalid registry JSON: {exc}")
        return 1

    prompts = index.get("prompts")
    files = manifest.get("files")
    if not isinstance(prompts, list) or not isinstance(files, dict):
        print("Repository validation failed: malformed registry structure.")
        return 1

    if index.get("count") != len(prompts):
        print("Repository validation failed: registry count mismatch.")
        return 1

    registry_paths = {entry.get("path") for entry in prompts}
    manifest_paths = set(files)
    if registry_paths != manifest_paths:
        print("Repository validation failed: registry/checksum path mismatch.")
        return 1

    print(f"Repository validation passed: {len(prompts)} prompt(s) indexed.")
    return 0


def main() -> int:
    if run_validator() != 0:
        return 1
    return check_registry()


if __name__ == "__main__":
    raise SystemExit(main())
