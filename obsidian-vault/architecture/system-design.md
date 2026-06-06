# System Design

## High-level architecture

```mermaid
graph TD
    NB[Jupyter Notebook] --> SRC[src/client.py]
    SRC --> API[Anthropic API]
    NB --> DATA[data/]
    NB --> LEARN[obsidian-vault/learnings/learnings.md]

    subgraph Experiment domains
        E1[01_embeddings]
        E2[02_rag]
        E3[03_agents]
        E4[04_fine_tuning]
    end

    NB --- E1 & E2 & E3 & E4
```

## Data flow per experiment

```mermaid
sequenceDiagram
    participant NB as Notebook
    participant CLIENT as src/client.py
    participant API as Anthropic API
    NB->>NB: Load/generate corpus
    NB->>CLIENT: get_client()
    NB->>API: messages.create() / embeddings
    API-->>NB: Response
    NB->>NB: Measure & compare
    NB->>NB: Append to learnings.md
```

## Deliberate constraints
- No vector database — NumPy in-memory for Phase 1
- No framework abstractions — every API call is explicit
- Single shared client helper (`src/client.py`) — all else is notebook-local
