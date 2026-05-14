import uuid

from langchain_core.documents import Document

from document_upload.ocr import extract_text

from document_upload.parser import chunk_document

from vectorstore.index_manager import vectorstore

from document_upload.hybrid_retriever import (
    add_to_bm25_store,
)

from guardrails.pii_masker import mask_pii


def ingest_document(
    file_path: str,
    session_id: str,
    filename: str,
):

    extracted_text = extract_text(file_path)

    safe_text = mask_pii(extracted_text)

    chunks = chunk_document(safe_text)

    documents = []

    document_id = str(uuid.uuid4())

    for chunk in chunks:

        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "type": "document",
                    "session_id": session_id,
                    "document_id": document_id,
                    "filename": filename,
                },
            )
        )

    vectorstore.add_documents(documents)

    add_to_bm25_store(
        session_id=session_id,
        chunks=chunks,
    )

    return {
        "document_id": document_id,
        "chunks": len(chunks),
    }
