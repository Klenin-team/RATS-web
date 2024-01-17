from typing import List
from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert

from app.database.session import async_session_maker
from app.database.models import Solution
from app.schemas.solution import SolutionSchema
from app.service.queue import QueueInterface

solution_router = APIRouter()


@solution_router.get("/solutions", response_model=List[SolutionSchema], tags=['solutions'])
async def show_solutions():
    async with async_session_maker() as session:
        query = select(Solution)
        res = await session.execute(query)
        res = res.all()
    return res


@solution_router.put("/solutions", tags=['solutions'])
async def put_problems(solution: SolutionSchema):
    await QueueInterface.add_solutiion(solution)
    async with async_session_maker() as session:
        query = insert(Solution).values(
            code=solution.code,
            problem=solution.problem,
            user=solution.user)
        await session.execute(query)
        await session.commit(query)
    return JSONResponse({"status": "OK"}, status_code=200)


@solution_router.get("/solutions/{user_id}/{task_id}", response_model=List[SolutionSchema], tags=['solutions'])
async def show_single_solution(task_id: UUID, user_id: UUID):
    async with async_session_maker() as session:
        query = select(Solution).filter(Solution.user == user_id, Solution.problem == task_id)
        res = await session.execute(query)
        res = res.all()
    return res


