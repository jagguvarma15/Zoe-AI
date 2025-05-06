from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient
import os

COLLECTION_NAME = "zoe-knowledge-base"

def get_vectorstore():
    """
    Connects to local Qdrant instance and returns a LangChain-compatible vector store.
    """
    # Local Qdrant instance by default
    client = QdrantClient(host=os.getenv("QDRANT_HOST", "localhost"), port=6333)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = Qdrant(
        client=client,
        collection_name=COLLECTION_NAME,
        embeddings=embeddings,
    )

    return vectorstore
