# Aura Prompt Specification (APS-1.0)

The **Aura Prompt Specification** defines the standard schema and execution context for prompts utilized across the Aura Ecosystem, Web4 nodes, and LMLM runtimes.

## Frontmatter Schema

Every prompt file inside `prompts/` or `promptcards/` must start with a YAML frontmatter block:

```yml
id: "lmlm-code-gen-v1"
name: "LMLM Multi-Language Code Generator"
version: "1.0.0"
author: "Seriki Yakub <qubuhub@googlemanagers.com>"
ecosystem: "aura-web4"
target_engine: "lmlm"
tags: ["code-generation", "multi-language", "privacy-first"]
parameters:
  temperature: 0.2
  max_tokens: 4096
  top_p: 0.95
---
```

### 3. Sample Prompt (`prompts/lmlm/code_generator.md`)
```Rmd
---
id: "lmlm-code-gen-v1"
name: "LMLM Multi-Language Code Generator"
version: "1.0.0"
author: "Seriki Yakub"
ecosystem: "aura-web4"
target_engine: "lmlm"
tags: ["code-generation", "multi-language", "privacy-first"]
---

# System Context
You are an expert AI software architect operating inside the LMLM (Local Multi-Language AI Model) environment. Your goal is to write clean, modular, production-ready code with zero external telemetry.

## Instructions
1. Analyze the requested tech stack: `{{tech_stack}}`.
2. Generate optimized, secure, and fully typed code for the task: `{{task_description}}`.
3. Include relevant unit tests and configuration files where necessary.

## Input Payload
- **Project**: `{{project_name}}`
- **Requirements**: 
{{requirements}}
```
