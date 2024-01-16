from uuid import UUID
from typing import List

from pydantic import BaseModel

from app.schemas.contest import UserSchema


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: str | None = None
    resent_contest: UUID | None = None


