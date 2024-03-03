current_db_state = {
  "587ec2a0": "https://www.google.com/",
  "f4256843": "https://www.bing.com/",
  "9c983138": "https://www.yahoo.com/",
  "JHiTvkTu": "https://www.facebook.com/"
}

def test_redirect(client):
    response = client.get("/587ec2a0", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "https://www.google.com/"

def test_bad_redirect(client):
    response = client.get("/12345678")
    assert response.status_code == 422
    assert response.json() == { "detail": "Short url does not exist." }