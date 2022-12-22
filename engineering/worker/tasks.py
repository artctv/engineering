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
    os.remove('/images/sample.jpg') #удалить картинку из папки

# Предсказание
predicted_class_idx = logits.argmax(-1).item()
func_result = model.config.id2label[predicted_class_idx]


#Результат
def result():
    print("Predicted class:", func_result)



