import os
import shutil
from pytest_mock import MockFixture
from fastapi.testclient import TestClient
from fastapi import FastAPI
from rq.job import JobStatus
from config import settings
from .utils import generate_fake_image
from .mocks import overrided_fake_queue, MockJob
from engineering.api.dependencies import get_queue
from engineering.api.routes import get_job_by_id


def test_full(app: FastAPI, mocker: MockFixture):
    mocker.patch("rq.job.Job.get_status").return_value = JobStatus.QUEUED

    # нагадили
    app.dependency_overrides[get_queue] = overrided_fake_queue
    app.dependency_overrides[get_job_by_id] = get_job_by_id
    original_dir = settings.image_dir_name
    settings.image_dir_name = "fake_images"
    os.makedirs(settings.base_dir / settings.image_dir_name, exist_ok=True)
    assert settings.image_dir_name

    fake_image = generate_fake_image("jpeg")
    original_task = settings.worker.tasks["call_model"]
    settings.worker.tasks["call_model"] = "tests.mocks.mocked_task"

    test_client = TestClient(app)
    response = test_client.post("/predict", files={'file': fake_image})

    MockJob.status = JobStatus.QUEUED
    response = test_client.get("/retrieve/" + response.json()['id'])
    assert response.status_code == 404

    # прибрались
    shutil.rmtree(settings.base_dir / settings.image_dir_name)
    settings.image_dir_name = original_dir
    settings.worker.tasks["call_model"] = original_task
    del fake_image

