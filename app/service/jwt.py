from datetime import datetime, timezone, timedelta
from typing import Dict

from fastapi import status, HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import session

from app.settings import get_settings
from app.database.session import async_session_maker
from app.database.models import User


class JwtAuthentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def _verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def _get_password_hash(self, password):
        return self.pwd_context.hash(password)

    async def _get_user(self, login:str):
        async with async_session_maker() as session:
            query = select(User).where(User.login==login)
            row = await session.execute(query)
            return row.first()
    
    async def authenticate_user(self, username: str, password: str):
        wrong_credentials = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="logint or password does not exist",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = self._get_user(username)
        if not user:
            raise wrong_credentials
        if not self._verify_password(password, user.password):
            raise wrong_credentials
        return user


    async def create_user(self, login, password):
        async with async_session_maker() as session:
            query = insert(User).values(
                    name=login, 
                    password=self.pwd_context.hash(password)
                    )
            return await session.execute(query)

    async def create_access_token(self, data: Dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + timedelta()
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            get_settings().WEB_SECRET_KEY,
            algorithm=get_settings().JWT_ALGORYTHM,
        )
        return encoded_jwt

