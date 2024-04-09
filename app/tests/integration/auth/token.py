from datetime import timedelta, timezone
import datetime

from jose import jwt
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

def test_decode_token():
    # Create a fake token (outside our api)
    expires = datetime.now(timezone.utc) + timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Verify our decode function properly decodes it
    assert decode_token(token)["sub"] == "test1"

def test_token(client):
    # Test that our route properly creates a token when given the correct data
    response = client.post("/token", data={"username": "test", "password": "test", "grant_type": "password"},
                           headers={"content-type": "application/x-www-form-urlencoded"})
    assert response.status_code == 200
    response_data = response.json()
    assert "access_token" in response_data
    assert response_data["token_type"] == "bearer"
    return Token(access_token=response_data["access_token"], token_type=response_data["token_type"])