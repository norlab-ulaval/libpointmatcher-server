from evaluation.evaluation import Evaluation


class EvaluationRepo:
    async def fetch_history_from_email(self, email: str) -> list[Evaluation]:
        pass

    async def save(self, evaluation: Evaluation):
        pass
