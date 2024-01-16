from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from app.database.session import async_session_maker
from app.database.models import Problem
from app.schemas.problem import ProblemSchema

problem_router = APIRouter()


@problem_router.get("/problems", response_model=List[ProblemSchema], tags=['problems'])
async def show_problems():
    async with async_session_maker() as session:
        query = select(Problem)
        res = await session.execute(query)
        res = res.all()
    return res


@problem_router.get("/problem/{problem_id}", response_model=ProblemSchema, tags=['problems'])
async def show_contest(problem_id: str):
    async with async_session_maker() as session:
        query = select(Problem).filter(Problem.id == problem_id)
        res = await session.execute(query)
        res = res.scalar_one_or_none()
        return res
