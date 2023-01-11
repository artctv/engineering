import pytest
from pytest_mock import MockFixture
from fastapi.testclient import TestClient
from .utils import generate_fake_image


def test_main(client: TestClient, mocker: MockFixture):

    mocked_etc_release_data = mocker.mock_open()
    builtin_open = "builtins.open"
    mocker.patch(builtin_open, mocked_etc_release_data)

    fake_image = generate_fake_image("jpeg")
    response = client.post("/predict", files={'file': fake_image})
    assert response.status_code == 200
    result = response.json()
    assert "id" in result
    assert "status" in result

    fake_image = generate_fake_image("png")
    response = client.post("/predict", files={'file': fake_image})
    assert response.status_code == 422
