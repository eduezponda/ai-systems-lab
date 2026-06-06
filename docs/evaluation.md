# Evaluation

## Metrics by domain

### Retrieval / Embeddings
- **Recall@k** — what fraction of relevant docs appear in top-k results
- **MRR** — mean reciprocal rank of the first relevant result
- **Cosine similarity distribution** — histograms of similar vs. dissimilar pairs

### RAG answer quality
- **Manual relevance score** (1–5, rubric in docs/experiments.md)
- **Faithfulness** — is the answer grounded in the retrieved context? (binary)
- **Latency** — wall-clock time from query to answer

### Agents
- **Task success rate** — % of tasks completed correctly end-to-end
- **Tool calls per task** — efficiency metric
- **Error rate** — % of runs that error or loop infinitely

## How to record results
Every notebook must end with a results cell:
```python
results = {
    "experiment": "rag_naive",
    "model": MODEL,
    "date": "2026-06-06",
    "n_queries": 5,
    "avg_relevance": 3.4,
    "avg_faithfulness": 0.8,
    "avg_latency_s": 1.2,
}
import json; print(json.dumps(results, indent=2))
```

Append key findings to `obsidian-vault/learnings/learnings.md`.
