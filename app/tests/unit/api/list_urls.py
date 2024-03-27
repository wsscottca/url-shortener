from unittest.mock import patch
from db.services.list_urls import get_urls
from db.models.url_pair import Url_Pair

@patch('db.models.url_pair.Url_Pair.scan')
def test_list_url_pairs_empty(mock_scan):
    # Setup the mock to return an empty db
    mock_scan.return_value = []

    # Validate that this does not break our function and that our function
    # returns an empty dict
    url_pairs = get_urls()
    assert len(url_pairs) == 0

@patch('db.models.url_pair.Url_Pair.scan')
def test_list_url_pairs_populated(mock_scan):
    # Setup the mock to return a populated db and validate they're properly returned in a dict
    mock_scan.return_value = [
                        Url_Pair(short_url="12345678", url="https://existing-url.com"),
                        Url_Pair(short_url="12345679", url="https://existing-url2.com")
                        ]

    url_pairs = get_urls()

    assert len(url_pairs) == 2
    assert url_pairs.keys() == {0,1}
    assert url_pairs[0].short_url == "12345678"
    assert url_pairs[1].url == "https://existing-url2.com"