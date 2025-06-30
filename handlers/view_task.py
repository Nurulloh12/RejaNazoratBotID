from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from database.db import get_tasks_by_user

router = Router()

@router.message(Command("view"))
async def view_tasks(message: Message):
    user_id = message.from_user.id
    tasks = await get_tasks_by_user(user_id)

    if not tasks:
        await message.answer("📭 Sizda hozircha hech qanday vazifa yo‘q.")
        return

    task_list = "\n".join([f"{idx+1}. {task[0]}" for idx, task in enumerate(tasks)])
    await message.answer(f"🗂 Sizning vazifalaringiz:\n\n{task_list}")