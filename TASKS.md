# TASKS.md — ai-systems-lab

## Active
- [ ] Complete `01_embeddings/embeddings_basics.ipynb` — wire up Anthropic embeddings, run cosine similarity across test pairs
- [ ] Complete `02_rag/rag_naive.ipynb` — add evaluation: run 5 questions, score answer relevance manually
- [ ] Complete `03_agents/file_agent.ipynb` — test on real repo structure, log tool call traces

## Backlog
- [ ] `01_embeddings/embedding_clustering.ipynb` — k-means cluster of document set, visualize with UMAP
- [ ] `02_rag/rag_dense.ipynb` — replace keyword retrieval with embedding similarity; compare vs. naive
- [ ] `02_rag/rag_reranking.ipynb` — add cross-encoder re-ranking step; measure precision@k delta
- [ ] `03_agents/react_agent.ipynb` — implement ReAct loop (reason + act); compare task success vs. single-shot
- [ ] `04_fine_tuning/dataset_prep.ipynb` — build training dataset from experiment outputs

## Done
- [x] Initialize repo with directory structure and starter notebooks
- [x] Bootstrap project structure (obsidian-vault, docs, root files)
