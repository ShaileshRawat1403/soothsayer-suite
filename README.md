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