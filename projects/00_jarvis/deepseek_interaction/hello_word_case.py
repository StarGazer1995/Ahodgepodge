# Please install OpenAI SDK first: `pip3 install openai`

from get_client import client

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Jarvis. You'll help me with anything I need."},
        {"role": "user", "content": "Jarvis, tell the weather in Shanghai right now."},
    ],
    stream=False
)

print(response.choices[0].message.content)