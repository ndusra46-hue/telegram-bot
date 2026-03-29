import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

last_message_time = time.time()

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_message_time
    last_message_time = time.time()
    
    print("CHAT ID:", update.message.chat_id)
    await update.message.reply_text("ID mil gaya check logs 😎")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, handle_message))

app.run_polling()
# update
# new token update
