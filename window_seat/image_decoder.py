import io
from datetime import datetime

from PIL import Image

def _extract_meta(img) -> datetime:
    metadata = img.getexif()
    created = metadata[306]
    dt = datetime.strptime(created, '%Y:%m:%d %H:%M:%S')
    return dt


def extract_created_from_bytes(bytes_img):
    img = Image.open(io.BytesIO(bytes_img))
    return _extract_meta(img)


def extract_created_from_filepath(file_location: str):
    img = Image.open(file_location)
    return _extract_meta(img)

