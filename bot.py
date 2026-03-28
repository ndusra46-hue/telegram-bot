import os
import time
import threading
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 🔑 Token (Railway se uth raha hai)
TOKEN = os.environ.get("BOT_TOKEN")

# ⏱ Last message time track
last_message_time = time.time()

# 📩 Jab bhi koi message aaye
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_message_time
    last_message_time = time.time()
    
    # 👇 Group ID print karega (logs me)
    print("CHAT ID:", update.message.chat_id)
    
    # 👇 Test reply (confirm bot chal raha hai)
    await update.message.reply_text("ID mil gaya check logs 😎")

# 🤖 Inactive hone pe message bhejne wala function
def check_inactive(app):
    global last_message_time
    
    messages = [
        "Busy hai kya sab 😀",
        "Bhai bat karo na mujse koi baat nahi kr rha 🥺",
        "Or bhai aaj kya kiya kuch kam kiya ya telegram me he hi hello krta rha 😂",
        "Hello hello koi zinda hai ya sab ghost ban gaye 👻",
        "Group me itna sannata kyu hai bhai 😶",
        "Koi ek hi hello bol do yaar 😅",
        "Lagta hai sab busy ho gaye... ya ignore kar rahe ho 😏",
        "Koi topic start karo bhai warna main hi karta hu 😂",
        "Aaj ka din kaisa gaya sabka? 🤔",
        "Koi interesting baat batao yaar bore ho raha hu 😴"
    ]
    
    while True:
        if time.time() - last_message_time > 300:  # 5 min silence
            
            for i in range(3):  # 3 messages bhejega
                msg = random.choice(messages)
                
                try:
                    app.bot.send_message(
                        chat_id=update.message.chat_id,,  # 👈 yaha apna GROUP ID daal
                        text=msg
                    )
                except Exception as e:
                    print("Error:", e)
                
                time.sleep(60)  # 1 min gap
            
            last_message_time = time.time()
        
        time.sleep(30)

# 🚀 Bot start
app = ApplicationBuilder().token(TOKEN).build()

# 📩 Handler add
app.add_handler(MessageHandler(filters.ALL, handle_message))

# 🔄 Background thread
threading.Thread(target=check_inactive, args=(app,)).start()

# ▶️ Run bot
app.run_polling()
# redeploy
