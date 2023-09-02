from collections.abc import Iterable
import os


def get_generation_with_errors(path_to_log: str) -> Iterable[str]:
	if not os.path.isfile(path_to_log):
		raise TypeError
	with open(path_to_log, "r", encoding="utf-8") as file:
		for rows in file.readlines():
			if "ERROR" in rows:
				yield rows.rstrip()


def save_error(str_with_error: str) -> None:
	with open("Только ошибки.log", "a", encoding="utf-8") as file:
		file.write(str_with_error + "\n")


for elem in get_generation_with_errors("example.log"):
	save_error(elem)
