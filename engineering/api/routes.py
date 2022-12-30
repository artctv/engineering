from fastapi import APIRouter, UploadFile, HTTPException, Depends, status
import os
import uuid
from engineering.config import settings


router: APIRouter = APIRouter()

def is_image_file(file:UploadFile):
    if not any([file.filename.endswith('.jpg'), file.filename.endswith('.jpeg')]):
        raise HTTPException(status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Только картинки с расширением .jpg или .jpeg")
    else:
        filename, file_extension = os.path.splitext(file.filename)
        return file_extension

@router.get("/")
def main():
    return {"message": "ok"}

@router.post("/predict")
def create_upload_file(file: UploadFile, file_extension = Depends(is_image_file)):

    id_images = str(uuid.uuid4())

    id_image = id_images + file_extension
    image_path = settings.base_dir / settings.image_dir_name / id_image
    with open(f"{image_path}", "wb") as file_object:
        file_object.write(file.file.read())


    return id_images
