from lines import count
import pytest
import sys


def test_empty_file(tmp_path, monkeypatch):
    file = tmp_path / "empty.py"
    file.write_text("")

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 0


def test_only_comments(tmp_path, monkeypatch):
    file = tmp_path / "comments.py"
    file.write_text(
        "# Comment\n"
        "    # Indented comment\n"
    )

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 0


def test_only_code(tmp_path, monkeypatch):
    file = tmp_path / "code.py"
    file.write_text(
        "x = 1\n"
        "y = 2\n"
        "print(x + y)\n"
    )

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 3


def test_mixed_file(tmp_path, monkeypatch):
    file = tmp_path / "mixed.py"
    file.write_text(
        "# Comment\n"
        "\n"
        "x = 1\n"
        "print(x)\n"
    )

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 2


def test_inline_comment(tmp_path, monkeypatch):
    file = tmp_path / "inline.py"
    file.write_text(
        'print("Hello")  # greeting\n'
    )

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 1


def test_docstring(tmp_path, monkeypatch):
    file = tmp_path / "doc.py"
    file.write_text(
        '"""\n'
        "Example\n"
        '"""\n'
        'print("Hello")\n'
    )

    monkeypatch.setattr(sys, "argv", ["lines.py", str(file)])
    assert count() == 4