from fakeredis import FakeStrictRedis
from rq import Queue
import time


def overrided_queue():
    pass


def overrided_delay():
    pass


def mocked_task(image_path, *args, **kwargs):
    print(image_path)



def overrided_fake_queue():
    queue = Queue(is_async=False, connection=FakeStrictRedis())
    return queue
