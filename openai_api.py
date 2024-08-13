from openai import OpenAI
import os
from pprint import pprint


chat_history = dict()

def chat_with_chatgpt(user_id,user_message,openai_api_key,extra_prompt=""):
    client = OpenAI(api_key=openai_api_key)
    if user_id in chat_history:
        chat_history[user_id].append({"role": "user","content": user_message})
    else:
        chat_history[user_id] = [{"role": "user", "content": user_message}]

    message = user_message + '  請用條列式的方式回答。'
    chat_completion = client.chat.completions.create(
        messages=chat_history[user_id][:-1]+[
            {"role": "user","content": user_message}],
        model="gpt-3.5-turbo",
    )
    
    response = chat_completion.choices[0].message.content

    chat_history[user_id].append({"role": "system","content": response,})
    return response if response else "NO Comtent"

if __name__=="__main__":

    api_key = os.getenv("OPENAI_API_KEY",None)
    user_id="XXX"
    while True:
        user_message = input("輸入")
        if user_message == "quit":
            print("結束")
            break
        if api_key and user_message:
            response = chat_with_chatgpt(user_id,user_message,api_key)
            print(response)
        else:
            print("api key not found")
        
        print("Histry:")
        print(chat_history)
        print()