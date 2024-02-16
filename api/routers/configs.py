from fastapi import APIRouter, Header, Depends
from typing import Annotated

from auth.auth import get_current_user
from interface.interface_models import User

router = APIRouter()

@router.get("/configs")
def get_configs(user: Annotated[User, Depends(get_current_user)]):
    return {"configs": "configs"}