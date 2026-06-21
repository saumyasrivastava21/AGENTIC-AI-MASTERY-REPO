KNOWLEDGE_BASE = {
    "agent": """
An AI agent is an LLM-based system that can reason, choose tools, take actions,
observe outputs, and generate final answers.
""",
    "rag": """
RAG stands for Retrieval-Augmented Generation. It retrieves external knowledge
from documents, vector databases, or search tools before generating an answer.
""",
    "langchain": """
LangChain is a framework for building LLM applications using chat models,
prompt templates, tools, output parsers, retrievers, and chains.
""",
    "langgraph": """
LangGraph is used to build stateful, controllable, multi-step agent workflows
using nodes, edges, state, and conditional routing.
""",
    "yolo": """
YOLO is a real-time object detection family used for detection, segmentation,
tracking, and computer vision applications.
"""
}


def research_search_tool(query: str) -> str:
    query_lower = query.lower()
    results = []

    for key, value in KNOWLEDGE_BASE.items():
        if key in query_lower:
            results.append(value.strip())

    if not results:
        return (
            "No exact knowledge-base result found. "
            "Try asking about agent, RAG, LangChain, LangGraph, or YOLO."
        )

    return "\n\n".join(results)