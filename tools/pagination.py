from telegram import Update, ReplyKeyboardMarkup
from tools.search import perform_search

async def handle_message(update: Update, context):
    user_message = update.message.text

    state = context.user_data.get("state")

    if state == "location":
        context.user_data["location"] = user_message
        await update.message.reply_text("מעולה! ומה התקציב המקסימלי שלך?")
        context.user_data["state"] = "max_price"

    elif state == "max_price":
        try:
            max_price = int(user_message)
            context.user_data["max_price"] = max_price
            await update.message.reply_text(
                f"מיקום: {context.user_data['location']}\nתקציב מקסימלי: {max_price}₪\n\nמחפש עבורך דירות... 👀"
            )
            
            listings = perform_search(context.user_data['location'], context.user_data['max_price'])
            context.user_data["listings"] = listings
            context.user_data["page"] = 0  # להתחיל מדף 0
            
            if listings:
                await send_listings(update, context)
            else:
                await update.message.reply_text("לא הצלחתי למצוא דירות.")
            
        except ValueError:
            await update.message.reply_text("אנא הכנס מספר תקין לתקציב.")

    elif state == "pagination":
        if user_message == "עוד 5 דירות":
            context.user_data["page"] += 1
            await send_listings(update, context)
        elif user_message == "חיפוש חדש":
            context.user_data.clear()
            await update.message.reply_text("איפה אתה מחפש דירות?")
            context.user_data["state"] = "location"
        else:
            await update.message.reply_text("לא הצלחתי להבין, נסה לבחור אחת מהאפשרויות.")

async def send_listings(update, context):
    page = context.user_data["page"]
    listings = context.user_data["listings"]
    start_index = page * 5
    end_index = start_index + 5
    for ad in listings[start_index:end_index]:
        await update.message.reply_text(
            f"📍 {ad['address']}\n🚪{ad['rooms']}\n💰 {ad['price']}\n🔗 {ad['link']}"
        )
    context.user_data["state"] = "pagination"

    if end_index < len(listings):
        keyboard = [["עוד 5 דירות"], ["חיפוש חדש"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text("מה תרצה לעשות עכשיו?", reply_markup=reply_markup)
    else:
        await update.message.reply_text("אלו כל הדירות שמצאתי. 😊")
