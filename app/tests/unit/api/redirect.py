from unittest.mock import patch

import pytest
from api import exceptions
from db.services.redirect import get_redirect_url
from db.models.url_pair import Url_Pair

@patch("db.models.url_pair.Url_Pair.get")
def test_get_redirect_url_exists(mock_get):
    # Set up mock to "get a url pair" from our db
    mock_get.return_value = Url_Pair(short_url="12345678", url="https://existing-url.com")

    # Validate the get_redirect_url returns the url to redirect to
    redirect_url = get_redirect_url("12345678")
    assert redirect_url == "https://existing-url.com"

@patch("db.models.url_pair.Url_Pair.get")
def test_get_redirect_url_does_not_exist(mock_get):
    # Set up mock to simulate the short_url we're trying to get does not exist
    mock_get.side_effect = Url_Pair.DoesNotExist()
    
    # Validate the proper error is thrown
    with pytest.raises(exceptions.KeyError):
        get_redirect_url("12345678")