from user.user import User
from user.user_repo import UserRepo
from auth.auth import get_password_hash, verify_password
from user.user_validation import validate
from auth.token import create_access_token, remove_token, get_validated_email
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
        if await self.user_repo.does_user_exist(username=username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Username already used")
        elif await self.user_repo.does_user_exist(email=email):
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
    
    async def logout(self, user: User):
        if remove_token(user.email) is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Could not logout user")    
            
        return {"message": "User logged out successfully"}
    
    async def get_current_user(self, token: str):
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
        
        email = get_validated_email(token)
        if email is None:
            raise credential_exception

        user = await self.find_by_email(email)
        if user is None:
            raise credential_exception

        return user
