from fastapi import Depends

from user.user import User
from auth.auth import oauth2_scheme
from user.user_controller import UserController

user_controller: UserController


async def get_authorized_user(token: str = Depends(oauth2_scheme)) -> User:
    return await user_controller.get_current_user(token)
