''' Unit tests for shorten_url '''
from unittest.mock import patch
import pytest

from app.api.generate_short_url import generate_short_url
from app.db.models.url_pair import UrlPair
from app.db.services.validate_url_unique import validate_url_unique
from app.api.exceptions import KeyExistsError


@patch('app.db.models.url_pair.UrlPair.get')
def test_validate_short_url_unique(mock_get):
    ''' Test validating that a short url is unique '''
    # Setup the mock to raise a DoesNotExist exception, simulating a unique user provided short URL
    mock_get.side_effect = UrlPair.DoesNotExist()

    short_url = validate_url_unique("12345678")
    assert len(short_url) == 8
    assert short_url == "12345678"

@patch('app.db.models.url_pair.UrlPair.get')
def test_validate_short_url_collision(mock_get):
    ''' Test we throw the proper error when there is a collision'''
    # Setup the mock to cause a collision and test that a KeyExistsError is thrown
    mock_get.return_value = UrlPair(short_url="12345678", url="https://existing-url.com")

    with pytest.raises(KeyExistsError):
        validate_url_unique("12345678")

@patch('app.db.models.url_pair.UrlPair.get')
def test_generate_short_url_unique(mock_get):
    ''' Test we properly generate a unique short_url '''
    # Setup the mock to raise a DoesNotExist exception, simulating a unique short URL
    mock_get.side_effect = UrlPair.DoesNotExist()

    short_url = generate_short_url()
    assert len(short_url) == 8

@patch('app.api.generate_short_url.validate_url_unique')
def test_generate_short_url_collision(mock_validate):
    '''Test that our generation function rejects and regenerates short urls that cause collisions'''
    # Setup the mock to return a valid response, simulating a collision in short URL
    # validate that generate_short_url returns still returns a valid short_url
    mock_validate.side_effect = [
                            KeyExistsError(422,
                                        "Short URL already exists, please enter a new short URL."),
                            "12345678"
                            ]


    short_url = generate_short_url()
    mock_validate.assert_called()
    assert short_url == "12345678"
