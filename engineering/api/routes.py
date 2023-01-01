import os
import uuid
from fastapi import APIRouter, UploadFile, HTTPException, Depends, status
from rq import Queue
from rq.job import Job
from config import settings
from .schemas import ResponsePredict
from .dependencies import request_delay, get_queue


router: APIRouter = APIRouter()


@router.get("/")
def main():
    return {"message": "ok"}


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
    _id = str(uuid.uuid4())
    image_name = _id + file_extension
    image_path = settings.base_dir / settings.image_dir_name / image_name
    with open(f"{image_path}", "wb") as file_object:
        file_object.write(file.file.read())

    job: Job = q.enqueue("worker.tasks.call_model", image_path, job_id=_id)

    return {"id": _id, "status": job.get_status()}

