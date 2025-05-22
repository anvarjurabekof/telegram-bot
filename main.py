from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
import os

# Bot token
API_TOKEN = os.getenv("BOT_TOKEN")

# Log format
logging.basicConfig(level=logging.INFO)

# Bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Language keyboard
language_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
language_keyboard.add(
    KeyboardButton("🇺🇿 O‘zbek tili"),
    KeyboardButton("🇷🇺 Русский язык")
)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Tilni tanlang:", reply_markup=language_keyboard)

@dp.message_handler(lambda message: message.text in ["🇺🇿 O‘zbek tili", "🇷🇺 Русский язык"])
async def set_language(message: types.Message):
    if message.text == "🇺🇿 O‘zbek tili":
        await message.answer("Siz O‘zbek tilini tanladingiz!")
    elif message.text == "🇷🇺 Русский язык":
        await message.answer("Вы выбрали русский язык!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
