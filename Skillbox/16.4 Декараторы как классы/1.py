from typing import Callable, Any
import functools
import datetime


def create_time(cls: Callable) -> Callable:
	"""Выводить дату создания экземпляра класса"""
	@functools.wraps(cls)
	def wrapped(*args, **kwargs) -> 'Person':
		instance = cls(*args, **kwargs)
		print("Дата и время созданию {} - {}".format(instance.name, datetime.datetime.now()))
		for name in dir(cls):
			if name.startswith("__"):
				continue
			print(name, end=", ")
		print()
		return instance
	return wrapped


@create_time
class Person:
	"""Персона, при рождении задается имя. Персона может умереть, вырасти, """
	def __init__(self, name) -> None:
		self.__name = name
		self.__age = 0
		self.status = True

	@property
	def age(self) -> int:
		"""Получить возраст экземпляра класса"""
		return self.__age

	@property
	def name(self) -> str:
		"""Получить имя экземпляра класса"""
		return self.__name

	def level_up(self):
		self.__age += 1
		if self.__age > 100:
			self.die()

	def die(self):
		self.status = False


men = Person("Стас")
men2 = Person("Оля")
print(men.name)
men.level_up()
men.level_up()
men.level_up()


