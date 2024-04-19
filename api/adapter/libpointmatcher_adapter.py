import json

from websockets.sync.client import connect
from os import environ as env

from evaluation.evaluator import Evaluator


class LibpointmatcherAdapter(Evaluator):
    def evaluate_config(self, config: str) -> dict[str, dict[str, dict[str, list]]]:
        with connect(f"ws://{env.get('LIBPOINTMATCHER_WS', 'localhost:8765')}") as websocket:
            websocket.send(config)
            results = websocket.recv()
            return json.loads(results)
