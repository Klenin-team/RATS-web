from fastapi import FastAPI

from app.api.auth import auth_router
from app.api.contests import contest_router
from app.api.problems import problem_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(contest_router)
app.include_router(problem_router)

