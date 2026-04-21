from ollama import create

SYSTEM_PROMPT='''
Ты ассистент, отвечающий на вопросы клиентов об университете
TIMU (Torsiza International Modern University).
Отвечай кратко и по делу.
'''

create(
    model='qwen-assistent',
    from_='qwen3.5:9b',
    system=SYSTEM_PROMPT,
    stream=True,
)