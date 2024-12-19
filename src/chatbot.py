
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def retrieve_answer(query, vector_store):
    # Use a free open-source LLM
    model_name = "google/flan-t5-small"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # Add parameters to encourage longer and more detailed answers
    hf_pipeline = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=256,       # Increase max token length
        min_length=50,        # Ensure a minimum token length
        num_return_sequences=1,
        no_repeat_ngram_size=3,  # Avoid repetitive answers
        temperature=0.7,      # Control randomness
    )
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    retriever = vector_store.as_retriever()
    #docs = retriever.get_relevant_documents(query)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    #print(f"Retrieved documents: {docs}")
    return qa_chain.run(query)



