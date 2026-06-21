# 🚀 Agentic AI Mastery - Day 1 & Day 2

> Building AI Agents from Scratch → LangChain Structured Router Agents

---

## 📌 Overview

This repository contains my Day 1 and Day 2 journey of learning Agentic AI from fundamentals to production-style structured agents.

### Day 1

Built a Tool Calling AI Agent from scratch using NVIDIA Llama.

### Day 2

Built a Production-Style LangChain Structured Router Agent using:

* LangChain
* NVIDIA Llama 3.3 70B
* Pydantic Structured Output
* Tool Routing
* Logging
* Safe Calculator (AST)
* Modular Agent Architecture

---

# 🎯 Learning Objectives

### Day 1

Understanding:

```text
LLM
↓
Tool Calling
↓
Agent Loop
↓
Reasoning
↓
Final Answer
```

### Day 2

Understanding:

```text
LangChain
↓
Prompt Templates
↓
Structured Output
↓
Pydantic
↓
Router Agent
↓
Tool Execution
↓
Logging
```

---

# 🏗️ Project Structure

```text
Agentic-AI-Mastery/
│
├── day1_ai_agent/
│   ├── main.py
│   ├── llm.py
│   ├── tools.py
│   ├── agent.py
│   ├── prompts.py
│   └── .env
│
├── langchain_agent/
│   ├── main.py
│   ├── llm.py
│   ├── schemas.py
│   ├── logger.py
│   ├── prompts.py
│   ├── .env
│   │
│   ├── logs/
│   │
│   ├── tools/
│   │   ├── calculator.py
│   │   ├── search.py
│   │   ├── summarizer.py
│   │   └── code_helper.py
│   │
│   └── agents/
│       ├── router_agent.py
│       └── research_agent.py
│
└── README.md
```

---

# 🧠 Day 1 - Tool Calling AI Agent

## Features

✅ NVIDIA Llama Integration

✅ Tool Calling

✅ JSON-Based Routing

✅ Calculator Tool

✅ Search Tool

✅ Time Tool

✅ Final Answer Generation

✅ CLI Interface

---

## Agent Flow

```text
User Query
↓
Router Prompt
↓
Tool Selection
↓
Tool Execution
↓
Observation
↓
Final Answer
```

---

## Example

### Input

```text
calculate 45 * 12 + 90
```

### Tool Selection

```json
{
  "tool": "calculator",
  "tool_input": "45 * 12 + 90"
}
```

### Output

```text
630
```

---

# 🧠 Day 2 - LangChain Structured Router Agent

## Features

✅ LangChain

✅ ChatNVIDIA

✅ Structured Output

✅ Pydantic Validation

✅ Safe AST Calculator

✅ Research Tool

✅ Coding Tool

✅ Summarizer Tool

✅ Logging

✅ Modular Architecture

---

## Architecture

```text
User Query
↓
Router Agent
↓
Pydantic Schema
↓
Route Selection
↓
Tool Execution
↓
Tool Output
↓
Final LLM Answer
↓
Logging
```

---

# 📦 Routes Supported

### Research

Examples:

```text
Explain RAG
What is LangGraph?
Explain AI Agents
```

---

### Coding

Examples:

```text
Give binary search code
Java DFS template
Python heap implementation
```

---

### Math

Examples:

```text
45 * 12
100/5 + 7
```

---

### Summary

Examples:

```text
Summarize this paragraph
```

---

### General

Fallback route.

---

# 🔐 Safe Calculator

Instead of:

```python
eval()
```

Used:

```python
ast.parse()
```

Benefits:

```text
Safer
Production-friendly
Prevents arbitrary code execution
```

---

# 🛠️ Tech Stack

### LLM

* NVIDIA Llama 3.3 70B

### Frameworks

* LangChain
* Pydantic

### Language

* Python

### Concepts

* Tool Calling
* Structured Output
* Agent Routing
* Prompt Engineering
* Observability
* Logging

---

# 📚 Concepts Learned

## Day 1

* LLM vs Agent
* Tool Calling
* ReAct Pattern
* Agent Loop
* JSON Outputs
* Routing

---

## Day 2

* LangChain
* Pydantic
* Structured Outputs
* Router Agents
* AST Parsing
* Logging
* Modular Design
* Separation of Concerns

---

# 🚀 Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/Agentic-AI-Mastery.git

cd Agentic-AI-Mastery
```

---

## Create Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install langchain
pip install langchain-core
pip install langchain-nvidia-ai-endpoints
pip install python-dotenv
pip install pydantic
```

---

## Environment Variables

Create:

```env
NVIDIA_API_KEY=your_api_key
NVIDIA_MODEL=meta/llama-3.3-70b-instruct
```

---

# ▶️ Run Day 1

```bash
cd day1_ai_agent

python main.py
```

---

# ▶️ Run Day 2

```bash
cd langchain_agent

python main.py
```

---

# 💡 Key Takeaways

### Day 1

Learned how AI agents:

```text
Think
↓
Choose Tool
↓
Execute
↓
Observe
↓
Respond
```

---

### Day 2

Learned how production systems use:

```text
LangChain
Pydantic
Structured Outputs
Safe Tools
Logging
Modular Design
```

---

# 🎯 Next Goals

* RAG Systems
* ChromaDB
* Vector Databases
* LangGraph
* Multi-Agent Systems
* FastAPI Agents
* Agent Memory
* Agent Evaluation
* ResearchPilot AI (Production Project)

---

## 👨‍💻 Author

**Saumya Srivastava**

AI Engineer | Machine Learning Engineer | Computer Vision Engineer

* 500+ LeetCode Problems
* AI Research Intern
* Computer Vision & Agentic AI Enthusiast

⭐ If you found this useful, consider giving the repository a star.
