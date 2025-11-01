import click
import os
import stat
import pwd
import grp
import datetime
from src.path_resolver import PathResolver

def mtime_str(ts: float) -> str:
    """
    Форматирует время последней модификации в виде 'Месяц День ЧЧ:ММ'.
    """
    dt = datetime.datetime.fromtimestamp(ts)
    return dt.strftime("%b %d %H:%M")


@click.command()
@click.argument('path', default=".")
@click.option('-l', is_flag=True)
def ls(path, l) -> None: # noqa
    """
    Выводит список файлов в указанной директории.

    Аргументы:
        path (str): Путь к директории (по умолчанию текущая директория).
        l (bool): Если установлен, выводит подробную информацию о файлах.
    """
    resolved_path = PathResolver.resolve(path)
    files = os.listdir(resolved_path)

    if l:
        for file in files:
            full_path = resolved_path / file
            stats = os.lstat(full_path)

            mode = stat.filemode(stats.st_mode)
            nlink = stats.st_nlink
            owner = pwd.getpwuid(stats.st_uid).pw_name
            group = grp.getgrgid(stats.st_gid).gr_name
            size = stats.st_size
            mtime = mtime_str(stats.st_mtime)

            print(f"{mode} {nlink} {owner} {group} {size} {mtime} {file}")
    else:
        print(" ".join(files))
