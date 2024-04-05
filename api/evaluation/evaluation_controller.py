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
        run_id = str(uuid.uuid4())
        date = datetime.utcnow()

        results = self.evaluator.evaluate_config(config)

        for result_type in results.keys():
            result = results.get(result_type)

            evaluation = Evaluation(run_id, user.email, result_type, result, date, anonymous)

            await self.evaluation_repo.save(evaluation)

    async def get_evaluations(self, user: User):
        return await self.evaluation_repo.fetch_history_from_email(user.email)

    async def get_evaluations_grouped_by_run_id(self, user: User) -> dict[str, list[Evaluation]]:
        evaluations = await self.evaluation_repo.fetch_history_from_email(user.email)

        groups: dict[str, list[Evaluation]] = {}
        for evaluation in evaluations:
            if evaluation.run_id not in groups.keys():
                groups[evaluation.run_id] = []
            groups[evaluation.run_id].append(evaluation)

        return groups
