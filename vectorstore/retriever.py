from vectorstore.chroma_client import vectorstore


def retrieve_examples(query: str, k=2):

    results = vectorstore.similarity_search(query, k=k)

    examples = []

    for result in results:

        examples.append(
            {"query": result.page_content, "response": result.metadata["response"]}
        )

    return examples
