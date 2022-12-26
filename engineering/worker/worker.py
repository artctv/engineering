from rq import Connection, Worker
from redis import Redis
from config import settings
import sys
import tensorflow as tf


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


with Connection():
    qs = sys.argv[1:] or ['default']
    w = Worker(qs)
    w.work()
