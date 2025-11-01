from src.shell import Shell
from src.commands.cat import cat
from pyfakefs.fake_filesystem import FakeFilesystem
import io

def test_cat_exists(fs: FakeFilesystem, mocker):
    fs.create_file("test_file", contents="hello world\nsecond line\n")

    mocker.patch("builtins.input", side_effect=["cat test_file", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(cat)
    shell.launch()

    out = captured.getvalue().strip()

    assert "hello world" in out
    assert "second line" in out

def test_cat_not_exists(fs: FakeFilesystem, mocker):
    fs.create_file("test_file", contents="hello world\n")

    mocker.patch("builtins.input", side_effect=["cat test_file123", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(cat)
    shell.launch()

    out = captured.getvalue().strip()

    assert "No such file" in out
