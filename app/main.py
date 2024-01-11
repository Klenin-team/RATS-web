from fastapi import FastAPI

from app.settings import get_settings
from app.database.session import init_models


app = FastAPI()
