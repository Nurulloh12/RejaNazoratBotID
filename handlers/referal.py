from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "🎯 Referal havola")
async def referal_link(message: Message):
    user_id = message.from_user.id
    bot_username = (await message.bot.get_me()).username

    link = f"https://t.me/{bot_username}?start={user_id}"

    await message.answer(
        f"🎯 <b>Sizning referal havolangiz:</b>\n\n"
        f"<code>{link}</code>\n\n"
        "Ushbu havolani do‘stlaringizga yuboring. Har bir taklif qilganingiz uchun 1 ta ⭐️ olasiz!"
    )
