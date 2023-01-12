import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from engineering.config import settings
from engineering.api.dependencies import get_queue, request_delay
from .mocks import overrided_queue, overrided_delay, mocked_task
from engineering.api.routes import get_job_by_id
from engineering.api.dependencies import get_queue, request_delay, get_redis
from .mocks import overrided_queue, overrided_delay, overrided_redis, overrided_get_job_by_id


# scope can be one of this: ["function", "module", "class", "package", "session"]


@pytest.fixture(scope="function")
def app() -> FastAPI:
    from engineering.api.app import app as fastapi_app
    fastapi_app.dependency_overrides[get_queue] = overrided_queue
    fastapi_app.dependency_overrides[request_delay] = overrided_delay
    fastapi_app.dependency_overrides[get_job_by_id] = overrided_get_job_by_id
    fastapi_app.dependency_overrides[get_redis] = overrided_redis
    return fastapi_app


@pytest.fixture(scope="function")
def client(app: FastAPI) -> TestClient:
    return TestClient(app)




