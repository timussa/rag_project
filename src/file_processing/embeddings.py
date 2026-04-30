from typing import List
from ollama import embed


def chunk_to_vector(chunk: str, model: str = 'qwen-embedding:latest'):
    return embed(
        model=model,
        input=chunk,
    )

def chunks_to_vectors(chunks: List, model: str = 'qwen-embedding:latest'):
    vectors = embed(
        model=model,
        input=chunks,
    )
    return vectors
