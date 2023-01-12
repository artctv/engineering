from typing import Union
from fakeredis import FakeStrictRedis
from rq import Queue


simple_fake_reids = {}


class MockJob:

    status: Union[str, None]

    def __init__(self):
        if not hasattr(self, "status"):
            self.status = None

    def get_status(self, *args, **kwargs):  # noqa
        return self.status


class MockQueue:

    def enqueue(self, *args, **kwargs):  # noqa
        return MockJob()


def overrided_queue():
    return MockQueue()


def overrided_redis():
    return simple_fake_reids


def overrided_delay():
    pass


def overrided_get_job_by_id():
    return MockJob()


def overrided_fake_queue():
    queue = Queue(is_async=False, connection=FakeStrictRedis())
    return queue


def mocked_task(image_path, *args, **kwargs):
    print(image_path)






