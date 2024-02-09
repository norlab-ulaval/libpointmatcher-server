from fastapi import APIRouter, HTTPException, status
from datetime import timedelta

from interface.interface_models import Token, RegisteringUser
from database import db
from user.user_controller import UserController


user_controller: UserController

router = APIRouter()

@router.post("/register")
def register_user(user: RegisteringUser):
    user_controller.register(user.username, user.email, user.password)
    
    return {"message": "User registered successfully",
            "user": user}

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: RegisteringUser):
    return user_controller.authenticate(form_data.username, form_data.password)