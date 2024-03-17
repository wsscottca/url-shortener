from unittest.mock import patch

import pytest
from api import exceptions
from api.redirect import get_redirect_url
from models.url_pair import Url_Pair

@patch("models.url_pair.Url_Pair.get")
def test_get_redirect_url_exists(mock_get):
    mock_get.return_value = Url_Pair(short_url="12345678", url="https://existing-url.com")

    redirect_url = get_redirect_url("12345678")
    assert redirect_url == "https://existing-url.com"

@patch("models.url_pair.Url_Pair.get")
def test_get_redirect_url_does_not_exist(mock_get):
    mock_get.side_effect = Url_Pair.DoesNotExist()
    
    with pytest.raises(exceptions.KeyError):
        get_redirect_url("12345678")