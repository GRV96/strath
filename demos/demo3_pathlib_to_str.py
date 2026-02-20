from pathlib import Path
import sys


repo_root = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, repo_root)
from strath import Strath, ensure_path_is_str
sys.path.remove(repo_root)
del repo_root


def _sys_path_contains(dir_path: Strath) -> bool:
	# The type of dir_path is uncertain.
	dir_path: str = ensure_path_is_str(dir_path, False)
	# We know dir_path is a string.

	return dir_path in sys.path


print("sys.path:\n" + "\n".join(sys.path))

print("\nAre these paths in sys.path?")
for dir_path in sys.argv[1:]:
	dir_path = Path(dir_path).resolve()
	print(f"{dir_path}: {_sys_path_contains(dir_path)}")
