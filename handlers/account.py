from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "ℹ️ Ma'lumot")
async def info_message(message: Message):
    await message.answer(
        "ℹ️ <b>Stars Bot haqida</b>\n\n"
        "Stars Bot — bu siz do‘stlaringizni botga taklif qilib, ⭐️ yulduzlar yig‘adigan motivatsion o‘yin tarzidagi bot.\n\n"
        "🎯 Har bir taklif qilingan foydalanuvchi uchun 1 ta ⭐️ olasiz.\n"
        "🏆 Eng ko‘p yulduz yig‘ganlar reytingda yuqoriga chiqadi.\n"
        "🎁 Kelajakda esa eng faol ishtirokchilarga bonuslar yoki sovg‘alar berilishi mumkin!\n\n"
        "🫂 Yulduz to‘plashni hoziroq boshlang, va do‘stlaringizni taklif qiling!\n\n"
        "<i>— Stars bilan yulduzingiz porlasin ⭐️</i>"
    )
