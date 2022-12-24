from fastapi import APIRouter
from uuid import UUID
from engineering.api.dependencies import get_queue
from rq.job import JobStatus
from rq import Queue
from rq.exceptions import NoSuchJobError
from .dependencies import get_queue
from fastapi import Depends

router: APIRouter = APIRouter()

#Получение модели
@router.get("/{uuid}")
def main(uuid: UUID):
    return {"message": "ok"}








#Обработка статусов
def main(q: Queue = Depends(get_queue)):
    print(JobStatus.Failed)
    status = "canceled"
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

        
