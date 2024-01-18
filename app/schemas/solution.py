from uuid import UUID
from typing import List

from pydantic import BaseModel

from app.schemas.problem import TestVerdictSchema


class SolutionSchema(BaseModel):
    id: UUID | None = None
    code: str
    problem: UUID
    user: UUID
    verdicts: List[TestVerdictSchema] | None = None
    
