import os

import tempfile

from fastapi import (
    APIRouter,
    File,
    UploadFile,
)

from document_upload.ingestion import (
    ingest_document,
)

router = APIRouter()


@router.post("/document/upload")
async def upload_document(
    file: UploadFile = File(...),
    session_id: str = "default",
):

    suffix = os.path.splitext(file.filename)[1]

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as tmp:

            content = await file.read()

            tmp.write(content)

            temp_path = tmp.name

        result = ingest_document(
            file_path=temp_path,
            session_id=session_id,
            filename=file.filename,
        )

        return {
            "message": "Document uploaded successfully",
            "document_id": result["document_id"],
            "chunks": result["chunks"],
        }

    finally:

        if temp_path and os.path.exists(temp_path):

            os.remove(temp_path)
