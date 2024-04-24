''' Module contains test for root route '''

from fastapi.testclient import TestClient


def test_get_root(client: TestClient):
    ''' Function tests that we get the correct response from the root route '''
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "URL Shortener API"}
