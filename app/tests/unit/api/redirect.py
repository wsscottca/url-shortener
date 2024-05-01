''' Unit tests for redirect function '''
from unittest.mock import patch

import pytest
from app.api.exceptions import KeyDoesNotExistError
from app.db.services.redirect import get_redirect_url
from app.db.models.url_pair import UrlPair

@patch("app.db.services.redirect.UrlPair.get")
def test_get_redirect_url_exists(mock_get):
    ''' Test our redirect function under correct conditions '''
    # Set up mock to "get a url pair" from our db
    mock_get.return_value = UrlPair(short_url="12345678", url="https://existing-url.com")

    # Validate the get_redirect_url returns the url to redirect to
    redirect_url = get_redirect_url("12345678")
    assert redirect_url == "https://existing-url.com"

@patch("app.db.services.redirect.UrlPair.get")
def test_get_redirect_url_does_not_exist(mock_get):
    ''' Test redirect function when the short_url is not in DB '''
    # Set up mock to simulate the short_url we're trying to get does not exist
    mock_get.side_effect = UrlPair.DoesNotExist()

    # Validate the proper error is thrown
    with pytest.raises(KeyDoesNotExistError):
        get_redirect_url("12345678")
