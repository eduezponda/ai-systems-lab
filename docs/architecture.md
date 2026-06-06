# Architecture

## Repository layout

```
ai-systems-lab/
├── notebooks/
│   ├── 01_embeddings/   ← embedding generation & similarity
│   ├── 02_rag/          ← retrieve-then-generate pipelines
│   ├── 03_agents/       ← tool-use agent implementations
│   └── 04_fine_tuning/  ← fine-tuning experiments
├── src/
│   └── client.py        ← shared Anthropic client
├── data/                ← local datasets (gitignored except .gitkeep)
├── obsidian-vault/      ← knowledge management
└── docs/                ← this directory
```

## Experiment pipeline

```mermaid
flowchart LR
    H[Hypothesis] --> I[Implement notebook]
    I --> R[Run & measure]
    R --> C{Better than baseline?}
    C -- yes --> L[Append to learnings.md]
    C -- no --> L
    L --> N[Next experiment]
```

## Dependency graph

```mermaid
graph TD
    ENV[.env / ANTHROPIC_API_KEY] --> CLIENT[src/client.py]
    CLIENT --> NB[All notebooks]
    REQ[requirements.txt] --> NB
```
