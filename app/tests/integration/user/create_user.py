from fastapi.testclient import TestClient
from db.services.get_user import get_user
from db.models.user import User


def test_signup(client: TestClient):
    # Test our route when given the proper information
    response = client.post('/signup', data={"username": "test2", "password": "test2"},
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
    response = client.post('/signup', data={"username": "test1", "password": "test2"},
                        headers={"content-type": "application/x-www-form-urlencoded"})

    # Ensure the message and status code are correct and relevant
    assert response.status_code == 422
    assert response.json() == { "detail": "Username already exists, please select a different username." }