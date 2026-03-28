import os
import time
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

last_message_time = time.time()

msgs = [
    "Bhai sab kidhar ho 😴",
    "Group dead ho gaya kya 💀",
    "Koi baat karo yaar 😅",
    "Hello hello 👀"
]

async def track_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_message_time
    last_message_time = time.time()

async def check_inactivity(context: ContextTypes.DEFAULT_TYPE):
    global last_message_time
    now = time.time()

    if now - last_message_time > 600:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=random.choice(msgs)
        )
        last_message_time = now

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, track_messages))

app.job_queue.run_repeating(check_inactivity, interval=300)

app.run_polling()
