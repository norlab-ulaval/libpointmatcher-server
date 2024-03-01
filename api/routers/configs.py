from fastapi import APIRouter, Depends
from typing import Annotated

from interface.interface_models import User
from user.user_controller import UserController
from routers.util.authorization import get_authorized_user

user_controller: UserController

router = APIRouter()

@router.get("/configs")
def get_configs(user: Annotated[User, Depends(get_authorized_user)]):
    return {"configs": "configs"}