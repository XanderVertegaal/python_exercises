__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from os import mkdir, remove, listdir
from os.path import abspath
import zipfile


def clean_cache() -> None:
    try:
        mkdir("./files/cache")
        print("File created.")
    except FileExistsError:
        print("Emptying cache...")
        for file in listdir("./files/cache/"):
            remove(f"./files/cache/{file}")


def cache_zip(path: str, cache_dir: str) -> None:
    with zipfile.ZipFile(file=path, mode="r") as f:
        f.extractall(cache_dir)


def cached_files() -> list[str]:
    file_list = []
    for file in listdir("./files/cache/"):
        file_list.append(abspath(f"./files/cache/{file}"))
    return file_list


def find_password(list_of_paths: list[str]) -> str:
    for path in list_of_paths:
        with open(file=path, mode="r") as f:
            for line in f:
                if "password" in line:
                    return line.replace("password: ", "")


print(find_password(cached_files()))
clean_cache()