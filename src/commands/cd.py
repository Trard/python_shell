import click
import os
from src.path_resolver import PathResolver


@click.command()
@click.argument('path', default='.', type=str)
def cd(path: str) -> None:
    """
    Изменяет текущую рабочую директорию на указанную.

    Если путь не указан, меняет директорию на домашнюю (текущую директорию по умолчанию — ".").
    """
    resolved_path = PathResolver.resolve(path)
    os.chdir(resolved_path)
