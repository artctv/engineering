from typing import Any
from PIL import Image
from rq import get_current_job
from rq.job import Job
from redis import Redis


def _calculate_model(path: str, feature_extractor: Any, model: Any) -> str:
    with Image.open(path) as image:
        inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]


def call_model(path: str, feature_extractor: Any, model: Any):
    job: Job = get_current_job()
    redis: Redis = job.connection
    result = _calculate_model(path, feature_extractor, model)
    redis.set(str(job.id), result)
    return result


