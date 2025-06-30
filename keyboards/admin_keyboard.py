from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_panel_keyboard():
    keyboard = [
        [KeyboardButton(text="📊 Faol foydalanuvchilar")],
        [KeyboardButton(text="📈 Umumiy statistika")],
        [KeyboardButton(text="📤 Xabar yuborish")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)