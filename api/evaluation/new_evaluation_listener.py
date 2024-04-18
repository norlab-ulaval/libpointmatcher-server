from evaluation.evaluation import Evaluation


class NewEvaluationListener:
    async def notify_batch(self, evaluations: list[Evaluation]):
        pass
