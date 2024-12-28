from telegram import Update


# הפונקציה שתענה לפקודת /start
async def start(update: Update, context):
    await update.message.reply_text(
        "שלום וברוך הבא! אני כאן לעזור לך למצוא דירות להשכרה 🏠.\n"
        "כדי להתחיל, אני צריך כמה פרטים ממך."
    )
    await update.message.reply_text("איפה אתה מחפש דירות?")
    context.user_data["state"] = "location"  # הגדרת מצב התחלה
