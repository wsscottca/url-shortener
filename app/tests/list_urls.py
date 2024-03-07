current_db_state = {
  "0":{"short_url": "587ec2a0", "url": "https://www.google.com/"},
  "1":{"short_url": "f4256843", "url": "https://www.bing.com/"},
  "2":{"short_url": "9c983138", "url": "https://www.yahoo.com/"},
  "3":{"short_url": "JHiTvkTu", "url": "https://www.facebook.com/"}
}

def test_list_urls(client):
    response = client.get("/list_urls")
    assert response.status_code == 200
    assert response.json() == current_db_state

def test_list_urls_empty(client):
    response = client.get("/list_urls")
    assert response.status_code == 200
    assert response.json() == {}