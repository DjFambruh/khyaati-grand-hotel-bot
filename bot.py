from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
🏨 KHYAATI GRAND HOTEL

Welcome Reception Manager 👋

Available Commands:

🛎 /checkin
🚪 /checkout
🏠 /rooms
👥 /guests
🧹 /housekeeping
📊 /reports
🤖 /ai
⚙️ /help
"""
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Reception Manager Assistant is ready.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Bot Started...")
app.run_polling()
