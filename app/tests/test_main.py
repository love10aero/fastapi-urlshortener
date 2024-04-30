from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/shorturl/abc123")
    assert response.status_code == 404

def test_create_shorturl():
    response = client.post("/shorturl/", json={"short_code": "abc123", "url": "https://example.com"})
    assert response.status_code == 201
    print(response.json())
    assert response.json() == {"url": "https://example.com/", "short_code": "abc123"}

def test_update_shorturl():
    client.post("/shorturl/", json={"short_code": "abc123", "url": "https://example.com"})
    response = client.put("/shorturl/abc123", json={"url": "https://example.org"})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"url": "https://example.org/"}

def test_delete_shorturl():
    client.post("/shorturl/", json={"short_code": "abc123", "url": "https://example.com"})
    response = client.delete("/shorturl/abc123")
    assert response.status_code == 204
    response = client.get("/shorturl/abc123")
    assert response.status_code == 404
