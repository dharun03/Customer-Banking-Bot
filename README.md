# Banking Customer Service & Complaint Resolution Assistant

This project is an enterprise-style AI banking assistant built using FastAPI, LangChain, OpenAI and Streamlit. It can handle banking FAQs, complaint workflows, EMI calculations, currency conversion, escalation handling, and multi-turn customer conversations using hybrid conversational memory. Semantic few-shot retrieval is implemented using ChromaDB to improve contextual understanding and response quality.

The assistant uses autonomous LangChain tool calling with custom banking tools. Hybrid memory combines recent conversation history with summarized older context to support long-running interactions and follow-up questions. LangSmith tracing is integrated for observability, debugging, workflow monitoring, and tool execution tracking.

## Tools Used

- **EMI Calculator Tool** — Calculates monthly loan EMI based on principal amount, interest rate, and loan tenure.
- **Currency Exchange Tool** — Performs mock currency conversion using predefined exchange rates.
- **Complaint Triage Tool** — Uses LLM-based analysis to classify complaint severity and determine escalation priority.
- **Ticket Creation Tool** — Generates and stores customer complaint tickets with status, priority, and escalation details.

## How to Run

Install dependencies:
- pip install -r requirements.txt

Start FastAPI backend:
- uvicorn api.app:app --reload

Start Streamlit frontend:
 - streamlit run frontend/streamlit_app.py