from fastapi.testclient import TestClient
from config import settings
from .utils import generate_fake_image
from fastapi import FastAPI
from .mocks import overrided_fake_queue
from engineering.api.dependencies import get_queue


def test_full(app: FastAPI):
    app.dependency_overrides[get_queue] = overrided_fake_queue
    original_dir = settings.image_dir_name
    settings.image_dir_name = "Fake_images"
    assert settings.image_dir_name
    fake_image = generate_fake_image("jpeg")
    original_task = settings.worker.tasks["call_model"]
    settings.worker.tasks["call_model"] = "tests.mocks.mocked_task"

    test_client = TestClient(app)
    response = test_client.post("/predict", files={'file': fake_image})
    print(response.json())

    response2 = test_client.get("/retrieve/" + response.json()['id'])
    assert response2.status_code == 200
    assert response2.json() == {"message": "Все работает"}

    settings.image_dir_name = original_dir
    settings.worker.tasks["call_model"] = original_task
    del fake_image
