from pathlib import Path


_ERROR_MSG =\
	"The path must be of type str or pathlib.Path."
_ERROR_MSG_NONE =\
	"The path must be None or of type str or pathlib.Path."


def _raise_type_error(allow_none):
	message = _ERROR_MSG if allow_none else _ERROR_MSG_NONE
	raise TypeError(message)


def ensure_path_is_pathlib(some_path, allow_none):
	"""
	If argument some_path is an str instance, this function converts it to a
	pathlib.Path instance, which it returns. If some_path is a pathlib.Path
	instance, this function returns its reference. Otherwise, a TypeError is
	raised.

	If argument some_path is None and argument allow_none is True, this
	function returns None. However, if allow_none is False, a TypeError is
	raised.

	Parameters:
		some_path (str or pathlib.Path): the path to a file or directory.
		allow_none (bool): determines whether some_path can be None.

	Returns:
		pathlib.Path: the path to a file or directory, possibly None.

	Raises:
		TypeError: if some_path is of a wrong type.
	"""
	if isinstance(some_path, Path) or allow_none and some_path is None:
		return some_path
	elif isinstance(some_path, str):
		return Path(some_path)
	else:
		_raise_type_error(allow_none)


def ensure_path_is_str(some_path, allow_none):
	"""
	If argument some_path is a pathlib.Path instance, this function converts
	it to a string (type str), which it returns. If some_path is an str
	instance, this function returns its reference. Otherwise, a TypeError is
	raised.

	If argument some_path is None and argument allow_none is True, this
	function returns None. However, if allow_none is False, a TypeError is
	raised.

	Parameters:
		some_path (str or pathlib.Path): the path to a file or directory.
		allow_none (bool): determines whether some_path can be None.

	Returns:
		str: the path to a file or directory, possibly None.

	Raises:
		TypeError: if some_path is of a wrong type.
	"""
	if isinstance(some_path, str) or allow_none and some_path is None:
		return some_path
	elif isinstance(some_path, Path):
		return str(some_path)
	else:
		_raise_type_error(allow_none)
