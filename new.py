from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['HUGGINGFACE_API_KEY'] = os.getenv("HUGGINGFACE_API_KEY")

def load_pdf(file_path):
    """
    Load a PDF document using PyPDFLoader.
    """
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs

def split_pdf(docs):
    """
    Split the loaded documents into smaller chunks using RecursiveCharacterTextSplitter.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    final_documents = text_splitter.split_documents(docs)
    return final_documents 

def embed_documents(final_documents):
    """
    Generate embeddings for the split documents using HuggingFaceEmbeddings.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

def create_faiss_index(embeddings, final_documents):
    """
    Create a FAISS index from the document embeddings and store it for similarity search.
    """
    vector_store = FAISS.from_documents(final_documents, embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def load_faiss_index():
    """
    Load a FAISS index from a saved local file.
    """
    vector_store = FAISS.load_local("faiss_index", HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),allow_dangerous_deserialization = True)
    return vector_store

# Workflow
if __name__ == "__main__":
    file_path = "dbms2.pdf"  # Path to your PDF file
    docs = load_pdf(file_path)
    final_documents = split_pdf(docs)
    embeddings = embed_documents(final_documents)

    # Create and save FAISS index
    faiss_index = create_faiss_index(embeddings, final_documents)
    print("FAISS index created and saved.")

    # Load FAISS index and query (example)
    loaded_index = load_faiss_index()
    query = "Explain DBMS normalization concepts."
    results = loaded_index.similarity_search(query, k=3)  # Retrieve top 3 similar documents
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result.page_content}")
