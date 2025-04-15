from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from bot_handlers import start 

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(start())
app.run_polling()

