# Please install OpenAI SDK first: `pip3 install openai`

from common import send_messages

messages = [
        {"role": "system", "content": "You are a helpful assistant named Jarvis. You'll help me with anything I need."},
        {"role": "user", "content": "Jarvis, tell the weather in Shanghai right now."},
]

response = send_messages(messages)

print(response.content)