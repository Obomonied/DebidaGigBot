import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.campaign import router as campaign_router
from handlers.payment import router as payment_router
from handlers.admin import router as admin_router


async def main():
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(campaign_router)
    dp.include_router(payment_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
