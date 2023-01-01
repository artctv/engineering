from fastapi import APIRouter, Depends, Response, HTTPException, status
from pydantic import UUID4
from redis import Redis
from rq.job import Job, JobStatus
from rq import Queue
from rq.exceptions import NoSuchJobError
from .dependencies import get_queue, get_redis
from .schemas import ResponseRetrieve


router: APIRouter = APIRouter()


def get_job_by_id(uuid: UUID4, q: Queue = Depends(get_queue)):
    try:
        job: Job = Job.fetch(str(uuid), connection=q.connection)
    except NoSuchJobError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Такой задачи нет"
        )
    else:
        return job


@router.get("/retrieve/{uuid}", response_model=ResponseRetrieve)
def retrive(
    uuid: UUID4,
    response: Response,
    job: Job = Depends(get_job_by_id),
    redis: Redis = Depends(get_redis)
):
    _status: JobStatus = job.get_status()

    if _status == JobStatus.FINISHED:
        result = redis.get(str(uuid))
        return {"status": _status, "result": result}
    else:
        response.status_code = status.HTTP_201_CREATED
        return {"status": _status}
