from ollama import chat, ChatResponse, embed
from src.db import vector_db

def search(query: str, top_k: int = 5, model: str = "qwen-embedding:latest"):

    query_vector = embed(
        input=query,
        model=model,
    )["embeddings"][0]

    return vector_db.query(
        query_texts=[query_vector],
        n_results=top_k,
    )
    

def start_chat():

    print("Привет, я могу рассказать тебе все об универе TIMU, задавай вопросы!")
    history = []

    while True:
        question = input()
        history.append({'role': 'user', 'content': question})
        response: ChatResponse = chat(
            model='qwen-assistent:latest',
            messages=history,
        )
        history.append({'role': 'ai', 'content': response.message.content})
        # print(response.message.content)





