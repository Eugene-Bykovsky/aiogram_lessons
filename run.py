import asyncio
from environs import Env

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

env = Env()
env.read_env()

TELEGRAM_TOKEN = env.str('TELEGRAM_TOKEN')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
