from openai import OpenAI
from dotenv import load_dotenv
from langchain_chroma import Chroma
import os
import text_preprocessing
import embeddings

load_dotenv()

def get_relevant_context(query_text, top_k=3):
    """Retrieve relevant context using LangChain and ChromaDB"""
    chroma_store = Chroma(
        collection_name="text_embeddings",
        embedding_function=embeddings.embedding_function,
        client=embeddings.client
    )
    results = chroma_store.similarity_search(query_text, k=top_k)
    return "\n".join([doc.page_content for doc in results])

def generate_response(query_text, context):
    """Generate response using OpenAI with retrieved context"""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    system_prompt = """You are a helpful assistant. Use the provided context to answer the question. 
    If the context doesn't contain relevant information, say so."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query_text}"}
    ]
    
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    
    return completion.choices[0].message.content

def process_query(query_text):
    """Main function to process queries using the combined system"""
    # First, get relevant context using LangChain
    context = get_relevant_context(query_text)
    
    # Then, generate response using OpenAI with the retrieved context
    response = generate_response(query_text, context)
    
    return response