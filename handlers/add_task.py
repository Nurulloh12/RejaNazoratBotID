from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from database.db import add_task_to_db

router = Router()

class AddTaskState(StatesGroup):
    waiting_for_task = State()

@router.message(Command("add"))
async def start_add_task(message: Message, state: FSMContext):
    await message.answer("📝 Iltimos, vazifani kiriting:")
    await state.set_state(AddTaskState.waiting_for_task)

@router.message(AddTaskState.waiting_for_task, F.text)
async def receive_task(message: Message, state: FSMContext):
    task_text = message.text
    await add_task_to_db(message.from_user.id, task_text)
    await message.answer("✅ Vazifa saqlandi!")
    await state.clear()