from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy import select
from database import User, async_session

router = Router()

@router.message(F.text == "🏆 Reyting")
async def show_rating(message: Message):
    async with async_session() as session:
        result = await session.execute(
            select(User).order_by(User.stars.desc()).limit(10)
        )
        top_users = result.scalars().all()

        if not top_users:
            await message.answer("⛔️ Reytingda hali hech kim yo‘q.")
            return

        text = "🏆 <b>Top 10 yulduz to‘plovchilar:</b>\n\n"
        for i, user in enumerate(top_users, 1):
            username = f"@{user.username}" if user.username else f"ID: {user.user_id}"
            text += f"{i}. {username} — {user.stars} ⭐️\n"

        await message.answer(text)
