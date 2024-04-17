import logging

from fastapi.testclient import TestClient
import pytest
from api.generate_short_url import generate_short_url
from db.models.url_pair import Url_Pair
from api import exceptions
from db.services.validate_url_unique import validate_url_unique

current_db_state = {
  "587ec2a0": "https://www.google.com/",
  "f4256843": "https://www.bing.com/",
  "9c983138": "https://www.yahoo.com/",
  "JHiTvkTu": "https://www.facebook.com/",
  # Once added during tests
  "testing1": "https://www.google.com/"
}

def clear_url():
    # Clear out pair created for testing
    try:
        Url_Pair.get("testing1").delete()
    except:
        pass

def test_validate_url():
    # Ensure validate_url_unique returns the short_url back if it is unique
    short_url = validate_url_unique("12345678")
    assert short_url == "12345678"

def test_validate_url_invalid():
    # Verify that if a key already exists we get the proper error
    with pytest.raises(exceptions.KeyExistsError) as KeyExistsError:
        validate_url_unique("587ec2a0")
        assert type(KeyExistsError) == exceptions.KeyExistsError
        # As well as the proper HTTP code and detail msg
        assert KeyExistsError.status_code == 422
        assert KeyExistsError.detail == "Short URL already exists, please enter a new short URL."

def test_generate_url():
    # Test generating a short url
    short_url = generate_short_url()
    # Validate it is the correct length
    assert len(short_url) == 8
    assert type(short_url) == str

def test_shorten_url_valid(client: TestClient):
    # Test shortening a URL that does not already exist
    response = client.post("/shorten_url?url=https%3A%2F%2Fwww.google.com%2F&short_url=testing1")
    # Ensure we get the correct response code (201 CREATED) and that the response returns the created pair
    assert response.status_code == 201
    assert response.json() == {
                            "short_url": "https://127.0.0.1:8000/testing1",
                            "url": current_db_state["testing1"]
                            }
    
def test_shorten_url_invalid(client: TestClient):
    # Same as valid, as valid creates a short_url making the second request a collision
    response = client.post("/shorten_url?url=https%3A%2F%2Fwww.google.com%2F&short_url=testing1")
    assert response.status_code == 422
    assert response.json() == { "detail": "Short URL already exists, please enter a new short URL." }

def test_shorten_url_invalid_url(client: TestClient):
    # Attempt to create a short url with an invalid URL
    response = client.post("/shorten_url?url=definitelynotaurl.fake&short_url=testing1")

    # Validate the error is correct and relevant
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'url_parsing'
    assert detail["loc"] == ["query", "url"]
    assert detail["msg"] == "Input should be a valid URL, relative URL without a base"
    assert detail["input"] == "definitelynotaurl.fake"

def test_shorten_url_invalid_short_url(client: TestClient):
    # Attempt to create a short url with a provided short_url that is too long
    response = client.post("/shorten_url?url=https%3A%2F%2Fwww.google.com%2F&short_url=shorturlthatisobviouslytoolong")

    # Validate the error is correct and relevant
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'string_too_long'
    assert detail["loc"] == ["query", "short_url"]
    assert detail["msg"] == "String should have at most 8 characters"
    assert detail["input"] == "shorturlthatisobviouslytoolong"