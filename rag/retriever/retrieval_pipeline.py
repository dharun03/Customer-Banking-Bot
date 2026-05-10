from rag.retriever.faq_retriever import (
    retrieve_faqs,
)

from rag.judge.llm_judge import (
    validate_retrieval,
)


def run_rag_pipeline(query: str):

    faqs = retrieve_faqs(query)

    if not faqs:
        return None

    context = "\n\n".join(
        [f"Q: {faq['question']}\n" f"A: {faq['answer']}" for faq in faqs]
    )

    is_relevant = validate_retrieval(
        query=query,
        retrieved_context=context,
    )

    if not is_relevant:
        return None

    return {
        "context": context,
        "sources": faqs,
    }
