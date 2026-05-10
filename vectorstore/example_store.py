import uuid

from vectorstore.index_manager import (
    vectorstore,
)

from prompts.few_shots import (
    FEW_SHOT_EXAMPLES,
)


def load_examples():

    texts = []

    metadatas = []

    ids = []

    for example in FEW_SHOT_EXAMPLES:

        texts.append(example["query"])

        metadatas.append(
            {
                "response": example["response"],
                "type": "few_shot",
                "domain": "banking",
            }
        )

        ids.append(str(uuid.uuid4()))

    vectorstore.add_texts(
        texts=texts,
        metadatas=metadatas,
        ids=ids,
    )

    print("Few-shot examples indexed in Pinecone.")
