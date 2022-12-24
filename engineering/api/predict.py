from fastapi import APIRouter, UploadFile, HTTPException
import os
import uuid
import requests
from uuid import UUID

filename, file_extension = os.path.splitext("wine.jpg")
print(filename) #'wine'
print(file_extension) #'.jpg'

f = os.startfile(r'C:\Users\Admin\Desktop\wine.jpg')


def is_image_file(value):
    if value.endswith('.jpg') or value.endswith('.jpeg'):
        print("YES")
    else:
        print("NO")
        raise HTTPException(status_code=400, detail="Bad Request")

is_image_file('wine.txt')

try:
    value.endswith('.jpg') or value.endswith('.jpeg')
    headers = {'Content-Type': 'image/png'}
except	TypeError as e:
    print(e)

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    #return {"filename": file.filename}

    id_image = str(uuid.uuid4())
    file_location = f"//{file.filename}"

    return {"info":f"file '{UploadFile.id_image}' saved at '{file_location}'"}

file_loc = "/engineering/image"

if os.path.exists(file_loc):
    if os.path.isfile(file_loc):
        print('ФАЙЛ')
    elif os.path.isdir(file_loc):
        print('КАТАЛОГ')
else:
    try:
        os.mkdir(file_loc)
    except OSError:
        print("Создать директорию %s не удалось" % file_loc)
    else:
        print("Успешно создана директория %s" % file_loc)