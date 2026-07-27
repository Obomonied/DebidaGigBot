from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🚀 Welcome to Debida Gig!\n\n"
        "Use the menu below to create campaigns, "
        "view pricing, and manage your tasks."
    )
