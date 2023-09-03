class File:
	def __init__(self, path_to_file: str, mode: str) -> None:
		self.__mode = mode
		self.__path = path_to_file
		self.__file = None

	def __enter__(self):
		try:
			self.__file = open(self.__path, self.__mode, encoding="utf-8")
		except FileNotFoundError:
			self.__file = open(self.__path, "w", encoding="utf-8")
		return self.__file

	def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
		self.__file.close()
		return True


with File("text.txt", "r") as file:
	print(file.read())