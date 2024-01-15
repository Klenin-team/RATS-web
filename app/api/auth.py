from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.schemas import Users
from app.service.jwt import JwtAuthentication
from app.schemas.jwt import Token

auth_router = APIRouter()


@auth_router.get("/users/login", tags=["users"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    jwt = JwtAuthentication()
    user = jwt.authenticate_user(form_data.username, form_data.password)
    
    access_token = jwt.create_access_token(
        data={"sub": user.login})
    return Token(access_token=access_token, token_type="bearer")


@auth_router.post("/users/register", tags=["users"])
async def register(user: Users):
    return await JwtAuthentication().create_user(user.username, user.password)
