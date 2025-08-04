# Soothsayer Suite

## Overview

The Soothsayer Suite is a modular, local-first AI system designed to translate unstructured markdown documentation into structured, queryable insights using agentic reasoning. It is optimized for clarity, control, and enterprise readiness.

## Why It Matters

Most AI tools are either too abstract for internal teams or too rigid to adapt to enterprise communication needs. Soothsayer bridges this gap by letting documentation speak—through structured reasoning, chunking, and aligned language models. It can power documentation Q&A, changelog generation, reasoning tasks, and more.

## Audience, Scope & Personas

This suite is intended for:

- Developers and DevOps engineers working with AI tools and LangChain/CrewAI
- Technical writers and content designers working with Markdown documentation
- Change managers and product teams looking to make their documentation queryable and explainable
- Anyone building practical AI agents with transparent workflows

## Prerequisites

- Python 3.10+
- `ollama` running locally with a downloaded model (`mistral` or `llama3`)
- Hugging Face account (optional fallback)
- Markdown files placed in a `docs/` directory

## Security, Compliance & Privacy

- The system runs locally and does not send data unless Hugging Face fallback is used.
- All models used can be containerized or hosted internally to ensure data compliance.
- No sensitive tokens are hardcoded. `.env` is required but is `.gitignore`d.

## Tasks & Step-by-Step Instructions

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Launch Ollama (required)

ollama run mistral

Or ensure Ollama is serving:

ollama serve

### Step 3: Test CLI locally

python -m cli.agent question --file docs/sample.md --test-mode -- "What is the purpose of this repo?"

### Step 4: Run full reasoning mode (LLM-powered)

python -m cli.agent question --file docs/sample.md -- "How does the agent process information?"

## Access Control & Permissions (RBAC guidelines)

This system is local and CLI-driven. If deployed in a shared environment:

- Restrict markdown source file access via filesystem permissions
- Restrict LLM usage to approved models and routes
- Add access guards around sensitive content directories if needed

## Practical Examples & Templates

**✅ Good usage**

python -m cli.agent question --file docs/onboarding.md -- "Summarize our onboarding flow"

**❌ Misusage**

python -m cli.agent question --file secret_keys.txt -- "Are these valid?"

## Known Issues & Friction Points

- If Ollama is not running, the fallback to Hugging Face may fail if the model is unavailable.
- Parsing very large markdown files may cause long processing times.
- Some responses may not retain formatting in terminals without Markdown rendering.

## Tips & Best Practices

- Use smaller, scoped markdowns to improve retrieval quality.
- Use clear section headings in your `.md` files (`## Feature`, `### Purpose`) for better chunk detection.
- Always validate local Ollama before relying on Hugging Face.

## Troubleshooting Guidance

- **Error: Ollama not available**
  - Ensure `ollama serve` is running and port 11434 is free.

- **Error: [FATAL] Both Ollama and Hugging Face failed**
  - Check Hugging Face model availability or use test mode.

- **No formatted output**
  - Check if the markdown file contains proper headings and readable content.

## Dependencies, Risks & Escalation Path

- Relies on local Ollama server or public Hugging Face models.
- Internet access is required only for fallback or model downloading.
- Risks include unstructured input files or malformed Markdown.

## Success Metrics & Outcomes

- CLI runs without failure on all supported commands.
- Responses show accurate, chunk-based LLM output.
- Full agent reasoning workflow is traceable, testable, and extendable.

## Resources & References

- [Ollama Documentation](https://ollama.com)
- [LangGraph](https://docs.langchain.com/langgraph/)
- [Typer](https://typer.tiangolo.com)
- [LangChain](https://docs.langchain.com)

## Last Reviewed / Last Updated

- **Date:** 2025-08-04  
- **Maintainer:** Shailesh Rawat

