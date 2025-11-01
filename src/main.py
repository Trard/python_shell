from src.shell import Shell
from src.commands.ls import ls
from src.commands.cd import cd
from src.commands.cat import cat
from src.commands.mv import mv
from src.commands.rm import rm
from src.commands.cwd import cwd
import signal

def handler(signum, frame):
    pass

signal.signal(signal.SIGINT, handler)

def main():
    """
    Регистрирует команды и запускает оболочку
    """
    shell = Shell()

    shell.register_command(ls)
    shell.register_command(cd)
    shell.register_command(cat)
    shell.register_command(mv)
    shell.register_command(rm)
    shell.register_command(cwd)

    shell.launch()

if __name__ == "__main__":
    main()
