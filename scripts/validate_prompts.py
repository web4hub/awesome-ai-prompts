import os
import sys
import yaml
from pathlib import Path

PROMPTS_DIR = Path("./prompts")
REQUIRED_FIELDS = ["id", "name", "version", "ecosystem", "target_engine", "tags", "author"]

def validate_prompt_file(file_path: Path) -> bool:
    try:
        content = file_path.read_text(encoding="utf-8")
        if not content.startswith("---"):
            print(f"[-] Error: {file_path.name} missing YAML frontmatter header.")
            return False
        
        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"[-] Error: {file_path.name} has malformed frontmatter delimiters.")
            return False
            
        frontmatter = yaml.safe_load(parts[1])
        
        # Validate required fields
        for field in REQUIRED_FIELDS:
            if field not in frontmatter:
                print(f"[-] Error: {file_path.name} missing required field -> '{field}'")
                return False
                
        # Validate ID formatting (kebab-case, lowercase)
        prompt_id = frontmatter["id"]
        if not prompt_id.islower() or " " in prompt_id:
            print(f"[-] Error: {file_path.name} ID '{prompt_id}' must be lowercase kebab-case.")
            return False
            
        print(f"[+] Success: {file_path.name} passed APS-1.0 schema validation.")
        return True
    except Exception as e:
        print(f"[-] Exception parsing {file_path.name}: {e}")
        return False

def main():
    if not PROMPTS_DIR.exists():
        print(f"[-] Directory {PROMPTS_DIR} not found.")
        sys.exit(0)
        
    failed = 0
    total = 0
    for prompt_file in PROMPTS_DIR.glob("**/*.md"):
        total += 1
        if not validate_prompt_file(prompt_file):
            failed += 1
            
    if failed > 0:
        print(f"\n[-] Validation failed: {failed}/{total} files invalid.")
        sys.exit(1)
    else:
        print(f"\n[+] All {total} prompt artifacts validated successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
