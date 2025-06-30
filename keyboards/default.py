from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Rejalarim")],
        [KeyboardButton(text="⚙️ Sozlamalar")],
    ],
    resize_keyboard=True
)