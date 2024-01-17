from uuid import UUID
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select, update

from app.database.session import async_session_maker
from app.database.models import Problem
from app.schemas.problem import ProblemSchema

problem_router = APIRouter()


@problem_router.get("/problems", response_model=List[ProblemSchema], tags=['problems'])
async def show_problems():
    session = async_session_maker()
    query = select(Problem)
    res = await session.execute(query)
    res = res.scalars().all()
    return res


@problem_router.get("/problem/{problem_id}", response_model=ProblemSchema, tags=['problems'])
async def show_contest(problem_id: str):
    session = async_session_maker()
    query = select(Problem).filter(Problem.id == problem_id)
    res = await session.execute(query)
    res = res.scalar_one_or_none()
    return res


@problem_router.put("/problem", tags=['problems'])
async def add_contest(problem: ProblemSchema):
    session = async_session_maker()
    c = Problem(
        title = problem.title,
        memory_limitation = problem.memory_limitation,
        time_limitation = problem.time_limitation,
        text = problem.text,
        input_file = problem.input_file,
        output_file = problem.output_file
    )
    session.add(c)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)


@problem_router.patch("/problems/{problem_id}", tags=['problems', 'broken'])
async def edit_contest(problem: ProblemSchema, problem_id: UUID):
    session = async_session_maker()
    query = update(Problem).where(Problem.id == problem_id).values(
        title = problem.title,
        memory_limitation = problem.memory_limitation,
        time_limitation = problem.time_limitation,
        text = problem.text,
        input_file = problem.input_file,
        output_file = problem.output_file
    )
    await session.execute(query)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)
