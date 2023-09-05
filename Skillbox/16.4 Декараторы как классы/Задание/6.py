from typing import Callable
import functools
import time


class LogerDecorator:
	"""Класс декоратор"""
	def __init__(self, func: Callable) -> None:
		self.__func = func
		functools.update_wrapper(self, self.__func)

	def __call__(self, *args, **kwargs) -> Callable:
		start = time.time()
		print("Порядковые аргументы:", *args)
		print("Bvtyyst аргументы:", *kwargs)
		result = self.__func(*args, **kwargs)
		print("Результат:", result)
		print("Время выполнения:", time.time() - start)
		return result


@LogerDecorator
def hard_func():
	print("Ух тружусь")

hard_func()