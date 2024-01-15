from app.schemas.schemas import *
from fastapi import APIRouter
from sqlalchemy import select
from app.database.session import async_session_maker
from app.database.models import Problem

problem_router = APIRouter()


@problem_router.get("/problems", response_model=GetProblemsResponse)
def show_problems():
    with async_session_maker() as session:
        query = select(Problem)
        session.execute(query)
    return query


@problem_router.get("/problem/{problem_id}", response_model=GetProblemResponse)
def show_contest(problem_id: str):
    with async_session_maker() as session:
        query = select(Problem).filter(Problem.id == problem_id)
        session.execute(query)
    return query
