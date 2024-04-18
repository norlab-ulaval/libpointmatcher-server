import uuid
from datetime import datetime

from evaluation.evaluation import EvaluationOld, Evaluation, Iteration
from evaluation.evaluation_repo import EvaluationRepo
from evaluation.evaluator import Evaluator
from user.user import User


class EvaluationController:
    def __init__(self, evaluator: Evaluator, evaluation_repo: EvaluationRepo):
        self.evaluator = evaluator
        self.evaluation_repo = evaluation_repo

    async def evaluate_config(self, user: User, config: str, anonymous: bool, evaluation_name: str = ""):
        # To decode the file use something like :
        # base64.b64decode(config).decode('utf-8')
        run_id = str(uuid.uuid4())
        date = datetime.utcnow()

        results = self.evaluator.evaluate_config(config)

        for result_type in results.keys():
            result = results.get(result_type)

            evaluation = Evaluation(run_id, user.email, result_type, evaluation_name, 'demo.csv', [Iteration(result, result, [])], date, anonymous)

            await self.evaluation_repo.save(evaluation)

    async def get_evaluations(self, user: User):
        evaluations = await self.evaluation_repo.fetch_history_from_email(user.email)

        return self.evaluation_old_convert(evaluations)

    async def get_evaluations_grouped_by_run_id(self, user: User) -> dict[str, list[EvaluationOld]]:
        evaluations = await self.evaluation_repo.fetch_history_from_email(user.email)

        evaluations = self.evaluation_old_convert(evaluations)

        groups: dict[str, list[EvaluationOld]] = {}
        for evaluation in evaluations:
            if evaluation.run_id not in groups.keys():
                groups[evaluation.run_id] = []
            groups[evaluation.run_id].append(evaluation)

        return groups

    def evaluation_old_convert(self, evaluations: list[Evaluation]) -> list[EvaluationOld]:
        evaluations_old = []

        for e in evaluations:
            evaluations_old.append(EvaluationOld(e.run_id, e.user_email, e.type, e.iterations[0].rotation_error,
                                                 e.date, e.anonymous, e.evaluation_name))

        return evaluations_old
