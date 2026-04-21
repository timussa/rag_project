import chromadb
from typing import List
from src.file_processing.chunking import qa_chunk_processing, chunk_directory
from src.file_processing.embeddings import chunks_to_vectors


chroma_client = chromadb.Client()

vector_db = chroma_client.create_collection(name="vector_db")

def save_file(path: str, embed_model: str="qwen-embedding"):
    try:
        chunks = qa_chunk_processing(path)
        print("chunks added")
        chunks_to_vectors(chunks=chunks)
        print("embedings added")

        ###
        ### There will be an addition to the db here 
        ###
    except:
        raise Exception

def save_dir(path: str, embed_model: str="qwen-embedding"):
    pass
    

