import os
import openai
from flask import Flask, request

app = Flask(__name__)

# إعدادات OpenRouter
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

@app.route("/")
def home():
    return "بوت ڨيان شغال 🤖✨"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data and "text" in data["message"]:
        user_message = data["message"]["text"]
        chat_id = data["message"]["chat"]["id"]

        response = openai.ChatCompletion.create(
            model="mistralai/mistral-7b-instruct",
            messages=[
                {"role": "system", "content": "انت ڨيان، صديقة مجنونة تحچي باللهجة العراقية وتعشق الهوسة 😂"},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response["choices"][0]["message"]["content"]

        send_message(chat_id, bot_reply)

    return "ok"

import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)
