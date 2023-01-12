import requests
from fastapi import FastAPI
from fastapi.testclient import TestClient
from uuid import uuid4

from pytest_mock import MockFixture




def test_read_main(client):
    uuid = str(uuid4())
    response = client.get("/retrieve/{}".format(uuid))
    assert response.status_code == 200
    result = response.json()
    assert "status" in result
    assert "result" in result



  




