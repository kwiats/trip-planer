import io
import mimetypes
from typing import IO, AnyStr, BinaryIO, Tuple


def create_file_name(file_name: str, folder_name: str) -> str:
    return f"{folder_name}/{file_name}"


def set_file_type(file: IO[AnyStr], file_type: str) -> str:
    file_type = file_type.lower() if file_type else mimetypes.guess_type(file.name)[0]
    extensions = ["jpg", "jpeg", "png", "webp"]
    image_mime_types = {
        ext: mimetypes.types_map.get(f".{ext}", "Unknown MIME type")
        for ext in extensions
    }

    return image_mime_types.get(file_type, "image/webp")


def prepare_file(
    file: BinaryIO,
    file_type: str = "webp",
) -> Tuple[io.BytesIO, int, str]:
    _file_content = file.read()
    _file_size = len(_file_content)
    _file_type = set_file_type(file, file_type)
    _file_io = io.BytesIO(_file_content)
    _file_io.seek(0)
    return _file_io, _file_size, _file_type
