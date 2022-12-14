from fastapi import APIRouter, Depends
from redis import Redis
from rq import Queue
from config import settings
from .dependencies import get_redis, get_queue


router: APIRouter = APIRouter()


@router.get("/predict")
def main(q: Queue = Depends(get_queue)):
    q.enqueue(settings.worker.tasks["some_func"], 30, job_id="my_id")
    # сохарнить картинку в файл в папку
    return {"message": "ok"}


@router.get("/retrive/{job_id}")
def main(redis: Redis = Depends(get_redis)):
    redis.setex("key", 10, "value")
    return {"message": "ok"}