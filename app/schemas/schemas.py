from pydantic import BaseModel
from typing import List


class QueueBackendRequest(BaseModel):
    id: str
    code: str
    language: str
    tests: List[List[str]]
    stdio: bool
    input_file: str
    output_file: str


class QueueBackendResponse(BaseModel):
    status: bool


class QueueRunnerResponse(QueueBackendResponse):
    any: bool


class PostLoginRequest(BaseModel):
    login: str
    password: str


class PostLoginRegisterRequest(BaseModel):
    login: str
    password: str
    real_name: str


class GetTournamentsRequest(BaseModel):
    my: bool


class TournamentEntity(BaseModel):
    id: str
    title: str
    start: str
    end: str
    official: bool


class GetTournamentsResponse(BaseModel):
    tournaments: List[TournamentEntity]


class GetTournamentRequest(BaseModel):
    tournament_id: str


class Tasks(BaseModel):
    id: str
    title: str
    last_verdict: str  # ??????????????????????


class GetTournamentResponse(BaseModel):
    tasks: List[Tasks]


class PostTournamentRegisterRequest(BaseModel):
    tournament_id: str


class GetTaskRequest(BaseModel):
    task_id: str


class GetTaskResponse(BaseModel):
    title: str
    last_verdict: str  # ??????????????????????
    test: str
    memory_limitation: int
    time_limitation: int
    input_file: str
    output_file: str
