import json
from time import sleep
from collections import deque
from websockets.sync.client import connect
from os import environ as env
from evaluation.evaluator import Evaluator
from uuid import uuid4

queue = deque()


class LibpointmatcherAdapter(Evaluator):
    def evaluate_config(self, config: str) -> dict[str, dict[str, dict[str, list]]]:
        ticket = str(uuid4())
        queue.append(ticket)

        while queue[0] != ticket:
            sleep(1)

        try:
            result = self.evaluate(config)
        except Exception as e:
            queue.popleft()
            raise e

        queue.popleft()

        return result

    def evaluate(self, config: str) -> dict[str, dict[str, dict[str, list]]]:
        try:
            with connect(f"ws://{env.get('LIBPOINTMATCHER_WS', 'localhost:8765')}") as websocket:
                websocket.send(config)
                results = websocket.recv()
                return json.loads(results)
        except Exception as e:
            reau