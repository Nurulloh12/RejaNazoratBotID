import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
from database.db import create_users_table
from utils.scheduler import setup_scheduler
from handlers import start, add_task, view_tasks, delete_task, settings, admin


async def main():
    # 💾 FSM storage
    storage = MemoryStorage()

    # 🤖 Bot va Dispatcher
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)

    # 🗃 Jadvalni yaratamiz
    await create_users_table()

    # 🧠 Routerlarni ulaymiz
    dp.include_router(start.router)
    dp.include_router(add_task.router)
    dp.include_router(view_tasks.router)
    dp.include_router(delete_task.router)
    dp.include_router(settings.router)
    dp.include_router(admin.router)

    # ⏰ Scheduler (motivatsion xabarlar)
    setup_scheduler(bot)

    # ▶️ Botni ishga tushuramiz
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
