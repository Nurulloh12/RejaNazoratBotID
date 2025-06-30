from aiogram import Router, F
from aiogram.types import Message
from database.db import get_tasks_by_user

router = Router()

@router.message(F.text == "📋 Rejalarni ko‘rish")
async def view_tasks(message: Message):
    tasks = await get_tasks_by_user(message.from_user.id)
    if not tasks:
        await message.answer("📭 Sizda hozircha hech qanday reja yo‘q.")
    else:
        text = "🗂 Sizning rejalaringiz:\n\n"
        for i, (task,) in enumerate(tasks, 1):
            text += f"{i}. {task}\n"
        await message.answer(text)