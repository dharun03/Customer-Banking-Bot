from langchain_pinecone import PineconeVectorStore

from vectorstore.embeddings import (
    embedding_model,
)

from vectorstore.pinecone_client import (
    index,
)

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embedding_model,
    text_key="text",
)
