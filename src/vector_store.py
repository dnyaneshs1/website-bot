from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def create_faiss_index(texts):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    vector_store = FAISS.from_texts(texts, embedder)
    return vector_store