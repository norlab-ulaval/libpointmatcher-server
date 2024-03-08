class LeaderboardEntry:
    username = ""
    score = ""
    score_type = ""
    version = ""
    date = ""

    def __init__(self, username=None, score=None, score_type=None, version=None, date=None):
        self.username = username
        self.score = score
        self.score_type = score_type
        self.version = version
        self.date = date