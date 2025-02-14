from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'),
     KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Контакты')]
], resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')


main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])


async def catalog():
    all_data = ('Nike', 'Adidas', 'Reebok')

    keyboard = ReplyKeyboardBuilder()

    for data in all_data:
        keyboard.add(KeyboardButton(text=data))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)
