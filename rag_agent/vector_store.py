import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from langchain_chroma import Chroma

from embeddings import get_embedding_model

load_dotenv()


def get_vector_store():
    chroma_dir = os.getenv("CHROMA_DIR", "data/chroma")
    collection_name = os.getenv("COLLECTION_NAME", "research_docs")

    Path(chroma_dir).mkdir(parents=True, exist_ok=True)

    return Chroma(
        collection_name=collection_name,
        embedding_function=get_embedding_model(),
        persist_directory=chroma_dir
    )


def clear_vector_store():
    chroma_dir = os.getenv("CHROMA_DIR", "data/chroma")

    if Path(chroma_dir).exists():
        shutil.rmtree(chroma_dir)

    Path(chroma_dir).mkdir(parents=True, exist_ok=True)

    return True