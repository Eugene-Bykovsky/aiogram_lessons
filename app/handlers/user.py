from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!')


@user_router.message(F.text == 'Приветики')
async def echo(message: Message):
    await message.reply('Привет!')


@user_router.message(F.photo)
async def echo(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id)


@user_router.message(F.document)
async def echo(message: Message):
    await message.answer_document(document=message.document.file_id)


@user_router.message(F.audio)
async def echo(message: Message):
    await message.answer_audio(audio=message.audio.file_id)


@user_router.message(F.animation)
async def echo(message: Message):
    await message.answer_animation(animation=message.animation.file_id)
