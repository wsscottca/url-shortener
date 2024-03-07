from api.shorten_url import generate_short_url, validate_short_url
from models.url_pair import Url_Pair
from api import exceptions

current_db_state = {
  "587ec2a0": "https://www.google.com/",
  "f4256843": "https://www.bing.com/",
  "9c983138": "https://www.yahoo.com/",
  "JHiTvkTu": "https://www.facebook.com/",
  # Once added during tests
  "testing1": "https://www.google.com/"
}

def clear_url():
    try:
        Url_Pair.get("testing1").delete()
    except:
        pass

def test_validate_url():
    short_url = validate_short_url("12345678")
    assert short_url == "12345678"

def test_validate_url_invalid():
    try:
        validate_short_url("587ec2a0")
    except exceptions.KeyExistsError as KeyExistsError:
        assert type(KeyExistsError) == exceptions.KeyExistsError
        assert KeyExistsError.status_code == 422
        assert KeyExistsError.detail == "Short URL already exists, please enter a new short URL."

def test_generate_url():
    short_url = generate_short_url()
    assert len(short_url) == 8
    assert type(short_url) == str

def test_shorten_url_valid(client):
    response = client.post("/shorten_url?url=https%3A%2F%2Fwww.google.com%2F&short_url=testing1")
    assert response.status_code == 201
    assert response.json() == {
                            "short_url": "https://127.0.0.1:8000/testing1",
                            "url": current_db_state["testing1"]
                            }
    
def test_shorten_url_invalid(client):
    
        # Same as valid, as valid creates a short_url making the second request a collision
        response = client.post("/shorten_url?url=https%3A%2F%2Fwww.google.com%2F&short_url=testing1")
        assert response.status_code == 422
        assert response.json() == { "detail": "Short URL already exists, please enter a new short URL." }