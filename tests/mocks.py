class c_status:
    def get_status(self, *args, **kwargs):
        # print(args, kwargs)
        return 'finished'






def overrided_queue():
    pass


def overrided_delay():
    pass
def overrided_get_job_by_id():
    object_job = c_status()
    return object_job


