from langchain.embeddings import HuggingFaceEmbeddings

def generate_embeddings(texts):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedder = HuggingFaceEmbeddings(model_name=model_name)
    return embedder.embed_documents(texts)