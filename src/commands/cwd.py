import click
import os

@click.command()
def cwd() -> None:
    """
    Выводит текущую рабочую директорию.
    """
    print(os.getcwd())
