import click
import shlex
import os
from datetime import datetime
from src.exceptions.no_such_command_exception import NoSuchCommandException
from src.constants import LOG_FILE
from src.constants import SUCCESS
from src.constants import ERROR
from src.constants import DATEFORMAT

class Shell:
    """
    Класс оболочки для регистрации и выполнения команд.
    Логирует команды и их результаты в файл.
    """

    def __init__(self):
        self.commands = {}

    def prompt(self, command: str) -> str:
        """
        Выполняет команду, переданную в виде строки.

        Выкидывает `NoSuchCommandException`, если команда не зарегистрирована или отсутствует.
        """
        command_and_args = shlex.split(command)

        if (len(command_and_args) == 0):
            raise NoSuchCommandException()

        [command, *args] = command_and_args

        click_command = self.commands.get(command)

        if click_command is None:
            raise NoSuchCommandException()

        return click_command(args, standalone_mode=False)

    def register_command(self, command: click.Command):
        """
        Регистрирует команду в оболочке.

        Выкидывает `NoSuchCommandException`, если у команды нет имени.
        """
        if (command.name is None):
            raise NoSuchCommandException()

        self.commands[command.name] = command

    def launch(self):
        """
        Запускает интерактивную оболочку с циклом ввода команд и логированием.
        """
        log_file = open(LOG_FILE, 'w+')

        while True:
            cwd = os.getcwd()
            command = input(f"{cwd} > ")

            if (command == "exit"):
                log_file.flush()
                return

            now = datetime.now()
            date = now.strftime(DATEFORMAT)
            log_file.write(f"{date} {command}\n")

            try:
                self.prompt(command)
                log_file.write(f"{SUCCESS}\n")
            except Exception as exception:
                log_file.write(f"{ERROR}: {exception}\n")
                print(exception)

            log_file.flush()
