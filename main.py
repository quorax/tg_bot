import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("✅ Бот работает! Aiogram v3.7 настроен корректно.")

async def main():
    print("🚀 Бот запущен и слушает Telegram...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
