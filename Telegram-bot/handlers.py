from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, URLInputFile
from keyboards import main, main2
from back import x, y, x2, y2, x3, y3, l1, l2, r1, r2, k1, k2, an, ph


router = Router()



@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer('Доброго времени суток, я бот-аналитик мемов! \n'
                         '\n'
                         'Могу показать топ 3 самых популярных мема на данный момент \n'
                         '\n'
                         'Могу сделать полный анализ любого поста вк \n'
                         '\n'
                         'Вся нецензурная лексика отфильтрована в отдельную категорию', reply_markup=main)
    


@router.message(F.text == 'Вывести топ 3 мема')
async def top_mem(message: Message):
    photo_url = x
    photo = URLInputFile(photo_url)
    photo_url2 = x2
    photo2 = URLInputFile(photo_url2)
    photo_url3 = x3
    photo3 = URLInputFile(photo_url3)
    await message.answer_photo(photo)
    await message.answer(y)
    await message.answer_photo(photo2)
    await message.answer(y2)
    await message.answer_photo(photo3)
    await message.answer(y3, reply_markup=main2)




@router.message(F.text == 'Анализ поста (ручной режим)')
async def start_cmd(message: Message):
    await message.answer('Отправьте id поста в вк')


@router.message(F.text == 'Назад')
async def zad(message: Message):
    await message.answer('угу', reply_markup=main)


@router.message(F.text == 'Мемы 18+')
async def eltern(message: Message):
    await message.answer('Я щас позвоню твоей маме и скажу, что ты балуешься!')


@router.message(F.text == 'Рекорд лайков')
async def li(message: Message):
    await message.answer_photo(l1)
    await message.answer(l2)


@router.message(F.text == 'Чаще всего репостят')
async def repost(message: Message):
    await message.answer_photo(r1)
    await message.answer(r2)


@router.message(F.text == 'Самый вызывающий')
async def comm(message: Message):
    await message.answer_photo(k1)
    await message.answer(k2)


@router.message()
async def message(message: Message):
    user_text = message.text
    if user_text.startswith('id-'):
        try:
            user_text = message.text
            txt = user_text[2:]
            await message.answer_photo(ph(txt))
            await message.answer(an(txt))
        except Exception as e:
            await message.answer(f"Произошла ошибка: {e}")


@router.message()
async def echo(message: Message):
    text = message.text

    if text in ['Привет', 'привет', 'hi', 'hello']:
        await message.answer('И тебе привет!')
    elif text in ['Пока', 'пока', 'До свидания']:
        await message.answer('И тебе пока!')
    else:
        await message.answer(message.text)
