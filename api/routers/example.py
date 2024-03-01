from fastapi import APIRouter
from user.user_controller import UserController


user_controller: UserController


router = APIRouter()


# TODO keep only as example for now
@router.get("/users")
def hello_world():
    return user_controller.get_all_users()
