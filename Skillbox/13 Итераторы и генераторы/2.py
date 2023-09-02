import os
from collections.abc import Iterable


def gen_files_path(path: str = None) -> Iterable[str]:
	if path is None:
		result = os.walk(os.path.expanduser("~"))
	else:
		result = os.walk(path)
	for path in result:
		yield path


for elem in gen_files_path():
	print(elem)
