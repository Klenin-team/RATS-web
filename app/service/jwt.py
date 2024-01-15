from datetime import datetime, timezone, timedelta
from typing import Dict, Annotated

from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import select, nulls_first

from app.settings import get_settings
from app.database.session import async_session_maker
from app.database.models import User
from app.schemas.jwt import TokenData


class JwtAuthentication:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    async def _verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    async def _get_password_hash(self, password):
        return self.pwd_context.hash(password)

    async def _get_user(self, login:str):
        async with async_session_maker() as session:
            query = (select(User).where(User.login==login))
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


    def create_access_token(self, data: Dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            get_settings().WEB_SECRET_KEY,
            algorithm=get_settings().JWT_ALGORYTHM,
        )
        return encoded_jwt

    # async def get_current_user(self, token: Annotated[str, Depends(oauth2_scheme)]):
    #     credentials_exception = HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Could not validate credentials",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )

    #     try:
    #         payload = jwt.decode(
    #             token,
    #             get_settings().WEB_SECRET_KEY,
    #             algorithms=[get_settings().JWT_ALGORYTHM]
    #             )
    #         username: str = payload.get("sub")
    #         if username is None:
    #             raise credentials_exception
    #         token_data = TokenData(username=username)
    #     except JWTError:
    #         raise credentials_exception
        
    #     user = get_user(username=token_data.username)
    #     if user is None:
    #         raise credentials_exception
    #     return user
