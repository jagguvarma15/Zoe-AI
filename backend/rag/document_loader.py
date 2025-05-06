import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient

COLLECTION_NAME = "zoe-knowledge-base"
EMBED_MODEL = "all-MiniLM-L6-v2"

def load_documents(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith(".txt"):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file type")

    return loader.load()

def process_and_index(file_path: str):
    docs = load_documents(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    split_docs = splitter.split_documents(docs)

    embeddings = SentenceTransformerEmbeddings(model_name=EMBED_MODEL)
    client = QdrantClient(host=os.getenv("QDRANT_HOST", "localhost"), port=6333)

    # Create or update the vector store
    Qdrant.from_documents(
        documents=split_docs,
        embedding=embeddings,
        client=client,
        collection_name=COLLECTION_NAME
    )

    return {"status": "indexed", "chunks": len(split_docs)}
