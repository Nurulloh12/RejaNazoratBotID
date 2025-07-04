from config import ADMINS
from database import get_user
from aiogram import Bot

async def notify_admin_if_10_stars(user_id: int, stars: int, bot: Bot):
    if stars == 10:
        user = await get_user(user_id)
        username = f"@{user.username}" if user.username else f"ID: {user.user_id}"

        text = (
            "🎉 <b>Yangi yulduz to‘plovchi!</b>\n\n"
            f"👤 Foydalanuvchi: {username}\n"
            f"⭐️ Taklif qilganlar soni: {stars} ta\n\n"
            "🚀 10 ta do‘st taklif qildi!"
        )

        # Bir nechta adminlarga yuborish
        for admin_id in ADMINS:
            await bot.send_message(chat_id=admin_id, text=text)
