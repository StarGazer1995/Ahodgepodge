from .get_client import client

def send_messages(messages, tools=None, stream=False):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools,
        stream=stream,
    )
    return response.choices[0].message