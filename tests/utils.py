from io import BytesIO
from PIL import Image


_image_formats = ["jpeg", "png"]


def generate_fake_image(_format: str):
    if _format not in _image_formats:
        raise ValueError(f"_format must be one this value: {_image_formats}")
    in_memory_file = BytesIO()
    image = Image.new('RGB', size=(10, 5), color=(155, 0, 0))
    image.save(in_memory_file, _format)
    in_memory_file.name = f'test_image.{_format}'
    in_memory_file.seek(0)
    return in_memory_file
