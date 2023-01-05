from typing import Any
from rq import Connection, Worker
from redis import Redis
from transformers import ViTFeatureExtractor, ViTForImageClassification
from rq_win import WindowsWorker
import platform
from config import settings


class BaseWorker:
    _feature_extractor: Any
    _model: Any

    def __init__(self, *args, **kwargs):
        self._feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
        self._model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
        super().__init__(*args, **kwargs)


class ExtendedWorker(BaseWorker, Worker):
    def execute_job(self, job, queue):
        job.args = (job.args[0], self._feature_extractor, self._model)
        return self.perform_job(job, queue)

    def work(self, *args, **kwargs):
        return super().work(*args, **kwargs)


class ExtendedWindowWorker(BaseWorker, WindowsWorker):
    def execute_job(self, job, queue):
        job.args = (job.args[0], self._feature_extractor, self._model)
        return self.perform_job(job, queue)

    def work(self, *args, **kwargs):
        return super().work(*args, **kwargs)


def run():
    redis: Redis = Redis(
        host=settings.redis.host,
        port=settings.redis.port,
        db=settings.redis.db,
        password=settings.redis.password
    )
    if platform.system() == "Windows":
        worker: Worker = ExtendedWindowWorker(settings.worker.queues)
    else:
        worker: Worker = ExtendedWorker(settings.worker.queues)

    with Connection(connection=redis):
        worker.work()

