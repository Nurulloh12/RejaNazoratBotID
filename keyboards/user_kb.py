from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎯 Referal havola")],
            [KeyboardButton(text="⭐️ Mening yulduzlarim")],
            [KeyboardButton(text="🏆 Reyting")],
            [KeyboardButton(text="ℹ️ Ma'lumot"), KeyboardButton(text="📋 Yordam")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
