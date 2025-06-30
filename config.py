import os
from dotenv import load_dotenv

load_dotenv()  # .env fayldan o‘qish uchun

TOKEN = os.getenv("BOT_TOKEN")

# Admin ID lar ro‘yxati (o‘zingiznikini yozing)
ADMINS = [7293959501]

# Agar kerak bo‘lsa boshqa sozlamalarni ham shu yerga qo‘shamiz