import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Бот работает. Напиши /test")

@dp.message(Command("test"))
async def test_cmd(message: types.Message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text="✅ Канал работает!")
        await message.answer("Сообщение отправлено в канал!")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

@dp.message()
async def echo_all(message: types.Message):
    await message.answer("Я отвечаю только на /start и /test")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
