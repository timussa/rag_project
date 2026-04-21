from src.db import vector_db
from src.file_processing.chunking import chunk_directory, qa_chunk_processing
from typing import List
from ollama import embed


def chunk_to_vector(chunk: str, model: str = 'qwen-embedding'):
    return embed(
        model=model,
        input=chunk,
    )

def chunks_to_vectors(chunks: List, model: str = 'qwen-embedding'):
    vectors = embed(
        model=model,
        input=chunks,
    )
    return vectors
