from fastapi import APIRouter, Depends
from typing import Annotated
from pydantic import BaseModel, Field

from evaluation.evaluation_controller import EvaluationController
from interface.interface_models import User
from routers.util.authorization import get_authorized_user

evaluation_controller: EvaluationController

router = APIRouter()


class NewEvaluation(BaseModel):
    config: str
    anonymous: bool


@router.post("/evaluation")
async def new_evaluation(evaluation: NewEvaluation, user: Annotated[User, Depends(get_authorized_user)]):
    return await evaluation_controller.evaluate_config(user, evaluation.config, evaluation.anonymous)
