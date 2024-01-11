from functools import lru_cache

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.main import get_settings


engine = create_async_engine(get_settings().get_postgres_url())
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


@lru_cache
async def get_async_session():
    async with async_session_maker() as session:
        yield session
