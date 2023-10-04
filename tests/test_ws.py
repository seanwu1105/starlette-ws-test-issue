from starlette.testclient import TestClient

from main import app

def test_ws():
    test_client = TestClient(app)
    with test_client.websocket_connect("/ws") as websocket:
        assert len(websocket.receive_text()) > 0
