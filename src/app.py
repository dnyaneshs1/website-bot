import streamlit as st
from src.vector_store import create_faiss_index
from src.chatbot import retrieve_answer


st.title("Website bot")

user_input = st.text_input("Ask your question:")

if user_input:
    texts = ["Sample document 1", "Sample document 2"]  # Replace with your dataset
    vector_store = create_faiss_index(texts)
    answer = retrieve_answer(user_input, vector_store)
    st.write(f"Answer: {answer}")