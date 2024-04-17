from fastapi.testclient import TestClient


current_db_state = {
  "587ec2a0": "https://www.google.com/",
  "f4256843": "https://www.bing.com/",
  "9c983138": "https://www.yahoo.com/",
  "JHiTvkTu": "https://www.facebook.com/"
}

def test_redirect(client: TestClient):
  # Test a valid redirect with an existing URLS, set allow_redirects to false so we can capture for test
  response = client.get("/587ec2a0", allow_redirects=False)
  assert response.status_code == 307
  assert response.headers["location"] == "https://www.google.com/"

def test_bad_redirect(client: TestClient):
  # Test a valid request but with a short_url that does not exist and throws an error
  response = client.get("/12345678")
  assert response.status_code == 422
  assert response.json() == { "detail": "Short url does not exist." }

def test_bad_redirect_long(client: TestClient):
  # Test a valid request but with a short_url that does not exist and throws an error
  response = client.get("/1234567890123456789")

  # Verify the response is the correct specific error and contains pertinent info
  assert response.status_code == 422
  detail = response.json()["detail"][0]
  assert detail["type"] == 'string_too_long'
  assert detail["loc"] == ["path", "short_url"]
  assert detail["msg"] == "String should have at most 8 characters"
  assert detail["input"] == "1234567890123456789"