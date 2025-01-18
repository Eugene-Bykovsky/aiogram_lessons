from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

admin_router = Router()


@admin_router.message(Command('adminpanel'))
async def cmd_apanel(message: Message):
    await message.answer('Это админ-панель')
