from pydantic import BaseModel
from typing import List

# !!!!OTHERS!!!!

class TournamentEntity(BaseModel):
    id: str
    title: str
    start: str
    end: str
    official: bool


class Tasks(BaseModel):
    id: str
    title: str
    last_verdict: str  # ??????????????????????


# !!!!DBTables!!!!

class TestVerdict(BaseModel):
    id: str
    test: str
    verdict: str
    compilation_output: str
    runtime_output: str
    used_ram: int
    used_time: int
    solve: str


class Tests(BaseModel):
    id: str
    problem: str
    input: str
    output: str


class Problem(BaseModel):
    id: str
    title: str
    memory_limitation: int
    time_limitation: int
    text: str
    input_file: str
    output_file: str


class Users(BaseModel):
    id: str
    username: str
    password: str
    real_name: str


class Contest(BaseModel):
    id: str
    title: str
    description: str
    problems: List[Problem]
    participants: List[Users]


class Solution(BaseModel):
    id: str
    problem: Problem
    user: str
    code: str
    language: str


# !!!!ENDPOINTS!!!!
class PostQueueBackendRequest(BaseModel):
    id: str
    code: str
    language: str
    tests: List[List[str]]
    stdio: bool
    input_file: str
    output_file: str


class PostQueueBackendResponse(BaseModel):
    status: bool


class GetQueueRunnerResponse(PostQueueBackendResponse):
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


class GetTournamentsResponse(BaseModel):
    tournaments: List[TournamentEntity]


class GetTournamentRequest(BaseModel):
    tournament_id: str


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
