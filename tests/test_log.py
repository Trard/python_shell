from src.shell import Shell
from src.commands.ls import ls
from src.constants import LOG_FILE, SUCCESS, ERROR
from pyfakefs.fake_filesystem import FakeFilesystem
import io
import os


def test_shell_logs_successful_command(fs: FakeFilesystem, mocker):
    fs.create_file("file_for_ls", contents="hello\n")

    mocker.patch("builtins.input", side_effect=["ls", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(ls)
    shell.launch()

    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, "r") as f:
        log = f.read()

    assert "ls" in log
    assert SUCCESS in log


def test_shell_logs_unknown_command_as_error(fs: FakeFilesystem, mocker):
    mocker.patch("builtins.input", side_effect=["this_command_does_not_exist", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.launch()

    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, "r") as f:
        log = f.read()

    assert "this_command_does_not_exist" in log
    assert ERROR in log
