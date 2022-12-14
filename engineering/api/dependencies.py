from typing import Generator, Callable
from fastapi import Depends
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
