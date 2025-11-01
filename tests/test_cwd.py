from src.shell import Shell
from src.commands.cd import cd
from src.commands.cwd import cwd
from pyfakefs.fake_filesystem import FakeFilesystem
import io

def test_cd_cwd(fs: FakeFilesystem, mocker):
    fs.create_dir("test_dir")

    mocker.patch("builtins.input", side_effect=["cd test_dir", "cwd", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(cwd)
    shell.register_command(cd)
    shell.launch()

    path = captured.getvalue().strip()

    assert path == "/test_dir"
