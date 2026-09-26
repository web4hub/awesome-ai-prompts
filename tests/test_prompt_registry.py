import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class PromptRegistryTests(unittest.TestCase):
    def test_prompt_validation(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate-prompts.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_registry_is_valid_json(self) -> None:
        index = json.loads((ROOT / "registry" / "index.json").read_text(encoding="utf-8"))
        checksums = json.loads((ROOT / "registry" / "checksums.json").read_text(encoding="utf-8"))
        self.assertEqual(index["count"], len(index["prompts"]))
        self.assertEqual(set(checksums["files"]), {entry["path"] for entry in index["prompts"]})


if __name__ == "__main__":
    unittest.main()
