from typing import Union


class MockJob:

    status: Union[str, None]

    def __init__(self):
        self.status = None

    def get_status(self, *args, **kwargs):  # noqa
        return self.status


class MockQueue:

    def enqueue(self, *args, **kwargs):  # noqa
        return MockJob()


def overrided_queue():
    return MockQueue()


def overrided_delay():
    pass

