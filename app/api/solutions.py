from typing import List

from fastapi import APIRouter
from sqlalchemy import select, insert

from app.database.session import async_session_maker
from app.database.models import Solution
from app.schemas.solution import SolutionSchema
from app.service.queue import QueueInterface

solution_router = APIRouter()


@solution_router.get("/solutions", response_model=List[SolutionSchema], tags=['solutions'])
async def show_problems():
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
        res = await session.execute(query)
        res = res.all()
    return res

