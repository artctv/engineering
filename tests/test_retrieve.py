from uuid import uuid4
from rq.job import JobStatus
from .mocks import MockJob, simple_fake_reids


def test_retrive_with_result(client):
    uuid = str(uuid4())
    simple_fake_reids[uuid] = "some result"
    MockJob.status = JobStatus.FINISHED
    response = client.get("/retrieve/{}".format(uuid))
    assert response.status_code == 200
    result = response.json()
    assert "status" in result
    assert "result" in result
    assert result["result"] == "some result"


def test_retrive_no_result(client):
    uuid = str(uuid4())
    MockJob.status = JobStatus.QUEUED
    response = client.get("/retrieve/{}".format(uuid))
    assert response.status_code == 201
    result = response.json()
    assert "status" in result
    assert "result" in result
    assert result["result"] is None



  




