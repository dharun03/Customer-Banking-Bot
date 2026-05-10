from vectorstore.index_manager import (
    vectorstore,
)


def retrieve_faqs(
    query: str,
    k: int = 5,
):

    results = vectorstore.similarity_search_with_score(
        query=query,
        k=k,
        filter={"type": "faq"},
    )

    faqs = []

    for doc, score in results:

        faqs.append(
            {
                "question": doc.metadata["question"],
                "answer": doc.metadata["answer"],
                "category": doc.metadata["category"],
                "score": score,
            }
        )

    return faqs
