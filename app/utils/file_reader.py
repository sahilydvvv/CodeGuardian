import os

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    return code

def get_file_size(file_path:str)-> int:
    return os.path.getsize(file_path)

MAX_FILE_SIZE = 100 * 1024  # 100 KB


def is_file_too_large(file_path: str) -> bool:
    size = get_file_size(file_path)

    return size > MAX_FILE_SIZE