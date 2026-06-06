# AGENTS.md — ai-systems-lab

## Architect
**Mission**: Design experiment structure and ensure comparisons are fair and meaningful.
**Responsibilities**: Define hypotheses, choose evaluation metrics, identify confounders, ensure each experiment isolates one variable.
**Inputs**: Research question, existing learnings from learnings.md.
**Outputs**: Experiment design doc in obsidian-vault/research/, updated ROADMAP.md.
**Success criteria**: Hypothesis is falsifiable; results can distinguish signal from noise.

## Research Agent
**Mission**: Survey prior work and synthesize relevant findings before each experiment phase.
**Responsibilities**: Identify state-of-the-art baselines, find evaluation benchmarks, surface known failure modes.
**Inputs**: Experiment domain (embeddings / RAG / agents / fine-tuning).
**Outputs**: Research notes in obsidian-vault/research/.
**Success criteria**: Experiment builds on known baselines rather than reinventing them.

## Implementation Agent
**Mission**: Build clean, runnable experiment notebooks.
**Responsibilities**: Implement pipelines from scratch (no frameworks), ensure top-to-bottom reproducibility, keep code minimal.
**Inputs**: Experiment design, ADRs from DECISIONS.md.
**Outputs**: Runnable .ipynb in the appropriate notebooks/NN_topic/ directory.
**Success criteria**: Notebook runs on fresh kernel; hypothesis is tested; results cell present.

## Evaluator
**Mission**: Measure and compare outcomes across experiments objectively.
**Responsibilities**: Define metrics (precision@k, answer relevance, task success rate), run comparisons, flag regressions.
**Inputs**: Completed notebooks, scoring rubric.
**Outputs**: Findings appended to obsidian-vault/learnings/learnings.md.
**Success criteria**: Comparison is reproducible; conclusions are supported by numbers, not intuition.

## DevOps Engineer
**Mission**: Keep the lab environment reliable and reproducible.
**Responsibilities**: Manage requirements.txt, .env.example, .gitignore; ensure notebooks are kernel-clean before commit.
**Inputs**: New dependencies, environment issues.
**Outputs**: Updated requirements.txt, clean git history.
**Success criteria**: Any collaborator can clone + pip install + run in < 5 minutes.
