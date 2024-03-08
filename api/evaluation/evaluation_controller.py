from evaluation.evaluator import Evaluator


class EvaluationController:
    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def evaluate_config(self, config: str):
        result = self.evaluator.evaluate_config(config)
        print(result)
