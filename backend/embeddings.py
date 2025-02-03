import requests
from dotenv import load_dotenv
import chromadb
from chromadb.config import Settings
from langchain_chroma import Chroma
from langchain.embeddings.base import Embeddings
import text_preprocessing
import os

load_dotenv()

hf_token = os.environ.get("HF_TOKEN")
model_id = "sentence-transformers/all-MiniLM-L6-v2"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

# provides a wrapper around Hugging Face's API for embeddings, to implement embed docs and embed query
# Langchain Embeddings class implementation for its integration
class HuggingFaceEmbeddings(Embeddings):
    def __init__(self, api_url, headers):
        self.api_url = api_url
        self.headers = headers
    
    # creates document embeddings
    def embed_documents(self, texts):
        try:
            return query(texts)
        except Exception as e:
            print(f"Error embedding documents: {e}")
            return None
    
    # creates query embeddings
    def embed_query(self, text):
        try:
            return query([text])[0]
        except Exception as e:
            print(f"Error embedding query: {e}")
            return None

# POST request to Hugging Face’s API with the input texts
# Returns the vector embeddings as a response
def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    response.raise_for_status()
    return response.json()

try:
    output = query(text_preprocessing.texts) # calls Hugging Face API to generate embeddings
    
    #Initializes a ChromaDB client and retrieves (or creates) a collection named
    client = chromadb.Client(Settings( 
        persist_directory="chromadb_store",
        anonymized_telemetry=False
    ))
    
    collection = client.get_or_create_collection(name="text_embeddings")
    
    for idx, text in enumerate(text_preprocessing.texts):
        collection.add(
            documents=[text],
            embeddings=[output[idx]],
            ids=[f"doc_{idx}"]
        )
        
    embedding_function = HuggingFaceEmbeddings(api_url, headers)

except Exception as e:
    print(f"Error: {e}")