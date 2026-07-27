from aiogram import Router
from aiogram.types import Message

from config import ADMIN_ID

router = Router()


@router.message(lambda message: message.from_user.id == ADMIN_ID)
async def admin_panel(message: Message):
    await message.answer(
        "🛠 Admin Panel\n\n"
        "Manage campaigns:\n\n"
        "✅ Approve Campaign\n"
        "❌ Reject Campaign\n"
        "📋 View Pending Tasks"
    )
