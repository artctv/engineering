class Cl_enqueue:
    def get_status(self, *args, **kwargs):
        return 'queued'
    def enqueue(self,*args, **kwargs):
        return self


def overrided_queue():
    object_something = Cl_enqueue()
    yield object_something


def overrided_delay():
    pass

