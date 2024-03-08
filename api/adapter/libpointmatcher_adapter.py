import json

from websockets.sync.client import connect
from os import environ as env


def run_evaluation() -> dict[str, float]:
    with connect(f"ws://{env.get('LIBPOINTMATCHER_WS', 'localhost:8765')}") as websocket:
        websocket.send('test')
        results = websocket.recv()
        return json.loads(results)


print(run_evaluation())
