from pathlib import Path
import sys

repo_root = str(Path(__file__).resolve().parents[1])
sys.path.append(repo_root)
from strath import ensure_path_is_pathlib
sys.path.remove(repo_root)
del repo_root


def _print_file_content(file_path: Path | str) -> None:
	# The type of file_path is uncertain.
	file_path: Path = ensure_path_is_pathlib(file_path, False)
	# We know file_path is a pathlib.Path instance.

	file_path = file_path.resolve()

	with file_path.open(mode="r", encoding="UTF-8") as file:
		for line in file:
			print(line.strip())


file_to_read: str = sys.argv[1]

_print_file_content(file_to_read)
