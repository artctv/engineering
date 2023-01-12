from pytest_mock import MockFixture
from rq.job import JobStatus
from fastapi.testclient import TestClient
from .mocks import MockJob
from .utils import generate_fake_image


def test_main(client: TestClient, mocker: MockFixture):
    mocked_etc_release_data = mocker.mock_open()
    mocker.patch("builtins.open", mocked_etc_release_data)
    fake_image = generate_fake_image("jpeg")
    MockJob.status = JobStatus.QUEUED
    response = client.post("/predict", files={'file': fake_image})
    assert response.status_code == 200
    result = response.json()
    assert "id" in result
    assert "status" in result

    fake_image = generate_fake_image("png")
    response = client.post("/predict", files={'file': fake_image})
    assert response.status_code == 422
