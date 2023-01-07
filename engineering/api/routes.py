import os
from uuid import uuid4
from fastapi import APIRouter, UploadFile, Response, HTTPException, Depends, status
from pydantic import UUID4
from redis import Redis
from rq.job import Job, JobStatus
from rq import Queue
from rq.exceptions import NoSuchJobError
from config import settings
from .dependencies import request_delay, get_queue, get_redis
from .schemas import ResponsePredict, ResponseRetrieve


router: APIRouter = APIRouter()


def check_get_ext(file: UploadFile):
    if not any([file.filename.endswith('.jpg'), file.filename.endswith('.jpeg')]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Только картинки с расширением .jpg или .jpeg"
        )
    filename, file_extension = os.path.splitext(file.filename)
    return file_extension


@router.post("/predict", response_model=ResponsePredict, dependencies=[Depends(request_delay)])
def create_upload_file(
    file: UploadFile,
    file_extension: str = Depends(check_get_ext),
    q: Queue = Depends(get_queue)
):
    _id = str(uuid4())
    image_name = _id + file_extension
    image_path = settings.base_dir / settings.image_dir_name / image_name
    with open(f"{image_path}", "wb") as file_object:
        file_object.write(file.file.read())

    job: Job = q.enqueue("worker.tasks.call_model", image_path, job_id=_id)

    return {"id": _id, "status": job.get_status()}


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
def retrieve(
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
