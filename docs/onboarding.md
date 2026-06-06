# Onboarding

## Prerequisites
- Python 3.11+
- Anthropic API key (get one at console.anthropic.com)

## Setup (5 minutes)
```bash
# 1. Clone
git clone <repo-url> ai-systems-lab
cd ai-systems-lab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
cp .env.example .env
# edit .env → set ANTHROPIC_API_KEY=sk-ant-...

# 4. Launch Jupyter
jupyter notebook
```

## First run
Open `notebooks/02_rag/rag_naive.ipynb` — it's the most self-contained experiment.
Run all cells top-to-bottom. You should see a generated answer in the last cell.

## Key files to read first
1. [CONTEXT.md](../CONTEXT.md) — what this project is and what questions it answers
2. [CLAUDE.md](../CLAUDE.md) — conventions when working with Claude on this repo
3. [obsidian-vault/learnings/learnings.md](../obsidian-vault/learnings/learnings.md) — accumulated findings

## Adding a new experiment
1. Create `notebooks/NN_topic/experiment_name.ipynb`
2. State hypothesis in first markdown cell
3. Implement, measure, conclude
4. Append findings to learnings.md
5. Mark task done in TASKS.md
