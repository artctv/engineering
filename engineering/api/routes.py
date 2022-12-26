from fastapi import APIRouter, UploadFile, HTTPException, Depends, status
import os
import uuid
from engineering.config import Settings

router: APIRouter = APIRouter()

def is_image_file(file:UploadFile):
    if not any([file.filename.endswith('.jpg'), file.filename.endswith('.jpeg')]):
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Только картинки с расширением .jpg или .jpeg")

@router.get("/")
def main():
    return {"message": "ok"}

@router.post("/predict", dependencies=[Depends(is_image_file)])
def create_upload_file(file: UploadFile):
    return file.filename

id_image = str(uuid.uuid4())

file_loc = "/engineering/images"

if os.path.exists(file_loc):
    if os.path.isfile(file_loc):
        print('ФАЙЛ')
    elif os.path.isdir(file_loc):
        print('КАТАЛОГ')
else:
    try:
        os.makedirs(file_loc, exists_ok = True)
    except OSError:
        print("Создать директорию %s не удалось" % file_loc)
    else:
        print("Успешно создана директория %s" % file_loc)

    return {"info": f"file '{UploadFile.id_image}' saved at '{file_loc}'"}