from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.chat_type import ChatType

from keyboards.user_kb import main_menu
from database import get_user, add_user, update_stars
from utils.functions import notify_admin_if_10_stars

router = Router()

@router.message(Command("start"), F.chat.type == ChatType.PRIVATE)
async def cmd_start(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    text_args = message.text.split()

    # Referalni ajratib olish
    ref_id = None
    if len(text_args) > 1 and text_args[1].isdigit():
        ref_id = int(text_args[1])
        if ref_id == user_id:
            ref_id = None  # O'zini o'ziga refer qilsa, hisoblanmaydi

    # Foydalanuvchi bazada bormi?
    user = await get_user(user_id)
    if not user:
        await add_user(user_id=user_id, username=username, invited_by=ref_id)

        # Refererga yulduz qo‘shish
        if ref_id:
            new_stars = await update_stars(ref_id)
            await notify_admin_if_10_stars(ref_id, new_stars, message.bot)

    await message.answer(
        "🎉 <b>Stars Botga xush kelibsiz!</b>\n\n"
        "👥 Do‘stlaringizni taklif qiling va ⭐️ yulduzlar to‘plang!",
        reply_markup=main_menu()
    )
