from fastapi.testclient import TestClient
from engineering.api.app import app

client = TestClient(app)

def test_retrieve(app:TestClient,retrieve):
    response = app.get("/retrieve/{uuid}")
    print(response.json())
    assert response.status_code == 201
    assert response.json() == {"massage": "Hello world"}