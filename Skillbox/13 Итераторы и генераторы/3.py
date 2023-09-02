from collections.abc import Iterable
import os


def count_rows(folder_name: str) -> Iterable[int]:
	"""
	Функция для получения количества строк кода в каждом отдельном файле выбранной директории.
	:param folder_name: путь папки, по которой будет происходить процедура.
	:return: генератор, где элементы это число строк с кодом в файле
	"""
	if not os.path.exists(folder_name):
		raise FileExistsError
	for file_name in os.listdir(folder_name):
		result = 0
		if not os.path.isfile(os.path.join(folder_name, file_name)) or not file_name.endswith(".py"):
			continue
		with open(os.path.join(folder_name, file_name), "r", encoding="utf-8") as file:
			for rows in file.readlines():
				if not rows.startswith("#") and rows != "\n":
					result += len(rows)
			yield result


for elem in count_rows("C:\\Users\\мвидео\\PycharmProjects\\education\\Skillbox\\13 Итераторы и генераторы"):
	print(elem)
