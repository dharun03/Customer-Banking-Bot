from langchain_community.vectorstores import Chroma

from langchain_openai import OpenAIEmbeddings

embedding_function = OpenAIEmbeddings()

vectorstore = Chroma(
    collection_name="banking_examples",
    embedding_function=embedding_function,
    persist_directory="./chroma_db",
)
