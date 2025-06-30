

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from database.db import get_all_users
from aiogram import Bot

async def send_motivation(bot: Bot):
    users = await get_all_users()
    now = datetime.now().strftime("%H:%M")
    
    for user_id, wake_time, review_time, category in users:
        # Faqat review_time bilan solishtirib yuboramiz
        if now == review_time:
            await bot.send_message(
                chat_id=user_id,
                text=(
                    f"🌙 <b>Baholash vaqti keldi!</b>\n"
                    f"📚 Bugungi <b>{category}</b> bo‘yicha rejalaringizni ko‘zdan kechiring.\n\n"
                    f"🕗 Soat: {review_time}"
                ),
                parse_mode="HTML"
            )

def setup_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler(timezone="Asia/Tashkent")
    scheduler.add_job(send_motivation, "interval", minutes=1, args=[bot])
    scheduler.start()