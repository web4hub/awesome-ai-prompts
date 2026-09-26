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

## Aura Ecosystem

- 🌐 Web4Hub
- 🤖 LMLM
- 🧠 Neomind AI
- ⚡ KIBS
- 📚 APLCE
- ⛓️ Fadaka Blockchain
- ☁️ QUBUHUB Cloud

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
docs(readme): rebrand Awesome AI Prompts for Web4Hub & Aura Ecosystem
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

## Contributing

We welcome prompt engineers, AI researchers, developers,
and Web4 contributors.

1. Fork
2. Create prompt
3. Commit
4. Pull Request
   
## 📜 Specification

- [Aura Prompt Specification](AURA_PROMPT_SPEC.md)
- [APS-1.0 JSON Schema](schemas/aura-prompt.schema.json)

# Built with ❤️ by Web4Hub.

Part of the Aura Ecosystem.

If this repository helps you, leave a ⭐ and contribute new prompts.
# Web4Hub Awesome AI Prompts

The largest curated collection of AI prompts for developers, creators,
researchers, blockchain builders, autonomous agents, and Web4 applications.

Maintained by Web4Hub — part of the Aura Ecosystem.

## License

See the repository license file for the applicable project terms.
