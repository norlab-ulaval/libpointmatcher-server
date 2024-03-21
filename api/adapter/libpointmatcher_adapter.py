import json

from websockets.sync.client import connect
from os import environ as env

from evaluation.evaluator import Evaluator
from evaluation.result import Result


class LibpointmatcherAdapter(Evaluator):
    def evaluate_config(self, config: str) -> Result:
        with connect(f"ws://{env.get('LIBPOINTMATCHER_WS', 'localhost:8765')}") as websocket:
            websocket.send('test')
            results = websocket.recv()
            return json.loads(results)
