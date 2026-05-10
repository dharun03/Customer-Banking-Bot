from vectorstore.example_store import (
    load_examples,
)

from rag.retriever.load_faqs import (
    load_faqs,
)

from vectorstore.pinecone_client import (
    index,
)

print("Clearing Pinecone index...")

index.delete(delete_all=True)

print("Loading few-shot examples...")

load_examples()

print("Loading FAQs...")

load_faqs()

print("Vectorstore initialization completed.")
