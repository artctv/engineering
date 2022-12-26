import tensorflow as tf
from transformers import ViTFeatureExtractor, ViTForImageClassification
from rq import Worker as _Worker
from rq.local import LocalStack

_model_stack = LocalStack()


def get_model():
    """Get Model."""
    m = _model_stack.top
    try:
        assert m
    except AssertionError:
        raise ('Run outside of worker context')
    return m


class Worker(_Worker):
    """Worker Class."""

    def work(self, burst=False, logging_level='WARN'):
        """Work."""
        _model_stack.push(tf.load_model())
        return super().work(burst, logging_level)


def predict_stuff_job(foo):
    model = get_model()
    result = model.predict(foo)
    return result
