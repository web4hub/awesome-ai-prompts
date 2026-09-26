#!/usr/bin/env python3
"""
Aura Prompts CLI - Validates and manages prompt registries.
"""

import os
import sys
import yaml

PROMPTS_DIR = os.path.join(os.path.dirname(__file__), "../prompts")

def validate_prompts():
    print("🔍 Scanning prompt registry...")
    valid_count = 0
    
    for root, _, files in os.walk(PROMPTS_DIR):
        for file in files:
            if file.endswith((".md", ".yml", ".yaml")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.startswith("---"):
                            parts = content.split("---", 2)
                            if len(parts) >= 3:
                                frontmatter = yaml.safe_load(parts[1])
                                print(f"  [OK] Validated: {frontmatter.get('id', file)}")
                                valid_count += 1
                except Exception as e:
                    print(f"  [ERROR] Failed to parse {file}: {e}")
                    sys.exit(1)
                    
    print(f"\n✨ Successfully validated {valid_count} prompt definitions.")

if __name__ == "__main__":
    if "--validate" in sys.argv:
        validate_prompts()
    else:
        print("Usage: python cli/main.py --validate")
