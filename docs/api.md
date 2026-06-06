# Anthropic API Usage

## Client setup
```python
from src.client import get_client
client = get_client()  # reads ANTHROPIC_API_KEY from .env
```

## Messages API (generation)
```python
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "..."}],
)
text = resp.content[0].text
```

## Tool use (agents)
```python
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    tools=[{"name": "...", "description": "...", "input_schema": {...}}],
    messages=messages,
)
# resp.stop_reason == "tool_use" → call tools, append results, loop
# resp.stop_reason == "end_turn" → done
```

## Stop reasons
| stop_reason | Meaning |
|-------------|---------|
| `end_turn` | Model finished naturally |
| `tool_use` | Model wants to call a tool |
| `max_tokens` | Hit token limit — increase max_tokens |
| `stop_sequence` | Hit a custom stop sequence |

## Token counting
```python
resp.usage.input_tokens   # prompt tokens
resp.usage.output_tokens  # completion tokens
```

## Costs (claude-sonnet-4-6, as of 2026-06)
Log `resp.usage` in experiments to track cost per run.
