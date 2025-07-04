from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "📋 Yordam")
async def help_message(message: Message):
    await message.answer(
        "📋 <b>Yordam</b>\n\n"
        "Botdan foydalanish juda oson 👇\n\n"
        "🎯 <b>Referal havola</b> — do‘stlaringizni taklif qilish uchun havolangizni olasiz.\n"
        ⭐️ <b>Mening yulduzlarim</b> — qancha odam chaqirganingizni ko‘rasiz.\n"
        "🏆 <b>Reyting</b> — eng ko‘p yulduz yig‘gan Top 10 foydalanuvchini ko‘rsatadi.\n\n"
        "👥 Har bir do‘stingiz uchun 1 ta ⭐️ olasiz.\n"
        "🔟 10 ta do‘st chaqirsangiz — siz haqingizda adminlarga xabar yuboriladi ✅\n\n"
        "Agar biror muammo bo‘lsa yoki savolingiz bo‘lsa, admin bilan bog‘laning: @Rakh1mov_xalol"
    )
