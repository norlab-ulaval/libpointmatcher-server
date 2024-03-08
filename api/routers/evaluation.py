from fastapi import APIRouter

from evaluation.evaluation_controller import EvaluationController

evaluation_controller: EvaluationController

router = APIRouter()


@router.post("/evaluation")
def new_evaluation(config: str):
    return evaluation_controller.evaluate_config(config)
