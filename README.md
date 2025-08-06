---
title: Soothsayer Suite – Prerequisites & Setup
archetype: Reference
owner: "@sans-serif-sentiments/team-agentic-ai"
status: Stable
version: v1.0
last_reviewed: 2025-08-06
tags: [agentic-ai, markdown-processing, local-llm, ollama, langgraph, cli-tools]
---

# Soothsayer Suite – Prerequisites & Setup

---

## Overview

The Soothsayer Suite is a local-first, agentic AI system that enables structured reasoning over internal Markdown documentation using lightweight LLMs, modular chunking, and CLI-based workflows.

This guide outlines the exact tools, versions, and configurations needed to get started with Soothsayer in a secure and reproducible manner. It’s built for both technical and non-technical teams who want to enable document intelligence without relying on cloud-based AI services.

---

## Why It Matters

Too often, internal documentation sits unused because it's hard to navigate, unstructured, or siloed.

Soothsayer transforms `.md` files into a queryable, explainable, and agent-powered system — letting teams reason over docs the same way they’d ask a subject-matter expert.

A proper setup ensures:

- Reproducible local development (no cloud risk)
- Faster time-to-answer for documentation queries
- Auditability, privacy, and alignment with enterprise data governance

---

## Audience, Scope & Personas

### Audience

- Developers and DevOps engineers building automation over documentation
- Technical writers, content strategists, or internal comms teams
- Business analysts and change managers focused on clarity, compliance, and reuse

### Scope

This document covers:

- Tool and environment setup
- Dependency installation
- Markdown structure requirements
- Testing and troubleshooting flows

---

## Prerequisites

The table below outlines the base system and environment requirements for installing and running Soothsayer locally.

| Requirement       | Minimum Version | Notes |
|-------------------|------------------|-------|
| Python            | `>= 3.10`        | Prefer 3.10 or 3.11. Avoid 3.12+ unless validated |
| OS                | macOS, Linux, WSL | Native Windows unsupported; use WSL |
| Virtual Environment | Recommended   | Use `venv` or `conda` for isolation |

### Python Dependencies

Install using:

```bash
pip install -r requirements.txt
```
Package	Minimum Version	Purpose

typer	>= 0.9.0	CLI interface
requests	>= 2.31.0	API and fallback calls
langgraph	>= 0.0.24	Agent control flow (via LangChain)
sentence-transformers	>= 2.2.2	Embeddings and text encoding
faiss-cpu (optional)	>= 1.7.4	Vector search (future support)
numpy	>= 1.24.0	Embedding preprocessing
python-dotenv	>= 1.0.1	Loads fallback config from .env file


---

LLM Configuration

✅ Primary Inference: Ollama (Local)

Component	Command / Description

Install Ollama	Install Guide
Run model	ollama run mistral
Test availability	curl http://localhost:11434/api/tags — should return model metadata


🕸️ Secondary (Fallback): Hugging Face Inference API

Only used if Ollama is not running or unavailable.
To enable:

1. Create a .env file in the project root


2. Add your API token:



HF_API_KEY=your_token_here


---

Project Structure

Place your .md context files inside the docs/ folder.
Each file should use proper Markdown headers such as:

## Purpose
## Workflow
## Risks
## Dependencies

Avoid uploading .txt, .pdf, or non-semantic files.


---

Quick Setup Checklist

Requirement	Status	Verification Command

Python ≥ 3.10	✅ / ❌	python3 --version
Virtual environment	✅ / ❌	python -m venv venv
Requirements installed	✅ / ❌	pip install -r requirements.txt
Ollama installed	✅ / ❌	ollama run mistral
Models downloaded	✅ / ❌	ollama list
.env configured	✅ / ❌	Only if using fallback
Markdown files ready	✅ / ❌	Place in /docs/



---

Access Control & Permissions

This system runs locally and does not upload data to the cloud.

If fallback is triggered, ensure .md files do not contain sensitive information.

Use OS-level access control to manage file visibility.



---

Practical Examples & Templates (✅/❌)

✅ Valid

python -m cli.agent question --file docs/onboarding.md -- "Summarize the onboarding process"

❌ Invalid

python -m cli.agent question --file docs/secrets.txt -- "List all passwords"

> Unstructured files or non-Markdown formats will break chunking and reasoning.




---

Known Issues & Friction Points

Issue	Impact	Resolution

Ollama not running	CLI returns no output	Run ollama serve and validate port 11434
.env misconfigured	Fallback LLM won't load	Ensure HF_API_KEY is correct
Poor Markdown structure	Inaccurate LLM results	Use headers and sections in .md files
Large files or long lists	Chunking errors	Split documents or reduce input size



---

Tips & Best Practices

✅ Do

Use clear headers (##) and logical bullets in all Markdown files

Validate your LLM setup before first query (--test-mode)

Keep .env out of version control (use .gitignore)


❌ Don’t

Use binary or plaintext .txt files

Rely on fallback for private data

Assume your Markdown is readable without testing it



---

Troubleshooting Guidance

Symptom	Likely Cause	Resolution

“No response from CLI”	Ollama not running	Start ollama run mistral
“Fallback doesn’t activate”	Missing .env	Add HF_API_KEY
“Markdown not understood”	Bad structure	Add semantic headers and bullets
“Inference failed silently”	Conflicting Python versions	Use pyenv or virtualenv isolation



---

Dependencies, Risks & Escalation Path

Dependencies

Tool	Role

Ollama	Local LLM inference
LangGraph	Structured agent reasoning
Typer	CLI UX and routing
FAISS (opt)	Vector retrieval backend (future)
dotenv	Loads fallback credentials


Risks

Risk	Mitigation

Fallback runs on sensitive data	Use local-only .md content or disable fallback
Incompatible Markdown files	Validate with --test-mode
Ollama model not loaded	Pre-download mistral and confirm with ollama list



---

Success Metrics & Outcomes

Metric	Threshold

CLI answers returned	✅ Success response within 2 seconds
Chunks processed and routed	✅ Flow traces available if verbose
Structured output generated	✅ Markdown or string output with correct headers
Fallback not triggered (default)	✅ Ollama responds consistently on port 11434



---

Resources & References

Ollama Docs

LangGraph on GitHub

LangChain Overview

Typer CLI Framework

Markdown Best Practices



---

Last Reviewed / Last Updated

Date: August 6, 2025
Maintainer: Shailesh Rawat (PoeticMayhem)
Version: v1.0
Status: ✅ Stable


---

Let me know if you’d like this split into multiple files (e.g., `README.md`, `setup.md`, `troubleshooting.md`) or continue with the next document (e.g., `agent-flow.md`, `security-guidelines.md`, etc.).

