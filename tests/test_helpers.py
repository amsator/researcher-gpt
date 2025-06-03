import os
import sys
import types
import json
from unittest.mock import patch, Mock

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
from app import search, scrape_website


def test_search_success():
    mock_resp = Mock(status_code=200, text='{"result": "ok"}')
    with patch('requests.post', return_value=mock_resp) as mock_post:
        result = search('hello')
        assert json.loads(result)["result"] == "ok"
        mock_post.assert_called_once()


def test_scrape_success():
    html = '<html><body>content</body></html>'
    mock_resp = Mock(status_code=200, content=html.encode())
    with patch('requests.post', return_value=mock_resp):
        result = scrape_website('objective', 'http://example.com')
        assert 'content' in result
