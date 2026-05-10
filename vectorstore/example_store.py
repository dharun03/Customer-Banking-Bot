from vectorstore.chroma_client import vectorstore

from prompts.few_shots import FEW_SHOT_EXAMPLES


def load_examples():

    documents = []

    metadatas = []

    for example in FEW_SHOT_EXAMPLES:

        documents.append(example["query"])

        metadatas.append({"response": example["response"]})

    vectorstore.add_texts(texts=documents, metadatas=metadatas)

    print("Few-shot examples loaded.")
