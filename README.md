---
title: Soothsayer Suite
description: Local-first agentic AI system for structured reasoning over Markdown documentation
last_updated: 2025-08-04
maintainer: Shailesh Rawat
---

# Soothsayer Suite

## Overview

The Soothsayer Suite is a modular, local-first agentic AI system designed to convert unstructured Markdown files into structured, queryable insights. It uses prompt-driven workflows, local LLMs, and content chunking to enable accurate and explainable reasoning over internal documentation.

## Why It Matters

Documentation is often overlooked as a source of real-time intelligence. Soothsayer turns your `.md` files into a living knowledge source—allowing you to query onboarding docs, architecture decisions, or changelogs using natural language, without relying on cloud-based black-box models.

## Audience, Scope & Personas

This system is built for:

- **Developers & DevOps Engineers**: to integrate documentation reasoning into CI/CD or CLI workflows.
- **Technical Writers & Product Teams**: to make internal docs queryable and explainable.
- **Change Managers & Business Analysts**: to ensure communication clarity and auditability from documentation.

Here is the fully detailed and clean Prerequisites section, rewritten to match your GitHub documentation style and make it understandable for developers, DevOps engineers, and non-technical contributors alike.

## Prerequisites

Before running Soothsayer Suite, ensure the following system and environment dependencies are installed and correctly configured.

---

### 🛠️ System Requirements

- **Python:** `>=3.10`  
  (Recommended: 3.10 or 3.11 — avoid 3.12+ unless compatibility is confirmed)
- **OS:** macOS, Linux, or WSL-compatible Windows

---

### 📦 Python Packages

Install all required dependencies using:

```bash
pip install -r requirements.txt
```
Minimum versions confirmed:
```bash
typer>=0.9.0

requests>=2.31.0

langgraph>=0.0.24

sentence-transformers>=2.2.2

faiss-cpu>=1.7.4 (optional, for future vectorstore use)

numpy>=1.24.0

python-dotenv>=1.0.1
```

---

### LLM Backends

Primary (Local First)

Ollama — must be installed and running on port 11434
Install guide

```bash
ollama run mistral
```
Test Ollama service:

curl http://localhost:11434/api/tags

You should see model metadata in response.

Secondary (Fallback)

Hugging Face Inference API
Add your token to .env file:

```python
HF_API_KEY=your_token_here
```

---

📄 Project File Structure

Place your context files in docs/ directory as .md (Markdown)

Each file should follow a semantic structure (e.g., headers like ## Purpose)



---

✅ Quick Setup Checklist

Requirement	Installed?	Notes

Python >= 3.10	✅ / ❌	Use python3 --version
Virtual environment	✅ / ❌	Recommended
ollama installed	✅ / ❌	ollama run mistral must succeed
Models downloaded	✅ / ❌	Use ollama list
.env file configured	✅ / ❌	For Hugging Face fallback
Markdown files ready	✅ / ❌	In docs/*.md



---


Access Control & Permissions (RBAC guidelines)

Local execution only unless deployed as a service.

Ensure .md files are permissioned via OS-level ACLs.

Sensitive documentation should not be passed to fallback inference.


Practical Examples & Templates

✅ Ask what a file contains:

python -m cli.agent question --file docs/onboarding.md -- "Summarize the onboarding process"

❌ Avoid using on unstructured or binary content:

python -m cli.agent question --file docs/secrets.txt -- "List all passwords"

Known Issues & Friction Points

Large files may exceed chunking capacity.

Ollama model must be pre-downloaded and ready.

Hugging Face fallback may return inconsistent results if model mismatch occurs.


Tips & Best Practices

Structure your markdown clearly (##, ###, bullet points).

Use test mode to validate chunking before querying with LLM.

Validate Ollama with curl http://localhost:11434/api/tags.


Troubleshooting Guidance

Ollama not responding?

Run ollama serve or ollama run mistral

Ensure port 11434 is not blocked.


LLM errors or fallback issues?

Check internet access.

Use --test-mode to validate logic path.



### Dependencies, Risks & Escalation Path

Relies on:

ollama for LLM inference

LangGraph (via LangChain) for structured reasoning

Typer for CLI interface

FAISS for optional vector storage (future-ready)


Risks:

Model not loading

Missing .env 

Markdown malformed or missing expected headers

API keys mismanagement if not vigilant



### Success Metrics & Outcomes

CLI returns formatted response successfully

Agents process chunks using the full flow

Output aligns with test vs production flows consistently


### Resources & References

Ollama Docs

LangGraph

LangChain

Typer CLI


Last Reviewed / Last Updated

Date: 2025-08-04

Maintainer: Shailesh Rawat
