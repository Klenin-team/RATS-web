from uuid import UUID
from typing import List

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert, update

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


@problem_router.put("/problem", tags=['problems'])
async def add_contest(problem: ProblemSchema):
    async with async_session_maker() as session:
        query = select(Problem).filter(Problem.id == problem.id)
        res = await session.execute(query)
        res = res.scalar_one_or_none()
        if res:
            return JSONResponse({"status": "Problem already exist"}, status_code=200)
        else:
            query = insert(Problem).values(
                title=problem.title,
                memory_limitation=problem.memory_limitation,
                time_limitation=problem.time_limitation,
                text=problem.text,
                input_file=problem.input_file,
                output_file=problem.output_file
            )
            await session.execute(query)
            await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)


@problem_router.patch("/problems/{problem_id}", tags=['problems'])
async def edit_contest(problem: ProblemSchema, problem_id: UUID):
    async with async_session_maker() as session:
        query = update(Problem).where(Problem.id == problem_id).values(
            title=problem.title,
            memory_limitation=problem.memory_limitation,
            time_limitation=problem.time_limitation,
            text=problem.text,
            input_file=problem.input_file,
            output_file=problem.output_file
        )
        await session.execute(query)
        await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)
