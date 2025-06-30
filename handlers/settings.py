from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.user_states import UserSettingsState
from database.db import save_user_settings

router = Router()

@router.message(F.text.lower() == "🛠 sozlamalar")
async def start_settings(message: Message, state: FSMContext):
    await message.answer("⏰ Uyg'onish vaqtini kiriting (masalan: 06:30):")
    await state.set_state(UserSettingsState.wake_time)

@router.message(UserSettingsState.wake_time)
async def set_wake_time(message: Message, state: FSMContext):
    await state.update_data(wake_time=message.text)
    await message.answer("🕗 Baholash vaqtini kiriting (masalan: 22:00):")
    await state.set_state(UserSettingsState.review_time)

@router.message(UserSettingsState.review_time)
async def set_review_time(message: Message, state: FSMContext):
    await state.update_data(review_time=message.text)
    await message.answer("📚 Yo‘nalishingizni kiriting (masalan: Dasturlash):")
    await state.set_state(UserSettingsState.category)

@router.message(UserSettingsState.category)
async def set_category(message: Message, state: FSMContext):
    data = await state.get_data()
    wake_time = data.get("wake_time")
    review_time = data.get("review_time")
    category = message.text

    await save_user_settings(message.from_user.id, wake_time, review_time, category)
    await state.clear()
    await message.answer("✅ Sozlamalar saqlandi! Har kuni sizga eslatmalar yuboriladi.")