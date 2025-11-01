import click
from pathlib import Path
from src.path_resolver import PathResolver

@click.command()
@click.argument('path', type=str)
def cat(path: str) -> None:
    """
    Выводит содержимое файла по указанному пути.
    """
    resolved_path: Path = PathResolver.resolve(path)
    with open(resolved_path) as f:
        print("".join(f.readlines()))
