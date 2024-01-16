from uuid import UUID
from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from app.database.session import async_session_maker
from app.database.models import Contest
from app.schemas.contest import ContestSchema, ProblemSchema

contest_router = APIRouter()


@contest_router.get("/contests", response_model=List[ContestSchema], tags=['contests'])
async def get_contests():
    async with async_session_maker() as session:
        query = select(Contest)
        res = await session.execute(query)
        res = res.all()
    return res


@contest_router.get("/contests/{contest_id}", response_model=ContestSchema, tags=['contests'])
async def get_contest_by_id(contest_id: UUID):
    async with async_session_maker() as session:
        query = select(Contest).filter(Contest.id == contest_id)
        res = await session.execute(query)
        res = res.scalar_one_or_none()
    return res


@contest_router.get("/contests/{contest_id}/problems", response_model=List[ProblemSchema], tags=['contests'])
async def get_contest_by_id_problems(contest_id: UUID):
    async with async_session_maker() as session:
        query = select(Contest.problems).filter(Contest.id == contest_id)
        res = await session.execute(query)
        res = res.all()
    return res
