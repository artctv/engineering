from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import os
import requests

# ссылка на папку
path = 'images/sample.jpg'

# Открыть, Закрыть картинку по пути
with Image.open(path) as image:

    # расчет модели
    feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
    model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    #os.remove('/images/sample.jpg') #удалить картинку из папки


# Предсказание
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])


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

# import time
#
#
# def some_func(timeout):
#     time.sleep(timeout)
#     return 'kek'
