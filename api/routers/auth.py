from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

from auth.auth import get_current_user
from interface.interface_models import Token, RegisteringUser, User
from user.user_controller import UserController

user_controller: UserController

router = APIRouter()

@router.post("/register")
async def register_user(user: RegisteringUser):
    await user_controller.register(user.username, user.email, user.password)

    return {"message": "User registered successfully",
            "user": user}


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return await user_controller.authenticate(form_data.username, form_data.password)

@router.post("/logout")
async def logout_user(user: Annotated[User, Depends(get_current_user)]):
    return await user_controller.logout(user)
