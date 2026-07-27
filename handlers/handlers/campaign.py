from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "🚀 Create Campaign")
async def create_campaign(message: Message):
    await message.answer(
        "📌 Create Campaign\n\n"
        "First, choose your task type:\n\n"
        "📢 Telegram\n"
        "🐦 X (Twitter)\n"
        "📘 Facebook\n"
        "📸 Instagram\n"
        "📌 Pinterest\n"
        "👽 Reddit"
    )
