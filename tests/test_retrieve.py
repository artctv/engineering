from fastapi import FastAPI
from fastapi.testclient import TestClient

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

