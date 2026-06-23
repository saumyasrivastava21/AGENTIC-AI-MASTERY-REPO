from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from vector_store import get_vector_store
from logger import log_event


def ingest_pdf(pdf_path: str) -> int:
    path = Path(pdf_path.strip().strip('"'))

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(str(path))
    docs = loader.load()

    valid_docs = []

    for doc in docs:
        text = doc.page_content.strip()

        if not text:
            continue

        doc.page_content = text
        doc.metadata["filename"] = path.name
        doc.metadata["source"] = str(path)
        valid_docs.append(doc)

    if not valid_docs:
        raise ValueError(
            "No extractable text found in this PDF. "
            "This PDF may be scanned/image-based. Try a text-based PDF or add OCR."
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_documents(valid_docs)

    chunks = [
        chunk for chunk in chunks
        if chunk.page_content and chunk.page_content.strip()
    ]

    if not chunks:
        raise ValueError(
            "PDF text was loaded, but chunking produced zero valid chunks."
        )

    store = get_vector_store()
    store.add_documents(chunks)

    log_event(
        "PDF_INGESTED",
        f"file={path.name}, pages={len(docs)}, valid_pages={len(valid_docs)}, chunks={len(chunks)}"
    )

    return len(chunks)