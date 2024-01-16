from uuid import UUID
from typing import List
from enum import Enum

from pydantic import BaseModel

from app.schemas.contest import ProblemSchema


class Verdicts(Enum):
    ok = 'OK'
    re = 'RE'
    tl = 'TL'
    ml = 'ML'
    wa = 'WA'
    ce = 'CE'
    se = 'SE'


class Test(BaseModel):
    id: UUID | None = None
    problem: ProblemSchema
    input: str
    output: str    


class TestVerdict(BaseModel):
    id: UUID | None = None
    verdict: Verdicts
    compilation_output: str
    runtime_output: str
    used_ram: int    # Bytes
    used_time: int   # Miliseconds
    test: Test
