import click
import os
import shutil
from pathlib import Path
from src.exceptions.no_permission_exception import NoPermissionException

@click.command()
@click.argument('path', type=str)
@click.option('-r', is_flag=True)
def rm(path: str, r: bool) -> None:
    """
    Удаляет файл или директорию по указанному пути.
    Не даёт удалить родительский каталог и корневой.

    Аргументы:
        path: Путь к файлу или директории для удаления.
        r: Если установлен, удаляет директорию рекурсивно.
    """
    if (os.getcwd().startswith(os.path.abspath(path)+os.sep) or path == Path(path).anchor):
        raise NoPermissionException()

    if r:
        prompt = input("Are you sure (y/n) ")

        if (prompt == "y"):
            shutil.rmtree(path)
    else:
        os.remove(path)
