from fastapi import APIRouter

from app.service.jwt import JwtAuthentication
from app.schemas.auth import TokenSchema, UserSchema

auth_router = APIRouter()


@auth_router.post("/users/login", tags=["users"])
async def login_for_access_token(credentials: UserSchema) -> TokenSchema:
    jwt = JwtAuthentication()
    user = await jwt.authenticate_user(credentials.login, credentials.password)
    
    access_token = await jwt.create_access_token(
        data={"sub": user.login})
    return TokenSchema(access_token=access_token, token_type="bearer")


@auth_router.post("/users/register", tags=["users"])
async def register(credentials: UserSchema):
    return await JwtAuthentication().create_user(credentials.login, credentials.password)
