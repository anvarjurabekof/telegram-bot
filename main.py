from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start komandasi funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ['🇺🇿 O‘zbek', '🇷🇺 Русский']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Iltimos, tilni tanlang 👇\nПожалуйста, выберите язык 👇",
        reply_markup=reply_markup
    )

# Botni ishga tushirish
if __name__ == '__main__':
    import os
    TOKEN = os.environ.get("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # Eskirgan getUpdates’larni tashlab, conflict xatosini bartaraf etamiz
    app.run_polling(drop_pending_updates=True)
