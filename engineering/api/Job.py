from enum import Enum


class JobStatus(str, Enum):
    Queued = 'queued'
    Finished = 'finished'
    Failed = 'failed'
    Started = 'started'
    Deferred = 'deferred'
    Scheduled = 'scheduled'
    Stopped = 'stopped'
    Canceled = 'canceled'
