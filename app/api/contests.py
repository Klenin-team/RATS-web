from uuid import UUID
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select, update

from app.database.session import async_session_maker
from app.database.models import Contest
from app.schemas.contest import ContestSchema, ProblemSchema, ContestSchemaID

contest_router = APIRouter()


@contest_router.get("/contests", response_model=List[ContestSchemaID], tags=['contests'])
async def get_contests():
    session = async_session_maker()
    query = select(Contest)
    res = await session.execute(query)
    res = res.scalars().all()
    return res


@contest_router.get("/contests/{contest_id}", response_model=ContestSchema, tags=['contests'])
async def get_contest_by_id(contest_id:UUID):
    session = async_session_maker()
    query = select(Contest).filter(Contest.id == contest_id)
    res = await session.execute(query)
    res = res.scalar_one_or_none()
    return res


@contest_router.get("/contests/{contest_id}/problems", response_model=List[ProblemSchema], tags=['contests'])
async def get_contest_by_id_problems(contest_id: UUID):
    session = async_session_maker()
    query = select(Contest.problems).filter(Contest.id == contest_id)
    res = await session.execute(query)
    res = res.scalars().all()
    return res


@contest_router.put("/contests", tags=['contests'])
async def add_contest(contest: ContestSchemaID):
    session = async_session_maker()
    c = Contest(
        title=contest.title,
        problems=contest.problems,
        participants=contest.participants
    )
    session.add(c)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)

## NOT WORKING
@contest_router.patch("/contests/{contest_id}", tags=['contests', 'broken'])
async def edit_contest(contest: ContestSchemaID, contest_id: UUID):
    session = async_session_maker()
    c = Contest(
        title=contest.title,
        problems=contest.problems,
        participants=contest.participants
    )

    query = update(Contest).where(Contest.id == contest_id).values(
        title=contest.title,
        problems=contest.problems,
        participants=contest.participants
    )
    await session.execute(query)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)
