from langchain_chroma import Chroma
from openai import OpenAI
from dotenv import load_dotenv
import embeddings
import os

load_dotenv()

def query_with_langchain(query_text, top_k=5):
    # Get relevant documents
    chroma_store = Chroma(
        collection_name="text_embeddings",
        embedding_function=embeddings.embedding_function,
        client=embeddings.client
    )
    results = chroma_store.similarity_search(query_text, k=top_k)
    context = "\n".join([doc.page_content for doc in results])
    
    # Generate response using OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
             "content": "You are a dentlah health assistant. Be direct and confident but make sure to use the provided context to answer the question. If the context isn't relevant, say so. Be kind and helpful do not be too stiff but be factual"},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query_text}"}
        ]
    )
    
    return completion.choices[0].message.content