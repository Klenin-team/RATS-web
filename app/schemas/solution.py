from uuid import UUID
from typing import List

from pydantic import BaseModel

from app.schemas.problem import TestVerdict


class SolutionSchema(BaseModel):
    id: UUID | None = None
    code: str
    problem: UUID
    user: UUID
    solutions: List[TestVerdict] | None = None
    
