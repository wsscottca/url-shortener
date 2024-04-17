from datetime import datetime, timedelta, timezone
import logging

from fastapi.testclient import TestClient
from jose import ExpiredSignatureError, JWTError, jwt
import pytest
from api.auth.create_token import create_token
from api.auth.decode_token import decode_token
from api.auth.dependencies import ALGORITHM, SECRET_KEY, TOKEN_EXPIRE_MINUTES
from api.models.token import Token

def test_create_token():
    # Create a fake token
    token_expiration = timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    token = create_token(data={"sub": "test1"}, expires_delta=token_expiration)
    assert type(token) == str
    # Test that it is a valid token by decoding it outside the bounds of our api
    assert jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)["sub"] == "test1"

def test_create_token_expired():
    # Create a fake token
    token_expiration = timedelta(minutes=-TOKEN_EXPIRE_MINUTES)
    token = create_token(data={"sub": "test1"}, expires_delta=token_expiration)
    assert type(token) == str
    # Test that it is an expired token by decoding it outside the bounds of our api
    with pytest.raises(ExpiredSignatureError):
        assert jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)["sub"] == "test1"

def test_decode_token():
    # Create a fake token (outside our api)
    expires = datetime.now(timezone.utc) + timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Verify our decode function properly decodes it
    assert decode_token(token)["sub"] == "test1"

def test_decode_token_expired():
    # Create a fake token (outside our api)
    expires = datetime.now(timezone.utc) - timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Verify our decode function properly raises the ExpiredSignatureError
    with pytest.raises(ExpiredSignatureError):
        decode_token(token)

def modify_token(token):
    modified = "".split(token)
    modified[len(modified)//2] = "?"
    modified = "".join(modified)
    return modified

def test_decode_token_modified():
    # Create a fake token (outside our api)
    expires = datetime.now(timezone.utc) + timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Verify our decode function properly raises the JWTError
    with pytest.raises(JWTError):
        decode_token(modify_token(token))

def test_token(client: TestClient):
    # Test that our route properly creates a token when given the correct data
    response = client.post("/token", data={"username": "test", "password": "password", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})
    
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"
    return Token(access_token=response_data["access_token"], token_type=response_data["token_type"])

def test_token_missing_username(client: TestClient):
    # Test that our route properly identifies a missing username
    response = client.post("/token", data={"password": "test", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == "missing"
    assert "username" in detail['loc']
    assert detail["msg"] == "Field required"

def test_token_missing_password(client: TestClient):
    # Test that our route properly identifies a missing password
    response = client.post("/token", data={"username": "test", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == "missing"
    assert "password" in detail['loc']
    assert detail["msg"] == "Field required"

def test_token_invalid_content_type(client: TestClient):
    # Test that our route properly creates a token when given the correct data
    response = client.post("/token", data={"username": "test", "password": "test", "grant_type": "password"},
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

def test_token_wrong_grant(client: TestClient):
    # Test that our route properly creates a token when given the correct data
    response = client.post("/token", data={"username": "test", "password": "test", "grant_type": "authorization_code"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    # Verify the error is specific to the grant type being incorrect
    assert response.status_code == 422
    detail = response.json()["detail"][0]
    assert detail["type"] == "string_pattern_mismatch"
    assert "grant_type" in detail['loc']
    assert detail["msg"] == "String should match pattern 'password'"
    assert detail["input"] == "authorization_code"

def test_token_invalid_username_short(client: TestClient):
    # Test that our route properly identifies a missing username
    response = client.post("/token", data={"username": "sho", "password": "test", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail == "Username not within length bounds. Username must be between 4-16 characters."

def test_token_invalid_username_long(client: TestClient):
    # Test that our route properly identifies a missing username
    response = client.post("/token", data={"username": "longusernamethatisinvalid", "password": "test", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail == "Username not within length bounds. Username must be between 4-16 characters."

def test_token_invalid_password_short(client: TestClient):
    # Test that our route properly identifies a missing username
    response = client.post("/token", data={"username": "test", "password": "shortpa", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail == "Password not within length bounds. Password must be between 8-32 characters."

def test_token_invalid_password_long(client: TestClient):
    # Test that our route properly identifies a missing username
    response = client.post("/token", data={"username": "test", "password": "longpasswordthatisinvalidasitistoolong", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})

    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail == "Password not within length bounds. Password must be between 8-32 characters."