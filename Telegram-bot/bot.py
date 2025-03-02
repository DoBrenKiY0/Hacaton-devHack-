import asyncio
from aiogram import Bot, Dispatcher
from handlers import router
from key import token

bot = Bot(token=token)
dp = Dispatcher()


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
