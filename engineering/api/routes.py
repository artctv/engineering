import os
import uuid
from fastapi import APIRouter, UploadFile, HTTPException, Depends, status
from config import settings
from .schemas import ResponsePredict


router: APIRouter = APIRouter()


@router.get("/")
def main():
    return {"message": "ok"}


def check_get_ext(file: UploadFile):
    if not any([file.filename.endswith('.jpg'), file.filename.endswith('.jpeg')]):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Только картинки с расширением .jpg или .jpeg"
        )
    filename, file_extension = os.path.splitext(file.filename)
    return file_extension


@router.post("/predict", response_model=ResponsePredict)
def create_upload_file(file: UploadFile, file_extension=Depends(check_get_ext)):
    _id = str(uuid.uuid4())
    image_name = _id + file_extension
    image_path = settings.base_dir / settings.image_dir_name / image_name
    with open(f"{image_path}", "wb") as file_object:
        file_object.write(file.file.read())

    return {"id": _id, "status": "queued"}
