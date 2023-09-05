import functools
from typing import Callable, Any


def singleton(cls) -> Callable:
	"""Делаем синглитон как можем"""
	@functools.wraps(cls)
	def wrapped_func(*args, **kwargs) -> Callable:
		nonlocal bank
		if bank is None:
			bank = cls(*args, **kwargs)
		return bank
	bank = None
	return wrapped_func


@singleton
class Example:
	pass


my_obj = Example()
my_another_obj = Example()
print(id(my_obj))
print(id(my_another_obj))
print(my_obj is my_another_obj)

# Результат:
# 1986890616688
# 1986890616688
# True
