import asyncio
import logging
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from tok import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message : Message):
    await message.answer(message.text)
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())