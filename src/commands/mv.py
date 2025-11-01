import click
from src.path_resolver import PathResolver
import shutil

@click.command()
@click.argument('path1', type=str)
@click.argument('path2', type=str)
def mv(path1: str, path2: str) -> None:
    """
    Перемещает (переименовывает) файл или директорию из path1 в path2.
    """
    src = PathResolver.resolve(path1)
    dst = PathResolver.resolve(path2)

    shutil.move(src, dst)
