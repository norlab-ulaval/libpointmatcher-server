class LeaderboardEntry:
    email = ""
    score = ""
    score_type = ""
    version = ""
    date = ""

    def __init__(self, email=None, score=None, score_type=None, version=None, date=None):
        self.email = email
        self.score = score
        self.score_type = score_type
        self.version = version
        self.date = date