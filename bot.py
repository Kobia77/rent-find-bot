from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from scrapers.madlan_scraper import scrape_madlan
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# הפונקציה שתענה לפקודת /start
async def start(update: Update, context):
    await update.message.reply_text(
        "שלום וברוך הבא! אני כאן לעזור לך למצוא דירות להשכרה 🏠.\n"
        "כדי להתחיל, אני צריך כמה פרטים ממך."
    )
    await update.message.reply_text("איפה אתה מחפש דירות?")
    context.user_data["state"] = "location"  # הגדרת מצב התחלה

# פונקציה לטיפול בהודעות טקסט רגילות
async def handle_message(update: Update, context):
    user_message = update.message.text

    # בדיקת המצב הנוכחי של המשתמש
    state = context.user_data.get("state")

    if state == "location":
        context.user_data["location"] = user_message  # שמירת המיקום
        await update.message.reply_text("מעולה! ומה התקציב המקסימלי שלך?")
        context.user_data["state"] = "max_price"  # מעבר לשלב הבא

    elif state == "max_price":
        try:
            max_price = int(user_message)  # המרה למספר
            context.user_data["max_price"] = max_price
            await update.message.reply_text(
                f"מיקום: {context.user_data['location']}\nתקציב מקסימלי: {max_price}₪\nמחפש עבורך דירות!"
            )
            # כאן תוכל להוסיף קריאה לפונקציית גרידת הנתונים
            context.user_data["state"] = None  # איפוס המצב

        except ValueError:
            await update.message.reply_text("אנא הכנס מספר תקין לתקציב.")

    else:
        await update.message.reply_text("אני לא בטוח מה לעשות עם זה. נסה לשלוח /start כדי להתחיל מחדש.")

# הרצת הבוט
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # פקודת /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))  # הודעות רגילות



    url = "https://www.madlan.co.il/for-rent/ישראל?page=1"    
    ads_data = scrape_madlan(url)
    for ad in ads_data:
        print(ad)



    print("bot is running!")
    app.run_polling()
    