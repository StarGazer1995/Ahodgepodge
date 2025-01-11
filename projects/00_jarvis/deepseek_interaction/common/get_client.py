from openai import OpenAI
from my_token import MODEL_API_KEY
client = OpenAI(api_key=MODEL_API_KEY, base_url="https://api.deepseek.com")