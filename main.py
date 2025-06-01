import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai
import asyncio

openai.api_key = os.getenv("OPENAI_API_KEY")
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا والله! أنا ڨيان، صديقتك الذكية 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "أنت بوت ذكي، تحچي عراقي وتجاوب بكل حرية."},
            {"role": "user", "content": user_text},
        ],
    )
    answer = response.choices[0].message.content
    await update.message.reply_text(answer)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("ڨيان اشتغلت!")
    app.run_polling()
