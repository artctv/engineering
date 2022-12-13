from typing import Generator, Callable
from redis import ConnectionPool, Redis
from config import settings


def _get_redis() -> Callable:
    pool: ConnectionPool = ConnectionPool(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db,
        password=settings.redis.password
    )

    def inner() -> Generator[Redis, None, None]:
        redis: Redis = Redis(connection_pool=pool)
        yield redis
        redis.close()

    return inner


get_redis = _get_redis()
