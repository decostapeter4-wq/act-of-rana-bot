"""Small offline tests for the search result contract."""
from unittest.mock import patch
import main


def test_search_web_maps_ddgs_fields():
    class FakeDDGS:
        def __enter__(self):
            return self
        def __exit__(self, *args):
            return False
        def text(self, query, max_results):
            assert query == "python docs"
            assert max_results == 2
            return iter([{
                "title": "Python",
                "href": "https://python.org",
                "body": "Official site",
            }])

    with patch.object(main, "DDGS", FakeDDGS):
        assert main.search_web("python docs", 2) == [{
            "title": "Python",
            "url": "https://python.org",
            "snippet": "Official site",
        }]


def test_empty_query_returns_empty():
    assert main.search_web("   ") == []
