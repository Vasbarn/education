# 1
# """Реализуйте класс File — контекстный менеджер для работы с файлами.
# # Он должен принимать на вход имя файла и режим чтения/записи и открывать сам файл.
# В начале работы менеджер возвращает файловый объект,
# # а в конце — закрывает файл."""
#
#
# class File:
# 	def __init__(self, path_to_file: str, mode: str) -> None:
# 		self.__mode = mode
# 		self.__path = path_to_file
# 		self.__file = None
#
# 	def __enter__(self):
# 		self.__file = open(self.__path, self.__mode, encoding="utf-8")
# 		return self.__file
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		self.__file.close()
# 		return True
#
#
# with File("урок.py", "r") as file:
# 	print(file.read())

# 2

# class Example:
# 	def __init__(self):
# 		print("Вызов __init__")
#
# 	def __enter__(self):
# 		print("Вызов __enter__")
# 		return True
#
# 	def __exit__(self, exc_type, exc_val, exc_tb):
# 		print("Вызов __exit__")
# 		if exc_type:
# 			print("Тип ошибки: {}\nЗначение ошибки: {}\n'След' ошибки: {}".format(exc_type, exc_val, exc_tb))
# 		return True
#
#
# my_obj = Example()
#
# with my_obj as obj:
# 	print('Код внутри первого вызова контекст менеджера')
# 	with my_obj as obj2:
# 		raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
# 	print('Я обязательно выведусь...')

