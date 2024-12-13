import os
from pathlib import Path

from strath import\
	ensure_path_is_pathlib,\
	ensure_path_is_str


_TITLE_PATH1 = "Path 1"
_TITLE_PATH2 = "Path 2"


def _print_path_and_type(message, some_path):
	print(f"{message}: {some_path} {type(some_path)}")


def _test_none_path(message, fnc, is_none_allowed):
	print(message)
	try:
		none_path = fnc(None, is_none_allowed)
		print(f"Returned value: {none_path}")
	except TypeError:
		print("TypeError raised")


current_file1 = os.path.abspath(__file__)
current_file2 = Path(__file__).resolve()

print("Demo path")
_print_path_and_type(_TITLE_PATH1, current_file1)
_print_path_and_type(_TITLE_PATH2, current_file2)

print("\nPath types swapped")
current_file1 = ensure_path_is_pathlib(current_file1, False)
current_file2 = ensure_path_is_str(current_file2, False)
_print_path_and_type(_TITLE_PATH1, current_file1)
_print_path_and_type(_TITLE_PATH2, current_file2)

_test_none_path("\nTest with None allowed, str -> pathlib", ensure_path_is_pathlib, True)
_test_none_path("\nTest with None disallowed, str -> pathlib", ensure_path_is_pathlib, False)
_test_none_path("\nTest with None allowed, pathlib -> str", ensure_path_is_str, True)
_test_none_path("\nTest with None disallowed, pathlib -> str", ensure_path_is_str, False)