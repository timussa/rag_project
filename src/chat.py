from ollama import chat, ChatResponse, create

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
        print(response.message.content)


if __name__ == '__main__':
    start_chat()

