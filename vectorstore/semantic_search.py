from vectorstore.index_manager import (
    vectorstore,
)


def semantic_search(
    query: str,
    k: int = 5,
):

    results = vectorstore.similarity_search_with_score(
        query=query,
        k=k,
    )

    return results
