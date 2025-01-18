import asyncio
import logging
from environs import Env

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

env = Env()
env.read_env()

TELEGRAM_TOKEN = env.str('TELEGRAM_TOKEN')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!')


@dp.message(F.text == 'Приветики')
async def echo(message: Message):
    await message.reply('Привет!')


@dp.message(F.photo)
async def echo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)


@dp.message(F.document)
async def echo(message: Message):
    await message.answer_document(document=message.document.file_id)


@dp.message(F.audio)
async def echo(message: Message):
    await message.answer_audio(audio=message.audio.file_id)


@dp.message(F.animation)
async def echo(message: Message):
    await message.answer_animation(animation=message.animation.file_id)


@dp.message(F.from_user.id == 534211907)
async def echo(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
