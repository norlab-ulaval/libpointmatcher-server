import uuid
from datetime import datetime

from evaluation.evaluation import Evaluation
from evaluation.evaluation_repo import EvaluationRepo
from evaluation.evaluator import Evaluator
from user.user import User


class EvaluationController:
    def __init__(self, evaluator: Evaluator, evaluation_repo: EvaluationRepo):
        self.evaluator = evaluator
        self.evaluation_repo = evaluation_repo

    async def evaluate_config(self, user: User, config: str, anonymous: bool):
        date = datetime.utcnow()

        results = self.evaluator.evaluate_config(config)

        for result_type in results.keys():
            run_id = str(uuid.uuid4())
            result = results.get(result_type)

            evaluation = Evaluation(run_id, user.email, result_type, result, date, anonymous)

            await self.evaluation_repo.save(evaluation)
