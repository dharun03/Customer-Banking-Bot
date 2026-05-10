from vectorstore.index_manager import (
    vectorstore,
)


def retrieve_examples(
    query: str,
    k: int = 3,
):

    results = vectorstore.similarity_search_with_score(
        query=query,
        k=k,
        filter={"type": "few_shot"},
    )

    examples = []

    for doc, score in results:

        examples.append(
            {
                "query": doc.page_content,
                "response": doc.metadata.get(
                    "response",
                    "",
                ),
                "score": score,
            }
        )

    return examples
