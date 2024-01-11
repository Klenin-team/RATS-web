from functools import lru_cache

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from .models import Base
from app.settings import get_settings



engine = create_async_engine(get_settings().get_postgres_url())
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@lru_cache
async def get_async_session():
    async with async_session_maker() as session:
        yield session
