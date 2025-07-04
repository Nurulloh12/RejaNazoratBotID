from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Umumiy foydalanuvchilar")],
            [KeyboardButton(text="🟢 Faol foydalanuvchilar")],
            [KeyboardButton(text="📤 Xabar yuborish")],
            [KeyboardButton(text="🔗 Kanal ulash"), KeyboardButton(text="❌ Kanal uzish")],
        ],
        resize_keyboard=True
    )
