import os
import chromadb
from src.file_processing.chunking import qa_chunk_processing
from src.file_processing.embeddings import chunks_to_vectors
import time


chroma_client = chromadb.PersistentClient(path="./chroma_db")

vector_db = chroma_client.get_or_create_collection(name="vector_db")

def save_file(path: str, embed_model: str="qwen-embedding:latest"):
    try:
        file_name = os.path.splitext(
            os.path.basename(path)
        )[0]

        chunks = qa_chunk_processing(path)
        print("Chunks created")

        vectors = chunks_to_vectors(chunks=chunks, model=embed_model)
        print("Embeddings created")

        if len(chunks) != len(vectors["embeddings"]):
            raise ValueError("Chunks and embeddings mismatch")

        run_id = int(time.time())
        ids = [f"{file_name}_{run_id}_{i}" for i in range(len(chunks))]

        vector_db.add(
            ids=ids,
            documents=chunks,
            embeddings=vectors["embeddings"]
        )
        print("Saved to ChromaDB")


    except Exception as e:
        raise e

def save_dir(path: str, embed_model: str="qwen-embedding:latest"):
    

    for root, ders, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                save_file(file_path, embed_model)
            except Exception as e:
                print(f"Failed file {file_path}: {e}")
    
