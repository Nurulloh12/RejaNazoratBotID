import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode

from config import BOT_TOKEN
from handlers import start, referal, rating, account, help, info
from middlewares.check_subs import CheckSubscriptionMiddleware  # kelajak uchun

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Routerlarni qo‘shish
dp.include_routers(
    start.router,
    referal.router,
    rating.router,
    account.router,
    help.router,
    info.router
)

# Boshlanishda
async def on_startup(bot: Bot):
    logging.info("🚀 Bot ishga tushdi!")

# To‘xtaganda
async def on_shutdown(bot: Bot):
    logging.info("🛑 Bot to‘xtadi.")

# Asosiy ishga tushirish funksiyasi
async def main():
    logging.basicConfig(level=logging.INFO)
    
    # Middleware ni hozircha o‘chirib qo‘yganmiz, keyin yoqamiz:
    # dp.message.middleware(CheckSubscriptionMiddleware())

    await on_startup(bot)
    await dp.start_polling(bot)
    await on_shutdown(bot)

if __name__ == "__main__":
    asyncio.run(main())
