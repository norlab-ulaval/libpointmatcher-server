from motor.core import AgnosticDatabase, AgnosticCollection

from evaluation.evaluation import Evaluation, Iteration
from evaluation.evaluation_repo import EvaluationRepo
from leaderboard.leaderboard_entry import LeaderboardEntry
from leaderboard.leaderboard_repo import LeaderboardRepo


def _to_json(evaluation: Evaluation):
    iterations = []

    for iteration in evaluation.iterations:
        iterations.append({
            'rotation_error': iteration.rotation_error,
            'translation_error': iteration.translation_error,
            'transformation': iteration.transformation
        })

    return {
        'run_id': evaluation.run_id,
        'user_email': evaluation.user_email,
        'type': evaluation.type,
        'evaluation_name': evaluation.evaluation_name,
        'file_name': evaluation.file_name,
        'iterations': iterations,
        'date': evaluation.date,
        'anonymous': evaluation.anonymous
    }


def _from_json(json):
    iterations = []

    for iteration_json in json['iterations']:
        iterations.append(Iteration(iteration_json['rotation_error'], iteration_json['translation_error'],
                                    iteration_json['transformation']))

    return Evaluation(json['run_id'], json['user_email'], json['type'], json['evaluation_name'],
                      json['file_name'], json['iterations'], json['date'], json['anonymous'])


class EvaluationMongo(EvaluationRepo):
    def __init__(self, mongo_database: AgnosticDatabase):
        self.collection: AgnosticCollection = mongo_database['evaluations']

    async def fetch_history_from_email(self, email: str) -> list[Evaluation]:
        evaluations = []

        cursor = (self.collection
                  .find({'user_email': email})
                  .sort([("date", -1)]))

        for doc in await cursor.to_list(length=None):
            evaluations.append(_from_json(doc))

        return evaluations

    async def save(self, evaluation: Evaluation):
        await self.collection.insert_one(_to_json(evaluation))

