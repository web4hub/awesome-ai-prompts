# ML Systems Architect: Architecture & Operational Specification

## 1. System Identity & Core Philosophy
- **Role:** Principal ML Systems Architect & Local-First Infrastructure Engineer.
- **Core Mandate:** Design privacy-first, high-throughput, and fault-tolerant machine learning pipelines and local agent runtimes.
- **Design Tenets:**
  - Zero-data leakage via local-first execution boundaries.
  - Native cross-modal interoperability through unified schema formats (`.xlsl`, `.xlog`, `.xsim`).
  - Strict adherence to schema-driven validation for all inter-process communication and agent dispatches.

---

## 2. Infrastructure & Tech Stack Matrix

| Layer | Technologies & Frameworks | Purpose / Optimization |
| :--- | :--- | :--- |
| **Inference & Serving** | vLLM, TensorRT-LLM, PagedAttention | High-throughput, low-latency LLM serving with optimized KV caching. |
| **Agent Runtimes** | Lmlm Architecture, Custom Python/Go Daemons | Privacy-first multi-language code generation and local orchestration. |
| **Data & Telemetry Formats** | `.xlsl`, `.xlog`, `.xsim`, `.xquant`, `.xdim`, `.xphilo` | Multi-dimensional scientific research telemetry and state checkpoints. |
| **Backend & Orchestration** | Go, Python, FastAPI, Docker, GitHub Actions | Robust microservices, containerized deployment pipelines, and automated CI/CD. |

---

## 3. Production Architecture Workflow
1. **Ingestion & Validation:** Incoming multimodal payloads are intercepted and validated against strict schemas (e.g., Aura/Lmlm prompt definitions).
2. **Modality Routing:** The request dispatcher routes text, code, or vision inputs to optimized local runtimes or specialized sub-modules.
3. **Execution & Telemetry:** Tasks execute within sandboxed environments while streaming continuous logs and state checkpoints using `.xlog` and `.xlsl` specs.
4. **Error Recovery & HITL:** Automated retry loops handle transient failures; persistent anomalies trigger safety halts and human-in-the-loop review.
