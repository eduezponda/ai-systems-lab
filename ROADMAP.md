# ROADMAP.md — ai-systems-lab

## Phase 1 — Foundations (current)
Goal: working baseline for each experiment domain.

- [x] Repo scaffold + starter notebooks
- [ ] Embeddings: generation, cosine similarity, clustering
- [ ] RAG: naive keyword retrieval → answer quality baseline
- [ ] Agents: minimal file agent with tool use
- [ ] Evaluation: manual scoring rubric for all three domains

## Phase 2 — Comparison experiments
Goal: measure the delta from improving each component.

- [ ] RAG: dense retrieval vs. keyword (embedding similarity swap)
- [ ] RAG: + re-ranking step (cross-encoder)
- [ ] RAG: + query expansion
- [ ] Agents: ReAct loop vs. single-shot prompting
- [ ] Agents: multi-tool agent (file + search + calc)

## Phase 3 — Integration & synthesis
Goal: combine learnings into a coherent retrieval + agent architecture.

- [ ] Hybrid RAG pipeline (keyword + dense + rerank)
- [ ] Agent with RAG retrieval as a tool
- [ ] Evaluation harness: automated scoring across all pipelines

## Phase 4 — Fine-tuning
Goal: understand when fine-tuning helps vs. hurts vs. is unnecessary.

- [ ] Dataset construction from experiment outputs
- [ ] Fine-tuned model eval vs. prompted baseline
- [ ] Cost/quality tradeoff analysis
