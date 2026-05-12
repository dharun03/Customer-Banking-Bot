from rank_bm25 import BM25Okapi

from vectorstore.index_manager import vectorstore

BM25_STORE = {}


def add_to_bm25_store(
    session_id: str,
    chunks: list[str],
):

    if session_id not in BM25_STORE:

        BM25_STORE[session_id] = {
            "documents": [],
            "bm25": None,
        }

    BM25_STORE[session_id]["documents"].extend(chunks)

    tokenized_docs = [doc.split() for doc in BM25_STORE[session_id]["documents"]]

    BM25_STORE[session_id]["bm25"] = BM25Okapi(tokenized_docs)


def retrieve_document_context(
    query: str,
    session_id: str,
    k: int = 3,
):

    bm25_results = []

    if session_id in BM25_STORE:

        bm25 = BM25_STORE[session_id]["bm25"]

        docs = BM25_STORE[session_id]["documents"]

        scores = bm25.get_scores(query.split())

        ranked = sorted(
            zip(docs, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        bm25_results = [doc for doc, _ in ranked[:k]]

    vector_results = vectorstore.similarity_search(
        query=query,
        k=k,
        filter={
            "type": "document",
            "session_id": session_id,
        },
    )

    vector_chunks = [doc.page_content for doc in vector_results]

    combined = bm25_results + vector_chunks

    unique_chunks = list(dict.fromkeys(combined))

    return "\n\n".join(unique_chunks[:5])
