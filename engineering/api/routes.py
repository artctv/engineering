from fastapi import APIRouter
from uuid import UUID
from rq.job import JobStatus
from rq import Queue
from .dependencies import get_queue
from fastapi import Depends

router: APIRouter = APIRouter()

#Получение модели
@router.get("/{uuid}")
def main(uuid: UUID):
    return {"message": "ok"}








#Обработка статусов
@router.get("/retrive/{uuid}", response_model=Response)
def retrive(uuid:UUID, q:Queue = Depends(get_queue())):
def main(q: Queue = Depends(get_queue)):
    print(JobStatus.Failed)
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

        
