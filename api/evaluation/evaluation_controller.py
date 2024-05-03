import uuid
import os
import csv
from datetime import datetime

from evaluation.evaluation import Evaluation, Iteration
from evaluation.evaluation_repo import EvaluationRepo
from evaluation.evaluator import Evaluator
from evaluation.new_evaluation_listener import NewEvaluationListener
from user.user import User


class EvaluationController:
    def __init__(self, evaluator: Evaluator, evaluation_repo: EvaluationRepo, new_evaluation_listener: NewEvaluationListener):
        self.evaluator = evaluator
        self.evaluation_repo = evaluation_repo
        self.new_evaluation_listener = new_evaluation_listener

    async def evaluate_config(self, user: User, config: str, anonymous: bool, evaluation_name: str = ""):
        run_id = str(uuid.uuid4())
        date = datetime.utcnow()

        evaluation_results = self.evaluator.evaluate_config(config)

        new_evaluations = []
        for result_type in evaluation_results.keys():
            evaluations_of_type = evaluation_results.get(result_type)

            for file_name in evaluations_of_type.keys():
                file_evaluation = evaluations_of_type.get(file_name)

                translation_errors = file_evaluation.get("error_translation")
                rotation_errors = file_evaluation.get("error_rotation")
                transformations = file_evaluation.get("transformations")

                if len(translation_errors) and len(translation_errors) == len(rotation_errors) == len(transformations):
                    iterations = []

                    for i in range(0, len(translation_errors)):
                        iterations.append(Iteration(rotation_errors[i], translation_errors[i], transformations[i]))

                    evaluation = Evaluation(run_id, user.email, result_type, evaluation_name, file_name, iterations, date,
                                            anonymous)

                    new_evaluations.append(evaluation)

        for evaluation in new_evaluations:
            await self.evaluation_repo.save(evaluation)

        await self.new_evaluation_listener.notify_batch(new_evaluations)

    async def get_evaluations(self, user: User):
        return await self.evaluation_repo.fetch_history_from_email(user.email)

    async def get_evaluations_grouped_by_run_id(self, user: User) -> dict[str, list[Evaluation]]:
        evaluations = await self.evaluation_repo.fetch_history_from_email(user.email)

        groups: dict[str, list[Evaluation]] = {}
        for evaluation in evaluations:
            if evaluation.run_id not in groups.keys():
                groups[evaluation.run_id] = []
            groups[evaluation.run_id].append(evaluation)

        return groups
    
    def get_files(self):
        filepath = "/app/data/"
        directories = [[x[0], x[2]] for x in  os.walk(filepath) if x[0] != filepath]
        
        ordered_files = {}
        for diff_path, files in directories:
            difficulty = diff_path.split("/")[-1]

            if ordered_files.get(difficulty) is None:
                ordered_files[difficulty] = {}

            for i, file in enumerate(files):
                cloud_path = diff_path + "/" + file

                if ordered_files.get(difficulty).get(file) is None:
                    ordered_files[difficulty][file] = []

                with open(cloud_path, "r") as f:
                    csv_reader = csv.DictReader(f)
                    for line in csv_reader:
                        ordered_files[difficulty][file].append(line)                


        return ordered_files
