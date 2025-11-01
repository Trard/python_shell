from src.shell import Shell
from src.commands.rm import rm
from src.exceptions.no_permission_exception import NoPermissionException
from pyfakefs.fake_filesystem import FakeFilesystem
import io
import pytest
import os


def test_rm_file_deletes_file(fs: FakeFilesystem, mocker):
    fs.create_file("test_file", contents="delete me\n")

    mocker.patch("builtins.input", side_effect=["rm test_file", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(rm)
    shell.launch()

    assert not os.path.exists("test_file")


def test_rm_dir_r_flag_confirms_and_deletes(fs: FakeFilesystem, mocker):
    fs.create_dir("mydir")
    fs.create_file("mydir/file.txt", contents="hi\n")

    mocker.patch("builtins.input", side_effect=["rm -r mydir", "y", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(rm)
    shell.launch()

    assert not os.path.exists("mydir")


def test_rm_dir_r_flag_decline_does_not_delete(fs: FakeFilesystem, mocker):
    fs.create_dir("keepdir")
    fs.create_file("keepdir/file.txt", contents="stay\n")

    mocker.patch("builtins.input", side_effect=["rm -r keepdir", "n", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(rm)
    shell.launch()

    assert os.path.exists("keepdir")
    assert os.path.exists("keepdir/file.txt")

def test_rm_ancestor_of_cwd_raises_no_permission(fs: FakeFilesystem, mocker):
    fs.create_dir("/parent/sub")

    os.chdir("/parent/sub")

    shell = Shell()
    shell.register_command(rm)

    with pytest.raises(NoPermissionException):
        shell.prompt("rm /parent")


def test_rm_anchor_root_raises_no_permission(fs: FakeFilesystem, mocker):
    shell = Shell()
    shell.register_command(rm)


    with pytest.raises(NoPermissionException):
        shell.prompt("rm /")
