from typing import Generator, Callable
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


def _get_redis() -> Callable:
    get_pool: Callable = _get_pool()

    def inner() -> Generator[Redis, None, None]:
        redis: Redis = Redis(connection_pool=get_pool())
        yield redis
        redis.close()

    return inner


def _get_queue() -> Callable:
    get_pool: Callable = _get_pool()

    def inner() -> Generator[Queue, None, None]:
        queue: Queue = Queue(
            name=settings.worker.queues[0],
            connection=Redis(connection_pool=get_pool())
        )
        yield queue

    return inner


get_redis: Callable = _get_redis()
get_queue: Callable = _get_queue()
