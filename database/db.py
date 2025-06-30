import aiosqlite
from datetime import datetime, timedelta

DB_NAME = "data.db"

# --- BAZANI YARATISH ---
async def create_users_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                wake_time TEXT,
                review_time TEXT,
                category TEXT,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                task TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                user_id INTEGER PRIMARY KEY,
                language TEXT
            )
        """)
        await db.commit()

# --- FOYDALANUVCHI QO‘SHISH ---
async def add_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users (user_id) VALUES (?)
        """, (user_id,))
        await db.commit()

# --- SOZLAMALARNI SAQLASH ---
async def save_user_settings(user_id: int, wake_time: str, review_time: str, category: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            UPDATE users SET wake_time=?, review_time=?, category=? WHERE user_id=?
        """, (wake_time, review_time, category, user_id))
        await db.commit()

# --- SOZLAMANI O‘QISH ---
async def get_user_settings(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT wake_time, review_time, category FROM users WHERE user_id=?", (user_id,)) as cursor:
            return await cursor.fetchone()

# --- REJA QO‘SHISH ---
async def add_task_to_db(user_id: int, task: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))
        await db.commit()

# --- REJALARNI O‘QISH ---
async def get_tasks_by_user(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT task FROM tasks WHERE user_id=?", (user_id,)) as cursor:
            return await cursor.fetchall()

# --- REJANI O‘CHIRISH ---
async def delete_task_by_index(user_id: int, task: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM tasks WHERE user_id=? AND task=? LIMIT 1", (user_id, task))
        await db.commit()

# --- FAOLLIKNI YANGILASH ---
async def update_last_active(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("UPDATE users SET last_active = CURRENT_TIMESTAMP WHERE user_id = ?", (user_id,))
        await db.commit()

# --- 24 SOAT ICHIDA FAOL FOYDALANUVCHILAR ---
async def get_active_users():
    cutoff = datetime.now() - timedelta(days=1)
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT user_id FROM users WHERE last_active >= ?", (cutoff.strftime('%Y-%m-%d %H:%M:%S'),)) as cursor:
            return await cursor.fetchall()

# --- BARCHA FOYDALANUVCHILAR ---
async def get_all_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT user_id, wake_time, review_time, category FROM users") as cursor:
            return await cursor.fetchall()