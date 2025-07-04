from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from utils.channel import get_channel_link
from aiogram.methods.get_chat_member import GetChatMember
from typing import Callable, Awaitable, Any

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict], Awaitable[Any]],
        event: Message,
        data: dict
    ) -> Any:
        channel_link = get_channel_link()
        if not channel_link:
            return await handler(event, data)

        try:
            # @channel_name chiqaramiz
            channel_username = channel_link.split("t.me/")[-1]
            member = await event.bot.get_chat_member(chat_id=f"@{channel_username}", user_id=event.from_user.id)

            if member.status in ["left", "kicked"]:
                # Agar obuna bo‘lmagan bo‘lsa, eventni o'tkazmaydi
                return
        except Exception as e:
            print("Majburiy obuna tekshiruvda xato:", e)
            return

        return await handler(event, data)
