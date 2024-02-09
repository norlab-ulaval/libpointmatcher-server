from user.user import User
from user.user_repo import UserRepo
import auth.auth
from fastapi import HTTPException, status
from datetime import datetime, timedelta


class UserController:
    
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def get_all_users(self) -> list[User]:
        return await self.user_repo.find_all()

    async def find_username(self, username: str) -> User:
        return await self.user_repo.find_username()
    
    async def find_user(self, username: str, password: str) -> User:
        return await self.user_repo.find()
    
    async def register(self, username: str, email: str, password: str):
        hashed_password = auth.get_password_hash(password)
        user = self.find_username(username)
        if not user:
            await self.user_repo.add({"username": username, "email": email, "hashed_password": hashed_password})
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Username already used")
    
    async def authenticate(self, username: str, password: str):
        hashed_pass = auth.get_password_hash(password)
        user = self.find_user(username, hashed_pass)
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
        access_token_expires = timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth.create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}