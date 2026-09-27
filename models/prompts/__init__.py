import os
import re
from pathlib import Path

def validate_markdown_file(file_path: Path) -> dict:
    """Reads a prompt file, checks for required metadata headers, and returns stats."""
    content = file_path.read_text(encoding="utf-8")
    
    # Check for metadata tags
    has_metadata = "## Metadata" in content or "Tags:" in content
    has_template = "## Prompt Template" in content or "```text" in content
    
    word_count = len(content.split())
    
    return {
        "file": file_path.name,
        "valid_structure": has_metadata and has_template,
        "word_count": word_count
    }

def run_repository_audit():
    print("🚀 Initializing Web4Hub Awesome AI Prompts Repository Audit...")
    prompts_dir = Path("./prompts")
    
    if not prompts_dir.exists():
        print("⚠️ Warning: 'prompts/' directory not found. Scanning root markdown files instead...")
        search_path = Path(".")
        files = list(search_path.glob("*.md"))
    else:
        files = list(prompts_dir.rglob("*.md"))
    
    if not files:
        print("❌ No markdown prompt files found to audit.")
        return

    print(f"📁 Found {len(files)} markdown file(s). Running validation checks...\n")
    
    total_words = 0
    valid_count = 0
    
    for file in files:
        if file.name.lower() == "readme.md":
            continue
        
        stats = validate_markdown_file(file)
        total_words += stats["word_count"]
        
        status = "✅ PASS" if stats["valid_structure"] else "⚠️ NEEDS REVIEW (Missing Metadata/Template)"
        if stats["valid_structure"]:
            valid_count += 1
            
        print(f"  - [{status}] {file.relative_to(Path('.'))} ({stats['word_count']} words)")

    print("\n" + "="*40)
    print("📊 AUDIT SUMMARY")
    print("="*40)
    print(f"Total Prompt Files Audited : {len(files) - 1 if (Path('.').glob('README.md')) else len(files)}")
    print(f"Structured Prompts Passed  : {valid_count}")
    print(f"Total Repository Corpus    : {total_words} words")
    print("✨ Repository check completed successfully.")

if __name__ == "__main__":
    run_repository_audit()
