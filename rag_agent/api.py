import os
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from ingest import ingest_pdf
from query import ask_question
from vector_store import clear_vector_store
from schemas import AskRequest, AskResponse, UploadResponse

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "uploads"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="Day 3 Advanced RAG Agent",
    description="Production-style PDF RAG API using FastAPI, ChromaDB, NVIDIA LLM, and citations.",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "app": "Day 3 Advanced RAG Agent",
        "status": "running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "vector_db": "ChromaDB",
        "llm": "NVIDIA",
        "rag": "enabled"
    }


@app.post("/upload", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    save_path = UPLOAD_DIR / file.filename

    try:
        content = await file.read()
        save_path.write_bytes(content)

        chunks = ingest_pdf(str(save_path))

        return UploadResponse(
            filename=file.filename,
            saved_path=str(save_path),
            chunks_created=chunks,
            message="PDF uploaded and ingested successfully."
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    try:
        return ask_question(
            question=request.question,
            top_k=request.top_k
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.delete("/clear")
def clear_db():
    clear_vector_store()

    return {
        "message": "Vector database cleared successfully."
    }