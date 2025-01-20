from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb

user_router = Router()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Привет!', reply_markup=kb.main_inline)


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


@user_router.callback_query(F.data == 'catalog')
async def cmd_catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('Вы открыли каталог.',
                                  reply_markup=await kb.catalog())
