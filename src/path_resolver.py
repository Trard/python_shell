from pathlib import Path
from os.path import expanduser


class PathResolver:
    """
    Рерзолвит путь из относительного или абслютного в специальный класс Path.
    Заменяет ~ на директорию пользователя.
    """
    @staticmethod
    def resolve(path: str) -> Path:
        return Path(expanduser(path)).resolve()
