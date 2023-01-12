class c_status:
    def get_status(self, *args, **kwargs):
        # print(args, kwargs)
        return 'finished'




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
    pass


def overrided_delay():
    pass

def overrided_get_job_by_id():
    object_job = c_status()
    return object_job


