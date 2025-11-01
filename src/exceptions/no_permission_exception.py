from src.exceptions.shell_exception import ShellException

class NoPermissionException(ShellException):
    """
    Исключение, выбрасываемое при отсутствии прав доступа.
    """
    def __str__(self) -> str:
        return "No permission"
