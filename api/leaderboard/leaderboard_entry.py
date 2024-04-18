from pydantic import BaseModel
from datetime import datetime


class LeaderboardEntryOld:
    def __init__(self, username: str, score: float, score_type: str, version: str,
                 date: datetime):
        self.username = username
        self.score = score
        self.score_type = score_type
        self.version = version
        self.date = date


class LeaderboardEntry:
    def __init__(self, file_name: str, type: str, user_email: str, rotation_error: float, translation_error: float,
                 date: datetime, release_version: str):
        self.file_name = file_name
        self.type = type
        self.user_email = user_email
        self.rotation_error = rotation_error
        self.translation_error = translation_error
        self.date = date
        self.release_version = release_version
