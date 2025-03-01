from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Вывести топ 3 мема')],
    [KeyboardButton(text='Анализ поста (ручной режим)'), KeyboardButton(text='Мемы 18+')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие')

main2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Рекрод лайков'), KeyboardButton(text='Самый вызывающий')],
    [KeyboardButton(text='Чаще всего репостят'), KeyboardButton(text='Назад')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие')

inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Самые залайканные', callback_data='lover')],
    [InlineKeyboardButton(text='Самые закомментированные', callback_data='byte'), InlineKeyboardButton(text='Чаще всего репостят', callback_data='reposter')]
])

