from enum import Enum

class ScoreType(Enum):
    HIGH_SCORE = "high_score"
    LOW_SCORE = "low_score"
    ALL = "all"
    UNKNOWN = "unknown"

    @staticmethod
    def from_str(label):
        if label is None:
            return ScoreType.UNKNOWN
        if label.lower() == "high_score":
            return ScoreType.HIGH_SCORE
        if label.lower() == "low_score":
            return ScoreType.LOW_SCORE
        if label.lower() == "all":
            return ScoreType.ALL
        return ScoreType.UNKNOWN