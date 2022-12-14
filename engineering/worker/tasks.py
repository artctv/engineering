"""
    Примеры кода для сохранения

    # Коннект к редис внутри job
    from rq import get_current_job
    from rq.job import Job
    _job: Job = get_current_job()
    print(_job.connection, type(_job.connection))

    # Получение таски, её резльтат и её статус
    job = Job.fetch(job_id)
    print(job.result, job.get_status())

    from rq.job import JobStatus
    Статусы таски
"""

import time


def some_func(timeout):
    time.sleep(timeout)
    return 'kek'


