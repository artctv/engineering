from typing import Generator
from redis import ConnectionPool, Redis
from config import settings


_pool: ConnectionPool = ConnectionPool(host=settings.redis.host, port=settings.redis.port, db=settings.redis.db)


def get_redis() -> Generator[Redis, None, None]:
    redis = Redis(connection_pool=_pool)
    try:
        yield redis
    finally:
        redis.close()
