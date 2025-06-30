from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.admin_keyboard import admin_panel_keyboard
from database.db import get_all_users, get_active_users
from states.broadcast_state import BroadcastState

router = Router()

# 👤 Admin ID
ADMIN_IDS = [7293959501]  # O‘zingizning Telegram ID'ingizni yozing

# 🔐 Admin tekshiruvi
def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS

# 🧭 /admin komandasi — admin panelga kirish
@router.message(Command("admin"))
async def show_admin_panel(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("👮‍♂️ Admin panelga xush kelibsiz!", reply_markup=admin_panel_keyboard())

# 📊 Faol foydalanuvchilar tugmasi
@router.message(F.text == "📊 Faol foydalanuvchilar")
async def show_active_users(message: Message):
    if not is_admin(message.from_user.id):
        return
    users = await get_active_users()
    await message.answer(f"📊 So‘nggi 24 soatda faol foydalanuvchilar: <b>{len(users)}</b>")

# 📈 Umumiy foydalanuvchilar tugmasi
@router.message(F.text == "📈 Umumiy statistika")
async def show_all_users(message: Message):
    if not is_admin(message.from_user.id):
        return
    users = await get_all_users()
    await message.answer(f"📈 Umumiy foydalanuvchilar soni: <b>{len(users)}</b>")

# 📤 Xabar yuborish tugmasi — matn so‘rash
@router.message(F.text == "📤 Xabar yuborish")
async def ask_broadcast_message(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        return
    await message.answer("✍️ Yuboriladigan xabar matnini kiriting:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(BroadcastState.waiting_for_message)

# ✅ Xabarni qabul qilib, yuborish
@router.message(BroadcastState.waiting_for_message)
async def process_broadcast_message(message: Message, state: FSMContext):
    users = await get_all_users()
    success = 0

    for user in users:
        try:
            await message.bot.send_message(user[0], message.text)
            success += 1
        except Exception as e:
            print(f"⚠️ Yuborilmadi: {user[0]} | Sabab: {e}")

    await message.answer(f"✅ Xabar {success} ta foydalanuvchiga yuborildi.")
    await state.clear()