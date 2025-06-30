from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import hbold

from keyboards.inline import time_keyboard, category_keyboard
from database.db import save_user_settings, add_user

router = Router()

# --- HOLATLAR ---
class RegistrationState(StatesGroup):
    wake_time = State()
    review_time = State()
    category = State()

# --- /start komandasi ---
@router.message(F.text == "/start")
async def start_command(message: Message, state: FSMContext):
    await add_user(message.from_user.id)  # Foydalanuvchini bazaga qo‘shamiz
    await message.answer(
        "👋 <b>Assalomu alaykum!</b>\n"
        "⏰ Keling, kundalik eslatmalarni sozlaymiz!\n\n"
        "Quyidan uyg‘onish vaqtini tanlang:",
        reply_markup=time_keyboard("wake")
    )
    await state.set_state(RegistrationState.wake_time)

# --- Uyg‘onish vaqti tanlanganda ---
@router.callback_query(RegistrationState.wake_time)
async def select_wake_time(callback: CallbackQuery, state: FSMContext):
    wake_time = callback.data
    await state.update_data(wake_time=wake_time)
    await callback.message.edit_text(
        "🌙 Endi baholash vaqtini tanlang:",
        reply_markup=time_keyboard("review")
    )
    await state.set_state(RegistrationState.review_time)

# --- Baholash vaqti tanlanganda ---
@router.callback_query(RegistrationState.review_time)
async def select_review_time(callback: CallbackQuery, state: FSMContext):
    review_time = callback.data
    await state.update_data(review_time=review_time)
    await callback.message.edit_text(
        "🎯 Endi yo‘nalishingizni tanlang:",
        reply_markup=category_keyboard()
    )
    await state.set_state(RegistrationState.category)

# --- Yo‘nalish tanlanganda ---
@router.callback_query(RegistrationState.category)
async def select_category(callback: CallbackQuery, state: FSMContext):
    category = callback.data
    data = await state.get_data()
    await save_user_settings(
        user_id=callback.from_user.id,
        wake_time=data["wake_time"],
        review_time=data["review_time"],
        category=category
    )
    await callback.message.edit_text(
        f"{hbold('✅ Muvaffaqiyatli saqlandi!')} Rejalaringizga sodiq bo‘ling! 💪"
    )
    await state.clear()