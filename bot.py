import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚀 Welcome to Debida Gig\n\n"
        "Create campaigns, pay with Telegram Stars, "
        "and connect with freelancers.\n\n"
        "Choose an option:\n"
        "🚀 Create Campaign\n"
        "💰 Pricing\n"
        "📋 My Campaigns\n"
        "📞 Support"
    )


async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
