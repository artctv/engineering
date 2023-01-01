from typing import Generator, Callable
from fastapi import Depends, Request, HTTPException, status
from redis import ConnectionPool, Redis
from rq import Queue
from config import settings


def _get_pool() -> Callable:
    pool: ConnectionPool = ConnectionPool(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db,
        password=settings.redis.password
    )

    def inner() -> ConnectionPool:
        return pool

    return inner


get_pool: Callable = _get_pool()


def get_redis(pool: ConnectionPool = Depends(get_pool)) -> Generator[Redis, None, None]:
    redis: Redis = Redis(connection_pool=pool)
    yield redis
    redis.close()


def get_queue(redis: Redis = Depends(get_redis)) -> Generator[Queue, None, None]:
    queue: Queue = Queue(name=settings.worker.queues[0], connection=redis)
    yield queue


def request_delay(request: Request, redis: Redis = Depends(get_redis)):
    ip = request.client.host
    if redis.exists(ip):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Слишком частое обращение"
        )
    redis.setex(ip, settings.time_delay, ip)