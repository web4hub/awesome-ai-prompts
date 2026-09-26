# Awesome AI Prompts 🚀

A production-oriented, multi-ecosystem prompt engineering repository for **Web4**, **LMLM**, decentralized AI workflows, and modern developer tooling.

The repository treats prompts as versioned engineering artifacts: they should have stable metadata, predictable structure, and automated validation.

## 📂 Repository Structure

- `prompts/` — curated, version-controlled prompts organized by target engine and use case.
- `promptcards/` — reusable modular prompt components with structured frontmatter.
- `schemas/` — machine-readable schemas for prompt metadata.
- `scripts/` — repository validation and maintenance tooling.
- `cli/` & `sdk/` — developer tooling when present.
- `docs/` — specifications, guides, and architecture documentation.

## ⚡ Quick Start

```bash
git clone https://github.com/web4hub/awesome-ai-prompts.git
cd awesome-ai-prompts
python3 scripts/validate-prompts.py
```

If the repository contains no prompt Markdown files yet, validation exits successfully and reports that there is nothing to validate.

## 🧬 Aura Prompt Specification

Prompt documents can follow **APS-1.0**, defined in [AURA_PROMPT_SPEC.md](AURA_PROMPT_SPEC.md).

The machine-readable contract lives at [schemas/aura-prompt.schema.json](schemas/aura-prompt.schema.json).

An APS prompt begins with YAML frontmatter containing, at minimum:

```yaml
---
id: "lmlm-code-gen-v1"
name: "LMLM Multi-Language Code Generator"
version: "1.0.0"
author: "Author Name"
ecosystem: "aura-web4"
target_engine: "lmlm"
tags: ["code-generation", "multi-language"]
---
```

## ✅ Validation

Run locally:

```bash
python3 scripts/validate-prompts.py
```

The validator checks:

- required APS metadata fields;
- prompt ID format;
- semantic version format;
- non-empty tags;
- required string fields;
- duplicate prompt IDs;
- valid YAML frontmatter boundaries.

GitHub Actions runs the same validation for pushes to `main` and pull requests.

## 🤝 Contributing

When adding a prompt:

1. Put it in the appropriate `prompts/` or `promptcards/` directory.
2. Give it a stable, unique `id`.
3. Include APS-1.0 frontmatter.
4. Use semantic versioning.
5. Run `python3 scripts/validate-prompts.py`.
6. Keep prompt content focused, reusable, and auditable.

## 📜 Specification

- [Aura Prompt Specification](AURA_PROMPT_SPEC.md)
- [APS-1.0 JSON Schema](schemas/aura-prompt.schema.json)

## License

See the repository license file for the applicable project terms.
