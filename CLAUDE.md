# CLAUDE.md — ai-systems-lab

Project-level conventions. Global rules live in ~/.claude/CLAUDE.md.

## Stack
- Python 3.11+ · Jupyter · Anthropic API (claude-sonnet-4-6 default)
- No orchestration frameworks — raw implementations only
- Dependencies: requirements.txt; secrets: .env (copy from .env.example)

## Experiment conventions
- One notebook = one hypothesis. State the hypothesis in the first markdown cell.
- Each notebook must be runnable top-to-bottom with a fresh kernel.
- Measure before concluding. Every experiment ends with a results cell (metrics table, plot, or printed comparison).
- Numbered directories enforce ordering: 01_embeddings → 02_rag → 03_agents → 04_fine_tuning

## Adding a new experiment
1. Create `notebooks/NN_topic/experiment_name.ipynb`
2. Add the experiment to obsidian-vault/sessions/YYYY-MM-DD.md
3. Append findings to obsidian-vault/learnings/learnings.md when done

## Model defaults
```python
MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 1024
```
Override per-notebook when a specific capability requires a different model.

## Knowledge management
- Consult `obsidian-vault/learnings/learnings.md` before designing a new experiment
- Create/append `obsidian-vault/sessions/YYYY-MM-DD.md` at the start of every session
