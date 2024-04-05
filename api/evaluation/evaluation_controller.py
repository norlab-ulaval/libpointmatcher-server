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

    async def evaluate_config(self, user: User, config: str, anonymous: bool, name: str = ""):
        run_id = str(uuid.uuid4())
        date = datetime.utcnow()

        results = self.evaluator.evaluate_config(config)

        for result_type in results.keys():
            result = results.get(result_type)

            evaluation = Evaluation(run_id, user.email, result_type, result, date, anonymous, name)

            await self.evaluation_repo.save(evaluation)

    async def get_evaluations(self, user: User):
        return await self.evaluation_repo.fetch_history_from_email(user.email)
