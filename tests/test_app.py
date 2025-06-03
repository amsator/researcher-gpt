from fastapi.testclient import TestClient
from unittest.mock import patch
import os
import sys
import types

stub = types.ModuleType("langchain_community")
stub.chat_models = types.ModuleType("chat_models")
class _ChatOpenAI:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return ""

stub.chat_models.ChatOpenAI = _ChatOpenAI
sys.modules.setdefault("langchain_community", stub)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app

client = TestClient(app.app)


def test_post_root():
    with patch('app.agent', lambda *args, **kwargs: {"output": "result"}):
        response = client.post('/', json={'query': 'hi'})
        assert response.status_code == 200
        assert response.json() == 'result'
