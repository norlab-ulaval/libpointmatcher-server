from datetime import datetime


class Iteration:
    def __init__(self, rotation_error: float, translation_error: float, transformation: list[list[float]]):
        self.rotation_error = rotation_error
        self.translation_error = translation_error
        self.transformation = transformation


class Evaluation:
    def __init__(self, run_id: str, user_email: str, type: str, evaluation_name: str, file_name: str,
                 iterations: list[Iteration], date: datetime, anonymous: bool):
        self.run_id = run_id
        self.user_email = user_email
        self.type = type
        self.evaluation_name = evaluation_name
        self.file_name = file_name
        self.iterations = iterations
        self.date = date
        self.anonymous = anonymous
