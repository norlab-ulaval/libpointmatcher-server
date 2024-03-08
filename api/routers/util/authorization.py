from fastapi import Depends

from interface.interface_models import User
from auth.auth import oauth2_scheme
from user.user_controller import UserController

user_controller: UserController

def get_authorized_user(token: str = Depends(oauth2_scheme)) -> User:
    return user_controller.get_current_user(token)