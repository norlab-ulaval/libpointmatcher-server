from datetime import datetime


class Evaluation:
    def __init__(self, run_id: str, user_email: str, type: str, result: float, date: datetime, anonymous: bool):
        self.run_id = run_id
        self.user_email = user_email
        self.type = type
        self.result = result
        self.date = date
        self.anonymous = anonymous
        