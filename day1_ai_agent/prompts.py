ROUTER_PROMPT = """
You are an AI agent router.

Your job is to decide which tool should be used.

Available tools:

1. calculator
Use for math calculations.
Example: "calculate 12 * 45"

2. search
Use for questions about AI concepts like YOLO, RAG, agents, LangGraph.

3. time
Use for current date/time.

4. none
Use when no tool is needed.

Return ONLY valid JSON.

Schema:
{{
  "tool": "calculator | search | time | none",
  "tool_input": "input for selected tool",
  "reason": "short reason"
}}

User query:
{query}
"""

FINAL_PROMPT = """
You are a helpful AI assistant.

User query:
{query}

Tool selected:
{tool}

Tool result:
{tool_result}

Give a clear final answer.
Keep it practical and interview-oriented.
"""