from llm import get_llm
from prompts import RAG_PROMPT
from vector_store import get_vector_store
from schemas import AskResponse, Citation
from logger import log_event


def build_context_and_citations(docs):
    context_blocks = []
    citations = []

    for index, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        filename = doc.metadata.get("filename", source)
        page = int(doc.metadata.get("page", 0)) + 1

        preview = doc.page_content[:220].replace("\n", " ")

        context_blocks.append(
            f"""
[Chunk {index}]
Source: {filename}
Page: {page}

{doc.page_content}
"""
        )

        citations.append(
            Citation(
                source=filename,
                page=page,
                chunk_preview=preview
            )
        )

    return "\n\n".join(context_blocks), citations


def ask_question(question: str, top_k: int = 5) -> AskResponse:
    store = get_vector_store()

    retriever = store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": top_k,
            "fetch_k": max(10, top_k * 3),
            "lambda_mult": 0.7
        }
    )

    docs = retriever.invoke(question)

    context, citations = build_context_and_citations(docs)

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    llm = get_llm(temperature=0.1)
    answer = llm.invoke(prompt).content

    log_event(
        "QUESTION_ASKED",
        f"question={question}, chunks={len(docs)}"
    )

    return AskResponse(
        question=question,
        answer=answer,
        retrieved_chunks=len(docs),
        citations=citations
    )