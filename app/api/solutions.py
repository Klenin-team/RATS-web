from typing import List, runtime_checkable
from uuid import UUID, uuid4

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy import select

from app.database.session import async_session_maker
from app.database.models import Problem, Solution, TestVerdict, Test, User
from app.schemas.solution import SolutionSchema
from app.schemas.problem import TestVerdictSchema
from app.service.queue import QueueInterface

solution_router = APIRouter()


@solution_router.get("/solutions", response_model=List[SolutionSchema], tags=['solutions'])
async def show_solutions():
    session = async_session_maker()
    query = select(Solution)
    res = await session.execute(query)
    res = res.scalars().all()
    return res


@solution_router.put("/solutions", tags=['solutions'])
async def put_problems(solution: SolutionSchema):
    solution.id = uuid4()
    # await QueueInterface.add_solutiion(solution)
    session = async_session_maker()
    c = Solution(
        id=solution.id,
        code=solution.code,
        problem=(await session.execute(select(Problem).filter(Problem.id == solution.problem))).one(),
        user=(await session.execute(select(User).filter(User.id == solution.user))).one()
    )
    session.add(c)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)


@solution_router.get("/solutions/{user_id}/{task_id}", response_model=List[SolutionSchema], tags=['solutions'])
async def show_single_solution(task_id: UUID, user_id: UUID):
    session = async_session_maker()
    query = select(Solution).filter(Solution.user == user_id, Solution.problem == task_id)
    res = await session.execute(query)
    res = res.scalars().all()
    return res


@solution_router.put("/verdicts/{solution_id}", tags=['solutions'])
async def put_verdicts(solution_id: UUID, verdicts: List[TestVerdictSchema]):
    session = async_session_maker()
    
    c = [TestVerdict(
            verdict=v.verdict,
            compilation_output=v.compilation_output,
            runtime_output = v.runtime_output,
            used_ram = v.used_ram,
            used_time = v.used_time,
            test = (await session.execute(select(Test).filter(Test.id == v.test))).one(),
            solution = v.solution
        ) for v in verdicts]
    session.add(c)
    await session.commit()
    return JSONResponse({"status": "OK"}, status_code=200)
