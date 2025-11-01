from src.exceptions.shell_exception import ShellException

class NoSuchCommandException(ShellException):
    """
    Исключение, выбрасываемое при попытке вызова несуществующей команды.
    """
    def __str__(self) -> str:
        return "No such command"
