import asyncio

from fastapi import FastAPI

from database.session import init_models
from settings import get_settings


get_settings()
asyncio.run(init_models())

app = FastAPI()
