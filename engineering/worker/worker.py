from rq import Connection, Worker
from redis import Redis
from config import settings


def run():
    redis: Redis = Redis(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db,
        password=settings.redis.password
    )
    with Connection(connection=redis):
        worker: Worker = Worker(settings.worker.queues)
        worker.work()

