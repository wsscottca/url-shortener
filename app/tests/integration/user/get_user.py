''' Integration tests for getting the current user '''

from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi.testclient import TestClient
from app.api.auth.dependencies import ALGORITHM, SECRET_KEY
from app.tests.integration.auth.token import test_token


def test_get_user(client: TestClient):
    ''' Test getting our user when we have a valid JWT authorization token '''
    response = client.get("/users/me",
                          headers={"Authorization": f"Bearer {test_token(client).access_token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "test"

def test_get_user_expired(client: TestClient):
    ''' Test attempting to get the current user with an expired token'''
    expires = datetime.now(timezone.utc) - timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Test getting our user when we have a valid token
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    detail = response.json()["detail"]
    assert detail == "ExpiredSignatureError('Signature has expired.')"

def test_get_user_invalid(client: TestClient):
    ''' Test when a username does not exist '''
    expires = datetime.now(timezone.utc) + timedelta(minutes=5)
    token = jwt.encode({"sub": "test9", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    # Test getting our user when we have a valid token
    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert detail == "User does not exist."
