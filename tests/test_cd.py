from src.shell import Shell
from src.commands.cd import cd
from src.commands.cwd import cwd
from pyfakefs.fake_filesystem import FakeFilesystem
import io
import os

def test_cd_cwd(fs: FakeFilesystem, mocker):
    fs.create_dir("test_dir")

    mocker.patch("builtins.input", side_effect=["cd test_dir", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(cwd)
    shell.register_command(cd)
    shell.launch()

    assert os.getcwd() == "/test_dir"
