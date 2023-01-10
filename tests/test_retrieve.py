import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from uuid import uuid4

app = FastAPI()
client = TestClient(app)

@app.get("/retrieve")
def root():
    return{"message":"Все хорошо"}


def test_read_main():
    response = client.get("/retrieve")
    assert response.status_code == 200
    assert response.json() == {"message": "Все хорошо"}
    print(response.json())

class TestUuid:
    def test_get_job_by_id(self, connection = None):
        response = requests.get("https://uuid", json=connection)
        assert response.status_code == 201
        assert response.json().get('uuid')
        assert isinstance(response.json().get('uuid'), int)
        print(response.text)



