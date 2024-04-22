import logging
from fastapi.testclient import TestClient
from db.services.get_user import get_user
from db.models.user import User


def test_signup(client: TestClient):
    # Test our route when given the proper information
    response = client.post('/signup', data={"username": "test2", "password": "test2password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 201
    body = response.json()
    assert body["username"] == "test2"
    assert body["msg"] == "User created successfully"

    # Also verify by ensuring the user was saved to the database
    created_user = get_user("test2")
    assert type(created_user) == User
    assert created_user.username == "test2"
    created_user.delete()
    
def test_signup_invalid(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "test1", "password": "test2password"},
                        headers={"content-type": "application/x-www-form-urlencoded"})

    # Ensure the message and status code are correct and relevant
    assert response.status_code == 422
    assert response.json() == { "detail": "Username already exists, please select a different username." }

def test_signup_missing_password(client: TestClient):
    # Test our route when the password is missing from the data
    response = client.post('/signup', data={"username": "test4"},
                        headers={"content-type": "application/x-www-form-urlencoded"})

    # Ensure the message and status code are correct and relevant
    assert response.status_code == 422
    payload = response.json()["detail"][0]
    assert payload["type"] == "missing"
    assert "password" in payload['loc']
    assert payload["msg"] == "Field required"

def test_signup_missing_username(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"password": "test4"},
                        headers={"content-type": "application/x-www-form-urlencoded"})

    # Ensure the message and status code are correct and relevant
    assert response.status_code == 422
    payload = response.json()["detail"][0]
    assert payload["type"] == "missing"
    assert "username" in payload['loc']
    assert payload["msg"] == "Field required"

def test_signup_invalid_content_type(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "test1", "password": "test2"},
                        headers={"content-type": "application/json"})

    # Ensure the message and status code are correct and relevant
    assert response.status_code == 422
    missing_username = response.json()["detail"][0]
    missing_password = response.json()["detail"][1]

    # As the content-type is incorrect the data will be missing
    assert missing_username["type"] == "missing"
    assert "username" in missing_username['loc']
    assert missing_username["msg"] == "Field required"

    assert missing_password["type"] == "missing"
    assert "password" in missing_password['loc']
    assert missing_password["msg"] == "Field required"

def test_signup_long_username(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "thisusernameistoolong", "password": "test2"},
                        headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'string_too_long'
    assert detail["loc"] == ["body", "username"]
    assert detail["msg"] == "String should have at most 16 characters"
    assert detail["input"] == "thisusernameistoolong"

def test_signup_long_password(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "test4", "password": "thisisaverylongpasswordthatwillnotgetaccepted"},
                        headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'string_too_long'
    assert detail["loc"] == ["body", "password"]
    assert detail["msg"] == "String should have at most 32 characters"
    assert detail["input"] == "thisisaverylongpasswordthatwillnotgetaccepted"

def test_signup_short_username(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "sho", "password": "test2"},
                        headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'string_too_short'
    assert detail["loc"] == ["body", "username"]
    assert detail["msg"] == "String should have at least 4 characters"
    assert detail["input"] == "sho"

def test_signup_short_password(client: TestClient):
    # Test our route when the username causes a collision
    response = client.post('/signup', data={"username": "test4", "password": "short"},
                        headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == 'string_too_short'
    assert detail["loc"] == ["body", "password"]
    assert detail["msg"] == "String should have at least 8 characters"
    assert detail["input"] == "short"