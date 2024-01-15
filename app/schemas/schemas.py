from pydantic import BaseModel
from typing import List

# !!!!OTHERS!!!!


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


class Problems(BaseModel):
    id: str
    title: str
    memory_limitation: int
    time_limitation: int
    text: str
    input_file: str
    output_file: str


class Users(BaseModel):
    id: str | None = None
    username: str
    password: str
    real_name: str | None = None


class ContestSchema(BaseModel):
    id: str
    title: str
    problems: List[Problems]
    participants: List[Users]


class Solution(BaseModel):
    id: str
    problem: Problems
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


class PostRegisterRequest(BaseModel):
    login: str
    password: str
    real_name: str | None = None


class GetContestsResponse(BaseModel):
    contests: List[ContestSchema]


class PostContestRegisterRequest(BaseModel):
    contest_id: str


class GetContestProblemsRequest(BaseModel):
    contest_id: str


class GetContestProblemsResponse(BaseModel):
    problems: List[Problems]


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


class GetProblemRequest(BaseModel):
    problem_id: str


class GetProblemResponse(BaseModel):
    id: str
    title: str
    memory_limitation: int
    time_limitation: int
    text: str
    input_file: str
    output_file: str


class GetProblemsResponse(BaseModel):
    problems: List[Problems]
