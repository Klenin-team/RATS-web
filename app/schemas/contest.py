from uuid import UUID
from typing import List

from pydantic import BaseModel


class ProblemSchema(BaseModel):
    id: UUID | None = None
    title: str
    memory_limitation: int # Bytes
    time_limitation: int # Miliseconds
    text: str
    input_file: str
    output_file: str

    class Config:
        orm_mode = True


class ContestSchema(BaseModel):
    id: UUID | None = None
    title: str
    problems: List[ProblemSchema] | None = None
    participants: List['UserSchema'] = []

    class Config:
        orm_mode = True


class UserSchema(BaseModel):
    id: UUID | None = None
    login: str
    password: str | None = None
    full_name: str | None = None 
    contests: List[ContestSchema] = []

    class Config:
        orm_mode = True
