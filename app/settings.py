from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class SupportedLanguages(Enum):
    gcc = 'gcc'
    gpp = 'g++'
    python = 'python'
    fps = 'fps'


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
    WEB_SECRET_KEY:str
    JWT_ALGORYTHM: str
    JWT_EXPIRES_MINUTES: int

    QUEUE_HOST:str

    POSTGRES_HOST: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    def get_postgres_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"

    
    def get_queue_url(self):
        return f'http://{self.QUEUE_HOST}'


@lru_cache
def get_settings():
    return Settings()
