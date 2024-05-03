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
    name: str = Field(default_factory=str)


@router.get("/evaluation")
async def get_evaluations(user: Annotated[User, Depends(get_authorized_user)]):
    return await evaluation_controller.get_evaluations(user)


@router.get("/run")
async def get_runs(user: Annotated[User, Depends(get_authorized_user)]):
    return await evaluation_controller.get_evaluations_grouped_by_run_id(user)


@router.post("/evaluation")
async def new_evaluation(evaluation: NewEvaluation, user: Annotated[User, Depends(get_authorized_user)]):
    return await evaluation_controller.evaluate_config(user, evaluation.config, evaluation.anonymous, evaluation.name)

@router.get("/files")
async def get_files():
    return evaluation_controller.get_files()
