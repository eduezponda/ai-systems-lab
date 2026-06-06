# DECISIONS.md — ai-systems-lab

## ADR-001 — No orchestration frameworks
**Date**: 2026-06-06
**Status**: Accepted
**Decision**: Use raw Anthropic SDK only. No LangChain, LlamaIndex, or similar.
**Rationale**: Frameworks abstract away the mechanics we're trying to understand. Raw implementation forces explicit reasoning about each design choice.
**Consequence**: More boilerplate per notebook; deeper understanding of tradeoffs.

## ADR-002 — Jupyter as primary experiment surface
**Date**: 2026-06-06
**Status**: Accepted
**Decision**: All experiments live in Jupyter notebooks, not standalone Python scripts.
**Rationale**: Iterative exploration is faster in notebooks; inline outputs make comparison easy.
**Consequence**: Notebooks must be kept runnable top-to-bottom (no hidden state assumptions).

## ADR-003 — claude-sonnet-4-6 as default model
**Date**: 2026-06-06
**Status**: Accepted
**Decision**: Use `claude-sonnet-4-6` unless an experiment specifically requires a different capability.
**Rationale**: Best balance of capability and latency for interactive experiments.
**Consequence**: Results are model-specific; note model version in every experiment's results cell.

## ADR-004 — No vector database in Phase 1
**Date**: 2026-06-06
**Status**: Accepted
**Decision**: Implement retrieval with in-memory NumPy operations in Phase 1.
**Rationale**: Eliminate infrastructure complexity while learning retrieval fundamentals.
**Consequence**: Not scalable beyond ~10k documents; intentional.
