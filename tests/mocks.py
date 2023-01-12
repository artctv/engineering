from typing import Union


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


