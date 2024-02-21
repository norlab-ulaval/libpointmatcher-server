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

    async def does_user_exist(self, username=None, email=None) -> bool:
        user_username = await self.find_by_username(username) if username is not None else None
        user_email = await self.find_by_email(email) if email is not None else None

        return user_username is not None or user_email is not None

    async def register(self, username: str, email: str, password: str):
        if await self.does_user_exist(username=username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Username already used")
        elif await self.does_user_exist(email=email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Email already used")
        else:
            validate(username, email, password)
            hashed_password = get_password_hash(password)
            await self.user_repo.add_user(username, email, hashed_password)
    
    async def authenticate(self, email: str, password: str) -> dict:
        user = await self.find_by_email(email)
        if user is None or not verify_password(password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Incorrect email or password",
                                headers={"WWW-Authenticate": "Bearer"})
    
        access_token = create_access_token(user)
        return {"access_token": access_token, "token_type": "bearer"}
