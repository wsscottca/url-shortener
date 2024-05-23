''' Module contains integration tests for list_urls route '''

from datetime import datetime, timedelta, timezone
from jose import jwt
from fastapi.testclient import TestClient
from app.api.auth.dependencies import ALGORITHM, SECRET_KEY
from app.tests.integration.auth.token import test_token


current_db_state = {
    "0":{"short_url": "587ec2a0", "url": "https://www.google.com/"},
    "1":{"short_url": "f4256843", "url": "https://www.bing.com/"},
    "2":{"short_url": "9c983138", "url": "https://www.yahoo.com/"},
    "3":{"short_url": "JHiTvkTu", "url": "https://www.facebook.com/"}
}

def test_list_urls(client: TestClient):
    ''' Test listing urls from populated DB'''
    response = client.get("/list_urls",
                        headers={"Authorization": f"Bearer {test_token(client).access_token}"})
    assert response.status_code == 200
    assert response.json()[0] == {"short_url": "587ec2a0", "url": "https://www.google.com/"}

def test_list_urls_expired_token(client: TestClient):
    ''' Function tests route with an expired token '''
    expires = datetime.now(timezone.utc) - timedelta(minutes=5)
    token = jwt.encode({"sub": "test1", "exp": expires}, key=SECRET_KEY, algorithm=ALGORITHM)
    response = client.get("/list_urls", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401
    detail = response.json()["detail"]
    assert detail == "ExpiredSignatureError('Signature has expired.')"
