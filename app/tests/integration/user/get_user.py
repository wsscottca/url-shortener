from fastapi.testclient import TestClient
from tests.integration.auth.token import test_token


def test_get_user(client: TestClient):
    # Test getting our user when we have a valid token
    response = client.get("/users/me", headers={"Authorization": f"Bearer {test_token(client).access_token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "test"