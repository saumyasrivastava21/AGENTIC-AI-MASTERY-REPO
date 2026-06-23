from typing import List
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(..., min_length=3)
    top_k: int = Field(default=5, ge=1, le=10)


class Citation(BaseModel):
    source: str
    page: int
    chunk_preview: str


class AskResponse(BaseModel):
    question: str
    answer: str
    retrieved_chunks: int
    citations: List[Citation]


class UploadResponse(BaseModel):
    filename: str
    saved_path: str
    chunks_created: int
    message: str