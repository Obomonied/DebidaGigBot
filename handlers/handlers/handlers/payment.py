from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda message: message.text == "💰 Pricing")
async def pricing(message: Message):
    await message.answer(
        "💰 Debida Gig Pricing\n\n"
        "Minimum reward per freelancer: ⭐2\n\n"
        "Example:\n"
        "100 workers × ⭐2 = ⭐200\n\n"
        "Service fee is added during checkout."
    )
