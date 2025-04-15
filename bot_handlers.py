from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("Hi there, I'm L, your on-chain alpha friend!")


def start():
    return CommandHandler("start", start)