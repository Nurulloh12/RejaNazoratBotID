from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def time_keyboard(mode: str) -> InlineKeyboardMarkup:
    """
    Uyg‘onish va baholash vaqtlarini tanlash uchun klaviatura.
    :param mode: "wake" yoki "review"
    """
    if mode == "wake":
        times = ["05:00", "06:00", "07:00", "08:00", "09:00", "10:00"]
    else:
        times = ["19:00", "20:00", "21:00", "22:00", "23:00"]

    buttons = [
        [InlineKeyboardButton(text=t, callback_data=t)] for t in times
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def category_keyboard() -> InlineKeyboardMarkup:
    """
    Yo‘nalish tanlash uchun klaviatura.
    """
    categories = [
        ("📚 O‘qish", "O‘qish"),
        ("💼 Ish", "Ish"),
        ("💪 Sport", "Sport"),
        ("🎯 Maqsad", "Maqsad"),
        ("🧠 O‘z ustida ishlash", "O‘z ustida ishlash"),
        ("🎨 Boshqa", "Boshqa"),
    ]
    buttons = [
        [InlineKeyboardButton(text=text, callback_data=callback)] for text, callback in categories
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)