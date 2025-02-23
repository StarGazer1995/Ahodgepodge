from functions import process_response, tools
from common import send_messages

if __name__ == "__main__":
    
    messages = [{"role": "system", "content": "You are a helpful assistant named Jarvis. You'll help me with anything I need. You should read the message carefully and give me the correct answer. You can use the tools I provide to help me. Reply to me with the same language I provided. Also, you should reply to me in a sentence."},
                {"role": "user", "content": "When the PRC was founded?"}]
    message = send_messages(messages, tools)
    count = 0
    while (count < 3 and message.tool_calls is not None):
        process_response(message, messages)
        message = send_messages(messages, tools)
        count += 1

    print(f"Model>\t {message.content}")