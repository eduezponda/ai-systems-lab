# Patterns

Recurring implementation patterns identified across experiments.
Append as patterns emerge.

---

## Pattern: Retrieve → Prompt → Evaluate
The core loop for all RAG experiments.
```
chunks = retrieve(query, corpus, k)
answer = client.messages.create(model=..., messages=[{context + query}])
score = evaluate(answer, ground_truth)
```

## Pattern: Tool-use agent loop
```
messages = [user_task]
while stop_reason != "end_turn":
    resp = client.messages.create(tools=TOOLS, messages=messages)
    messages.append(assistant: resp.content)
    if tool_calls:
        results = [run_tool(call) for call in tool_calls]
        messages.append(user: tool_results)
return final_text
```
