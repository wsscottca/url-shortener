def test_get_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "URL Shortener API"}