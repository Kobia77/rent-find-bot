from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# הפונקציה שתענה לפקודת /start
async def start(update: Update, context):
    await update.message.reply_text("שלום וברוך הבא! אני הבוט שלך למציאת דירות 🏠.\nמה תרצה לחפש היום?")

# פונקציה לטיפול בהודעות טקסט רגילות
async def handle_message(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"קיבלת: {user_message}\nאחפש דירות עבורך בקרוב!")

# הרצת הבוט
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # פקודת /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # הודעות רגילות

    print("bot is running!")
    app.run_polling()
