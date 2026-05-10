import json
import uuid

from vectorstore.index_manager import (
    vectorstore,
)


def load_faqs():

    with open(
        "rag/faq_dataset/banking_faqs.json",
        "r",
    ) as f:

        faqs = json.load(f)

    texts = []
    metadatas = []
    ids = []

    for faq in faqs:

        combined_text = f"Question: {faq['question']}\n" f"Answer: {faq['answer']}"

        texts.append(combined_text)

        metadatas.append(
            {
                "type": "faq",
                "faq_id": faq["id"],
                "category": faq["category"],
                "question": faq["question"],
                "answer": faq["answer"],
            }
        )

        ids.append(str(uuid.uuid4()))

    vectorstore.add_texts(
        texts=texts,
        metadatas=metadatas,
        ids=ids,
    )

    print("FAQs indexed successfully.")
