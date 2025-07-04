from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import ADMINS
from keyboards.admin_kb import admin_menu
from states.admin_states import ChannelState
from utils.channel import save_channel_link, get_channel_link, remove_channel_link
from database import async_session, User
from sqlalchemy import select

router = Router()

# /admin komandasi
@router.message(Command("admin"))
async def admin_start(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("🔐 Admin panelga xush kelibsiz!", reply_markup=admin_menu())
    else:
        await message.answer("⛔️ Siz admin emassiz.")

# 📊 Umumiy foydalanuvchilar
@router.message(F.text == "📊 Umumiy foydalanuvchilar")
async def total_users(message: Message):
    if message.from_user.id in ADMINS:
        async with async_session() as session:
            result = await session.execute(select(User))
            users = result.scalars().all()
            await message.answer(f"👥 Umumiy foydalanuvchilar soni: {len(users)} ta")

# 🟢 Faol foydalanuvchilar (faqat bazadagi barcha)
@router.message(F.text == "🟢 Faol foydalanuvchilar")
async def active_users(message: Message):
    if message.from_user.id in ADMINS:
        async with async_session() as session:
            result = await session.execute(select(User))
            users = result.scalars().all()
            # Bu yerda haqiqiy aktivlik mezoni qo‘shilsa bo‘ladi
            await message.answer(f"🟢 Faol foydalanuvchilar: {len(users)} ta (hozircha bazadagi barchasi)")

# 📤 Xabar yuborish (so‘rash)
@router.message(F.text == "📤 Xabar yuborish")
async def ask_broadcast_text(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("📨 Yubormoqchi bo‘lgan xabaringizni kiriting:")
        await state.set_state(ChannelState.waiting_for_channel_link)  # vaqtincha holat nomidan foydalanamiz

# 📤 Xabarni yuborish (bazadagi barcha userlarga)
@router.message(ChannelState.waiting_for_channel_link)
async def broadcast_message(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        text = message.text
        async with async_session() as session:
            result = await session.execute(select(User.user_id))
            user_ids = result.scalars().all()

        count = 0
        for uid in user_ids:
            try:
                await message.bot.send_message(chat_id=uid, text=text)
                count += 1
            except:
                pass
        await message.answer(f"✅ {count} foydalanuvchiga yuborildi.")
        await state.clear()

# 🔗 Kanal ulash
@router.message(F.text == "🔗 Kanal ulash")
async def ask_channel_link(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("🔗 Ulamoqchi bo‘lgan kanal linkini yuboring (masalan: https://t.me/kanalim):")
        await state.set_state(ChannelState.waiting_for_channel_link)

# 🔗 Linkni qabul qilish va saqlash
@router.message(ChannelState.waiting_for_channel_link)
async def save_channel(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        link = message.text.strip()
        if "t.me/" in link:
            save_channel_link(link)
            await message.answer(f"✅ Kanal ulandi:\n{link}")
        else:
            await message.answer("❌ To‘g‘ri link yuboring. Masalan: https://t.me/kanalim")
        await state.clear()

# ❌ Kanal uzish
@router.message(F.text == "❌ Kanal uzish")
async def unlink_channel(message: Message):
    if message.from_user.id in ADMINS:
        remove_channel_link()
        await message.answer("🚫 Kanal ulandi! Obuna tekshiruvi o‘chirildi.")
