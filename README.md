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

## Prerequisites

- Python 3.10+
- Ollama with a local model (`mistral` or `llama3`) downloaded
- Local markdown files under the `docs/` directory
- Hugging Face account (optional fallback)
- `.env` file for model configuration

## Security, Compliance & Privacy

- No cloud dependency unless Hugging Face fallback is triggered.
- `.env` is excluded via `.gitignore`.
- The system can run in secure, offline environments.
- Ideal for enterprise settings with compliance restrictions.

## Tasks & Step-by-Step Instructions

### Install dependencies

```bash
pip install -r requirements.txt

Start Ollama

ollama run mistral
# or
ollama serve

Run in test mode (no LLM call)

python -m cli.agent question --file docs/sample.md --test-mode -- "What is the purpose of this repo?"

Run full agentic reasoning

python -m cli.agent question --file docs/sample.md -- "How does this system chunk and reason over markdown?"

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



Dependencies, Risks & Escalation Path

Relies on:

ollama for LLM inference

LangGraph (via LangChain) for structured reasoning

Typer for CLI interface

FAISS for optional vector storage (future-ready)


Risks:

Model not loading

Missing .env

Markdown malformed or missing expected headers



Success Metrics & Outcomes

CLI returns formatted response successfully

Agents process chunks using the full flow

Output aligns with test vs production flows consistently


Resources & References

Ollama Docs

LangGraph

LangChain

Typer CLI


Last Reviewed / Last Updated

Date: 2025-08-04

Maintainer: Shailesh Rawat


Let me know if you'd like to add Mermaid diagrams or split this into multiple files for `docs/`, `agents/`, or `cli/`.

