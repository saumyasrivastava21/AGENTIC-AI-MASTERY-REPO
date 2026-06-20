import math
from datetime import datetime

# calculator function that evaluates mathematical expressions safely
def calculator(expression: str) -> str:
    try:
        allowed_names = {
            "sqrt": math.sqrt,
            "pow": pow,
            "abs": abs,
            "round": round,
            "min": min,
            "max": max
        }

        result = eval(
            expression,
            {"__builtins__": {}}, # restrict access to built-in functions
            allowed_names
        ) #So user cannot run unsafe code like file delete/import.

        return str(result)

    except Exception as e:
        return f"Calculator error: {str(e)}"


def mock_search(query: str) -> str:
    database = {
        "yolo": "YOLO is a real-time object detection family used for detection, segmentation, and tracking.",
        "rag": "RAG means Retrieval-Augmented Generation. It retrieves external context before answering.",
        "agent": "An AI agent uses an LLM plus tools to complete tasks through reasoning and actions.",
        "langgraph": "LangGraph is used to build stateful, multi-step, controllable agent workflows."
    }

    query_lower = query.lower()

    for key, value in database.items():
        if key in query_lower:
            return value

    return "No exact result found. Try query with YOLO, RAG, agent, or LangGraph."


def get_current_time(_: str = "") -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def summarize_text(text: str) -> str:
    if len(text) <= 200:
        return text

    return text[:200] + "..."