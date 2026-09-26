# Aura Prompt Specification (APS-1.0)

The **Aura Prompt Specification** defines the standard schema and execution context for prompts utilized across the Aura Ecosystem, Web4 nodes, and LMLM runtimes.

## Frontmatter Schema

Every prompt file inside `prompts/` or `promptcards/` must start with a YAML frontmatter block:

```yaml
---
id: "lmlm-code-gen-v1"
name: "LMLM Multi-Language Code Generator"
version: "1.0.0"
author: "Seriki Yakub <kubu@qubuhub.com>"
ecosystem: "aura-web4"
target_engine: "lmlm"
tags: ["code-generation", "multi-language", "privacy-first"]
parameters:
  temperature: 0.2
  max_tokens: 4096
  top_p: 0.95
---
