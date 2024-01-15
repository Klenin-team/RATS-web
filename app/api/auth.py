from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.schemas import User
from app.service.jwt import JwtAuthentication
from app.schemas.jwt import Token

auth_router = APIRouter()


@auth_router.post("/users/login", tags=["users"])
async def login_for_access_token(credentials: User) -> Token:
    jwt = JwtAuthentication()
    user = await jwt.authenticate_user(credentials.login, credentials.password)
    
    access_token = await jwt.create_access_token(
        data={"sub": user.login})
    return Token(access_token=access_token, token_type="bearer")


@auth_router.post("/users/register", tags=["users"])
async def register(credentials: User):
    return await JwtAuthentication().create_user(credentials.login, credentials.password)
