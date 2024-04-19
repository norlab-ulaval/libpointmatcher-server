import json
import uuid
from time import sleep

from websockets.sync.client import connect
from os import environ as env

from evaluation.evaluator import Evaluator

queue = []


class LibpointmatcherAdapter(Evaluator):
    def evaluate_config(self, config: str) -> dict[str, dict[str, dict[str, list]]]:
        ticket = uuid.UUID()
        queue.append(ticket)

        while queue[0] != ticket:
            sleep(1)

        result = self.evaluate(config)

        queue.pop()

        return result

    def evaluate(self, config: str) -> dict[str, dict[str, dict[str, list]]]:
        with connect(f"ws://{env.get('LIBPOINTMATCHER_WS', 'localhost:8765')}") as websocket:
            websocket.send(config)
            results = websocket.recv()
            return json.loads(results)