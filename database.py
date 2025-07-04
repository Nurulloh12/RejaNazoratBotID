from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, select, update

DATABASE_URL = "sqlite+aiosqlite:///stars_bot.db"

engine = create_async_engine(DATABASE_URL)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Foydalanuvchi modeli
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True)
    username = Column(String, nullable=True)
    stars = Column(Integer, default=0)
    invited_by = Column(BigInteger, nullable=True)

# Bazani yaratish (once)
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Foydalanuvchini olish
async def get_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        return result.scalar_one_or_none()

# Foydalanuvchini qo‘shish
async def add_user(user_id: int, username: str, invited_by: int = None):
    async with async_session() as session:
        user = User(user_id=user_id, username=username, invited_by=invited_by)
        session.add(user)
        await session.commit()

# Yulduz qo‘shish va qaytarish
async def update_stars(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.user_id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.stars += 1
            await session.commit()
            return user.stars
        return 0
