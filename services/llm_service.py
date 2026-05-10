from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    temperature=float(os.getenv("TEMPERATURE")),
)
