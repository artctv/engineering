import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from engineering.config import settings
from engineering.api.dependencies import get_queue, request_delay
from .mocks import overrided_queue, overrided_delay

# scope can be one of this: ["function", "module", "class", "package", "session"]


@pytest.fixture(scope="function")
def app() -> FastAPI:
    from engineering.api.app import app as fastapi_app
    fastapi_app.dependency_overrides[get_queue] = overrided_queue
    fastapi_app.dependency_overrides[request_delay] = overrided_delay
    return fastapi_app


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    test_client = TestClient(app)
    return test_client



