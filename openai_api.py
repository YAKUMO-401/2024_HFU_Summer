from openai import OpenAI
import os

def chat_with_chatgpt(user_message,openai_api_key):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message+"請用溫柔的方式回答",
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    response = chat_completion.choices[0].message.content
    return response if response else "NO Comtent"

if __name__=="__main__":
    user_message = "我愛蘋果"
    api_key = os.getenv("OPENAI_API_KEY",None)
    if api_key and user_message:
        response = chat_with_chatgpt(user_message,api_key)
        print(response)
    else:
        print("api key not found")