''' All unit tests related to list_urls route or function '''

from unittest.mock import patch

from app.db.services.list_urls import get_urls
from app.db.models.url_pair import UrlPair

@patch('app.db.services.list_urls.UrlPair.scan')
def test_list_url_pairs_empty(mock_scan):
    ''' Test listing urls when DB is empty '''
    # Setup the mock to return an empty db
    mock_scan.return_value = []

    # Validate that this does not break our function and that our function
    # returns an empty dict
    url_pairs = get_urls()
    assert len(url_pairs) == 0

@patch('app.db.services.list_urls.UrlPair.scan')
def test_list_url_pairs_populated(mock_scan):
    ''' Test listing url pairs when DB is populated '''
    # Setup the mock to return a populated db and validate they're properly returned in a dict
    mock_scan.return_value = [
                        UrlPair(short_url="12345678", url="https://existing-url.com"),
                        UrlPair(short_url="12345679", url="https://existing-url2.com")
                        ]

    url_pairs = get_urls()

    assert len(url_pairs) == 2
    assert url_pairs.keys() == {0,1}
    assert url_pairs[0].short_url == "12345678"
    assert url_pairs[1].url == "https://existing-url2.com"
