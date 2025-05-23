from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['🇺🇿 O‘zbek', '🇷🇺 Русский']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Iltimos, tilni tanlang 👇\nПожалуйста, выберите язык 👇",
        reply_markup=reply_markup
    )

# Til tanlash funksiyasi
async def choose_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "🇺🇿 O‘zbek":
        await update.message.reply_text("Siz O‘zbek tilini tanladingiz.")
    elif text == "🇷🇺 Русский":
        await update.message.reply_text("Вы выбрали русский язык.")

# Botni ishga tushirish
if __name__ == '__main__':
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, choose_language))

    app.run_polling(drop_pending_updates=True)
