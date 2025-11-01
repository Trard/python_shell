from src.shell import Shell
from src.commands.mv import mv
from pyfakefs.fake_filesystem import FakeFilesystem
import io
import os

def test_mv_moves_file(fs: FakeFilesystem, mocker):
    fs.create_file("test_file", contents="move me\n")

    mocker.patch("builtins.input", side_effect=["mv test_file moved_file", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(mv)
    shell.launch()

    assert os.path.exists("moved_file")
    assert not os.path.exists("test_file")

    with open("moved_file", "r") as f:
        assert f.read() == "move me\n"

def test_mv_src_not_exists(fs: FakeFilesystem, mocker):
    fs.create_file("existing_file", contents="i stay\n")

    mocker.patch("builtins.input", side_effect=["mv nofile moved_file", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(mv)
    shell.launch()

    assert not os.path.exists("moved_file")
    assert os.path.exists("existing_file")
