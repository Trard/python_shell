import os
import io

from src.shell import Shell
from src.commands.ls import ls
from pyfakefs.fake_filesystem import FakeFilesystem

def test_ls_exists(fs: FakeFilesystem, mocker):
    fs.create_dir("test_dir")
    fs.create_file("test_file")

    mocker.patch("builtins.input", side_effect=["ls", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(ls)
    shell.launch()

    out_files = captured.getvalue().strip().split()

    contains = "test_file" in out_files and "test_dir" in out_files

    assert contains

def test_ls_not_exists(fs: FakeFilesystem, mocker):
    fs.create_dir("test_dir")
    fs.create_file("test_file")

    mocker.patch("builtins.input", side_effect=["ls", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(ls)
    shell.launch()

    out_files = captured.getvalue().strip().split()

    contains = "test_file123" not in out_files and "test_dir321" not in out_files

    assert contains

def test_ls_l_flag_in_directory(fs: FakeFilesystem, mocker):
    fs.create_dir("mydir")
    fs.create_file("mydir/test_file", contents="hello world\n")

    os.chdir("mydir")

    mocker.patch("builtins.input", side_effect=["ls -l", "exit"])

    captured = io.StringIO()
    mocker.patch("sys.stdout", new=captured)

    shell = Shell()
    shell.register_command(ls)
    shell.launch()

    out = captured.getvalue().strip()
    lines = out.splitlines()

    parts = lines[0].split()
    assert parts[-1] == "test_file"
    assert parts[4] == str(12)
    assert parts[0].startswith("-")
