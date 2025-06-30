from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from database.db import get_tasks_by_user, delete_task_by_index

router = Router()

# --- Holatlar ---
class DeleteTaskState(StatesGroup):
    choosing_task = State()

# --- /delete komandasi ---
@router.message(F.text == "/delete")
async def delete_task_start(message: Message, state: FSMContext):
    tasks = await get_tasks_by_user(message.from_user.id)
    if not tasks:
        await message.answer("📭 Sizda hech qanday reja yo‘q.")
        return

    task_list = "\n".join([f"{i+1}. {task[0]}" for i, task in enumerate(tasks)])
    await message.answer(f"🗑 Qaysi vazifani o‘chirmoqchisiz?\n\n{task_list}\n\nIltimos, raqamini kiriting:")
    await state.set_state(DeleteTaskState.choosing_task)

# --- Raqamni qabul qilish va o‘chirish ---
@router.message(DeleteTaskState.choosing_task)
async def delete_task_confirm(message: Message, state: FSMContext):
    tasks = await get_tasks_by_user(message.from_user.id)

    try:
        index = int(message.text) - 1
        if index < 0 or index >= len(tasks):
            raise ValueError
    except ValueError:
        await message.answer("❌ Noto‘g‘ri raqam. Iltimos, ro‘yxatdagi raqamni kiriting.")
        return

    task_to_delete = tasks[index][0]
    await delete_task_by_index(message.from_user.id, task_to_delete)
    await message.answer(f"✅ \"{task_to_delete}\" vazifasi o‘chirildi.", reply_markup=ReplyKeyboardRemove())
    await state.clear()