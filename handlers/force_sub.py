from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from utils.channel import get_channel_link

router = Router()

@router.message()
async def check_subscription_prompt(message: Message):
    link = get_channel_link()
    if link:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="✅ Obuna bo‘ldim", callback_data="check_sub")]
            ]
        )
        await message.answer(
            "❗️ Botdan foydalanish uchun avval kanalga obuna bo‘ling:\n"
            f"{link}",
            reply_markup=keyboard
        )
