from datetime import datetime, timezone, timedelta
from typing import Dict

from fastapi import status, HTTPException, Response
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import select, insert

from app.settings import get_settings
from app.database.models import User
from app.database.session import async_session_maker

class JwtAuthentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def _verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def _get_password_hash(self, password):
        return self.pwd_context.hash(password)

    async def _get_user(self, login: str):
        async with async_session_maker() as session:
            query = select(User).filter_by(login=login)
            res = await session.execute(query)
            res = res.scalar_one_or_none()
        return res
            
    async def authenticate_user(self, login: str, password: str):
        wrong_credentials = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="logint or password does not exist",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = await self._get_user(login=login)
        if not user:
            raise wrong_credentials
        user.password
        if not self._verify_password(password, user.password):
            raise wrong_credentials
        return user

    async def create_user(self, login, password):
        async with async_session_maker() as session:
            query = insert(User).values(
                    login=login,
                    password=self.pwd_context.hash(password)
                    )
            await session.execute(query)
            await session.commit()
            return Response('Created')

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
