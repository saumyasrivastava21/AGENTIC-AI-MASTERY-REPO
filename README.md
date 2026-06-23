
# 🚀 Agentic AI Mastery

A hands-on journey to master **AI Agents, RAG, LangChain, LangGraph, and production-style LLM workflows**.

This repo is focused on learning by building — from a basic tool-calling agent to self-correcting LangGraph workflows.

---

## 📌 Progress

| Day | Project | Core Learning |
|---|---|---|
| Day 1 | Tool Calling AI Agent | LLM + tools + agent loop |
| Day 2 | LangChain Structured Router Agent | Pydantic routing + modular tools |
| Day 3 | Advanced PDF RAG Agent | PDF ingestion + ChromaDB + citations |
| Day 4 | LangGraph Self-Correcting Workflow | StateGraph + retries + critic loop |

---

## 🧠 What I Built

### Day 1 — Tool Calling AI Agent

Built an AI agent from scratch using NVIDIA Llama.

**Learned:**
- LLM vs Agent
- Tool calling
- JSON routing
- Agent loop
- Calculator, search, and time tools

**Flow:**

```text
User Query
↓
Tool Decision
↓
Tool Execution
↓
Observation
↓
Final Answer
````

---

### Day 2 — LangChain Structured Router Agent

Built a production-style router agent using LangChain and Pydantic.

**Learned:**

* LangChain chat models
* Structured output
* Pydantic validation
* Router agents
* Safe AST-based calculator
* Logging and modular architecture

**Routes:**

```text
Math Query     → Calculator Tool
Research Query → Search Tool
Coding Query   → Code Helper Tool
Summary Query  → Summarizer Tool
```

---

### Day 3 — Advanced PDF RAG Agent

Built a PDF-based RAG backend with FastAPI and ChromaDB.

**Learned:**

* PDF ingestion
* Chunking with overlap
* Embeddings
* Vector databases
* MMR retrieval
* Citation-based answers
* FastAPI endpoints

**Flow:**

```text
PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Retriever
↓
LLM Answer + Citations
```

---

### Day 4 — LangGraph Self-Correcting Workflow

Built a self-correcting research workflow using LangGraph.

**Learned:**

* StateGraph
* Nodes and edges
* Conditional routing
* Retry loops
* Critic node
* State management
* Production-style workflow logs

**Flow:**

```text
User Query
↓
Planner Node
↓
Research Node
↓
Critic Node
↓
If weak → Retry Node → Research Again
↓
If good → Final Answer
```

---

## 🏗️ Repository Structure

```text
Agentic-AI-Mastery/
│
├── day1_ai_agent/
├── langchain_agent/
├── rag_agent/
├── langgraph_workflow/
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* NVIDIA Llama / ChatNVIDIA
* LangChain
* LangGraph
* Pydantic
* FastAPI
* ChromaDB
* HuggingFace Embeddings
* Docker-ready architecture

---

## ⚙️ Setup

Clone the repo:

```bash
git clone https://github.com/yourusername/Agentic-AI-Mastery.git
cd Agentic-AI-Mastery
```

Create environment:

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies inside each project folder:

```bash
pip install -r requirements.txt
```

Create `.env` from `.env.example`:

```env
NVIDIA_API_KEY=your_nvidia_api_key
NVIDIA_MODEL=meta/llama-3.3-70b-instruct
```

---

## ▶️ Run Projects

### Day 1

```bash
cd day1_ai_agent
python main.py
```

### Day 2

```bash
cd langchain_agent
python main.py
```

### Day 3

```bash
cd rag_agent
python app.py
```

For API:

```bash
uvicorn api:app --reload
```

### Day 4

```bash
cd langgraph_workflow
python main.py
```

---

## 🎯 Key Concepts Covered

* AI Agents
* Tool Calling
* Router Agents
* Structured Output
* Pydantic Validation
* RAG
* Embeddings
* Vector Databases
* ChromaDB
* FastAPI
* LangGraph
* StateGraph
* Conditional Edges
* Retry Loops
* Critic-Based Self-Correction

---

## 📌 Learning Outcome

By Day 4, I built the foundation of production-style Agentic AI systems:

```text
LLM Apps
→ Tool Calling Agents
→ Structured Router Agents
→ RAG Systems
→ Self-Correcting LangGraph Workflows
```

---

## 👨‍💻 Author

**Saumya Srivastava**

AI Engineer | Machine Learning Engineer | Computer Vision Engineer

* AI Research Intern
* Computer Vision + Agentic AI Enthusiast
* 500+ LeetCode Problems

---

⭐ If this repo helps you, feel free to star it.

```
```
