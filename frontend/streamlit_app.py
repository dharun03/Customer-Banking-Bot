import streamlit as st

import requests

import uuid

st.set_page_config(page_title="Banking AI Assistant")

st.title("🏦 Banking Customer Assistant")

if "session_id" not in st.session_state:

    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


query = st.chat_input("Ask your banking question")

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query,
        }
    )

    with st.chat_message("user"):

        st.markdown(query)

    response = requests.post(
        "http://localhost:8000/chat",
        json={
            "query": query,
            "session_id": st.session_state.session_id,
        },
    )

    answer = response.json()["answer"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):

        st.markdown(answer)
