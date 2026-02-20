import pytest

import os
from pathlib import Path
import sys


repo_root = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, repo_root)
from strath import\
	Strath,\
	ensure_path_is_pathlib,\
	ensure_path_is_str
sys.path.remove(repo_root)
del repo_root


_ERROR_MSG =\
	"The path must be of type str or pathlib.Path. None is not allowed."
_ERROR_MSG_NONE =\
	"The path must be None or of type str or pathlib.Path."


def test_str_is_strath() -> None:
	some_path = os.path.abspath(__file__)
	assert isinstance(some_path, Strath)


def test_pathlib_is_strath() -> None:
	some_path = Path(__file__).resolve()
	assert isinstance(some_path, Strath)


def test_not_strath() -> None:
	some_path = 3.14159
	assert not isinstance(some_path, Strath)


def test_pathlib_to_pathlib() -> None:
	some_path = Path(__file__).resolve()
	converted_path = ensure_path_is_pathlib(some_path, False)

	assert isinstance(converted_path, Path)
	assert converted_path == some_path
	assert converted_path is some_path


def test_pathlib_to_str() -> None:
	some_path = Path(__file__).resolve()
	converted_path = ensure_path_is_str(some_path, False)

	assert isinstance(converted_path, str)
	assert Path(converted_path) == some_path
	assert converted_path is not some_path


def test_str_to_pathlib() -> None:
	some_path = os.path.abspath(__file__)
	converted_path = ensure_path_is_pathlib(some_path, False)

	assert isinstance(converted_path, Path)
	assert str(converted_path) == some_path
	assert converted_path is not some_path


def test_str_to_str() -> None:
	some_path = os.path.abspath(__file__)
	converted_path = ensure_path_is_str(some_path, False)

	assert isinstance(converted_path, str)
	assert converted_path == some_path
	assert converted_path is some_path


def test_none_allowed_str() -> None:
	some_path = None
	converted_path = ensure_path_is_str(some_path, True)
	assert converted_path is None


def test_none_disallowed_str() -> None:
	some_path = None
	with pytest.raises(TypeError, match=_ERROR_MSG):
		ensure_path_is_str(some_path, False)


def test_none_allowed_pathlib() -> None:
	some_path = None
	converted_path = ensure_path_is_pathlib(some_path, True)
	assert converted_path is None


def test_none_disallowed_pathlib() -> None:
	some_path = None
	with pytest.raises(TypeError, match=_ERROR_MSG):
		ensure_path_is_pathlib(some_path, False)


def test_incorrect_type_none_allowed_str() -> None:
	some_path = 3.14159
	with pytest.raises(TypeError, match=_ERROR_MSG_NONE):
		ensure_path_is_str(some_path, True)


def test_incorrect_type_none_disallowed_str() -> None:
	some_path = 3.14159
	with pytest.raises(TypeError, match=_ERROR_MSG):
		ensure_path_is_str(some_path, False)


def test_incorrect_type_none_allowed_pathlib() -> None:
	some_path = 3.14159
	with pytest.raises(TypeError, match=_ERROR_MSG_NONE):
		ensure_path_is_pathlib(some_path, True)


def test_incorrect_type_none_disallowed_pathlib() -> None:
	some_path = 3.14159
	with pytest.raises(TypeError, match=_ERROR_MSG):
		ensure_path_is_pathlib(some_path, False)
