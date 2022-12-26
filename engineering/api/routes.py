from pydantic import BaseModel
from fastapi import APIRouter
from uuid import UUID
from rq.job import Job, JobStatus
from rq import Queue
from rq.exceptions import NoSuchJobError
from .dependencies import get_queue
from fastapi import Depends

router: APIRouter = APIRouter()

#Получение модели
@router.get("/{uuid}")
def main(uuid: UUID):
    return {"message": "ok"}


class Response(BaseModel):
    message: str






#Обработка статусов
@router.get("/retrive/{uuid}", response_model=Response)
def retrive(uuid:UUID, q:Queue = Depends(get_queue())):
    try:
        job: Job = Job.fetch(str(uuid), connection = q.connection)
    except NoSuchJobError:
        return {"message": "Ошибка: нет такой задачи"}
    else:
        status = job.get_status()


    if status == JobStatus.Canceled:
        return("Ваш запрос был отменен.Повторите попытку позже")
    elif status == JobStatus.Queued:
        return("Ваш запрос в очереди,ожидайте")
    elif status == JobStatus.Finished:
        return("Ваш запрос обработан")
    elif status == JobStatus.Started:
        return ("Ваш запрос в обработке")
    elif status == JobStatus.Deferred:
        return ("Ваш запрос отложен, повторите попытку позже")

        
