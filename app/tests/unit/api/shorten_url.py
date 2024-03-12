from unittest.mock import patch
from api.shorten_url import generate_short_url, validate_short_url
from models.url_pair import Url_Pair
import shortuuid
from api import exceptions
import pytest

@patch('models.url_pair.Url_Pair.get')
def test_validate_short_url_unique(mock_get):
    # Setup the mock to raise a DoesNotExist exception, simulating a unique user provided short URL
    mock_get.side_effect = Url_Pair.DoesNotExist()

    short_url = validate_short_url("12345678")
    assert len(short_url) == 8
    assert short_url == "12345678"

@patch('models.url_pair.Url_Pair.get')
def test_validate_short_url_collision(mock_get):
    # Setup the mock to cause a collision and test that a KeyExistsError is thrown
    mock_get.return_value = Url_Pair(short_url="12345678", url="https://existing-url.com")

    with pytest.raises(exceptions.KeyExistsError):
        validate_short_url("12345678")

@patch('models.url_pair.Url_Pair.get')
def test_generate_short_url_unique(mock_get):
    # Setup the mock to raise a DoesNotExist exception, simulating a unique short URL
    mock_get.side_effect = Url_Pair.DoesNotExist()

    short_url = generate_short_url()
    assert len(short_url) == 8

@patch('api.shorten_url.validate_short_url')
def test_generate_short_url_collision(mock_validate):
    # Setup the mock to return a valid response, simulating a collision in short URL
    # validate that generate_short_url returns still returns a valid short_url
    mock_validate.side_effect = [
                            exceptions.KeyExistsError(422, "Short URL already exists, please enter a new short URL."),
                            "12345678"
                            ]

    assert generate_short_url() == "12345678"