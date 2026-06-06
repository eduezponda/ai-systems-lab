# CONTEXT.md — ai-systems-lab

## What is this project?
A hands-on empirical lab for comparing retrieval and agent architectures.
Every experiment is implemented from scratch (no LangChain, no LlamaIndex) to understand tradeoffs firsthand.

## Core questions
1. How much does retrieval strategy (keyword vs. dense vs. hybrid) affect answer quality in RAG?
2. What is the minimum viable tool-use agent for file-based tasks? Where does it break?
3. How do fine-tuned models compare to prompted models on narrow tasks?
4. What embedding similarity metrics work best for semantic search at small scale?

## Scope
| In scope | Out of scope |
|---|---|
| Raw Python + Jupyter experiments | Production-ready services |
| Anthropic API (Claude models) | Multi-provider comparison |
| Small datasets (< 10k docs) | Large-scale retrieval (vector DBs) |
| Qualitative + quantitative eval | Automated CI/eval pipelines |

## Current phase
**Phase 1 — Foundations**: embeddings basics, naive RAG, minimal file agent.

## Key files
- `src/client.py` — shared `get_client()` → `Anthropic`
- `notebooks/` — all experiments
- `obsidian-vault/learnings/learnings.md` — accumulated findings
