from flask import Flask, request, abort,render_template

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
from handle_keys import get_secret_and_token

from openai_api import chat_with_chatgpt
import os
from cwa_opendata_scraper import get_cities_weather

app = Flask(__name__)
keys = get_secret_and_token()
handler = WebhookHandler(keys['LINEBOT_SECRET_KEY'])
configuration = Configuration(access_token=keys['LINEBOT_ACCESS_TOKEN'])


@app.route("/")
def say_hello_world(username=""):
    return render_template("hi.html",name=username)

@app.route("/callback", methods=['POST'])
@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):

    user_id = event.source.user_id 
    user_message = event.message.text 
    api_key = keys["OPENAI_API_KEY"]

    if '天氣如何' in user_message:
        cwa_api_key = keys['CWA_API_KEY']
        locations_name = user_message.split()[1:]
        if locations_name:
            weather_data = get_cities_weather(cwa_api_key, locations_name)
            response = ""
            for location in weather_data: 
                response += f"{location}:\n" 
                for weather_key in sorted(weather_data[location]): 
                    response += f"\t\t{weather_key}: {weather_data[location][weather_key]}\n"
            response = response.strip()            
            # response = chat_with_chatgpt(user_id, user_message, api_key,extra_prompt="請根據稍早的天氣資訊,提供200字內的穿搭建議報導,")
        else:
            response = "請輸入縣市"
    else:
        response = chat_with_chatgpt(user_id, user_message, api_key)
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[
                    TextMessage(text=response)
                ]
            )
        )

if __name__ == "__main__":
    app.run(debug=True)