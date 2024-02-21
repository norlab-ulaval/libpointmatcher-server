from user.user import User
from user.user_repo import UserRepo
from auth.auth import get_password_hash, verify_password
from user.user_validation import validate
from auth.token import create_access_token
from fastapi import HTTPException, status


class UserController:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    async def get_all_users(self) -> list[User]:
        return await self.user_repo.find_all()
    
    async def find_by_username(self, username: str) -> User:
        return await self.user_repo.find_username(username)

    async def find_by_email(self, email: str) -> User:
        return await self.user_repo.find_email(email)
    
    async def find_user(self, email: str, password: str) -> User:
        return await self.user_repo.find(email, password)         
    
    async def register(self, username: str, email: str, password: str):
        hashed_password = get_password_hash(password)
        user = await self.find_by_username(username)
        if user is None:
            validate(username, email, password)
            await self.user_repo.add_user(username, email, hashed_password)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Username already used")
    
    async def authenticate(self, email: str, password: str) -> dict:
        user = await self.find_by_email(email)
        if user is None or not verify_password(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect email or password",
                                headers={"WWW-Authenticate": "Bearer"})
    
        access_token = create_access_token(user)
        return {"access_token": access_token, "token_type": "bearer"}
