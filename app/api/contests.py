from app.schemas.schemas import *
from fastapi import APIRouter
from sqlalchemy import select
from app.database.session import async_session_maker
from app.database.models import Contest

contest_router = APIRouter()


@contest_router.get("/contests", response_model=GetContestsResponse)
def show_contests():
    with async_session_maker() as session:
        query = select(Contest)
        session.execute(query)
    return query


@contest_router.get("/contests/{contest_id}", response_model=ContestSchema)
def show_contest(contest_id: str):
    with async_session_maker() as session:
        query = select(Contest).filter(Contest.id == contest_id)
        session.execute(query)
    return query


@contest_router.get("/contests/{contest_id}/problems", response_model=GetContestProblemsResponse)
def show_contests(contest_id: str):
    with async_session_maker() as session:
        query = select(Contest).filter(Contest.id == contest_id)
        row = session.execute(query)
    return row
