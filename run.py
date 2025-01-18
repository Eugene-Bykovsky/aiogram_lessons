import asyncio
import logging
from environs import Env

from aiogram import Bot, Dispatcher
from app.handlers import user_router


async def main():
    env = Env()
    env.read_env()
    TELEGRAM_TOKEN = env.str('TELEGRAM_TOKEN')
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
