from fastapi import APIRouter, Header, Depends
from typing import Annotated

from auth.auth import get_current_active_user

router = APIRouter()

@router.get("/configs")
def get_configs(x_token: Annotated[str | None, Header(), Depends(get_current_active_user)] = None):
    return {"configs": "configs"}