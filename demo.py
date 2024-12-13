import os
from pathlib import Path

from strath import\
	ensure_path_is_pathlib,\
	ensure_path_is_str


def _print_path_and_type(message, some_path):
	print(f"{message}: {some_path} {type(some_path)}")


current_file1 = os.path.abspath(__file__)
current_file2 = Path(__file__).resolve()

print("Demo path")
_print_path_and_type("Path 1", current_file1)
_print_path_and_type("Path 2", current_file2)

print("\nPath types swapped")
current_file1 = ensure_path_is_pathlib(current_file1, False)
current_file2 = ensure_path_is_str(current_file2, False)
_print_path_and_type("Path 1", current_file1)
_print_path_and_type("Path 2", current_file2)
