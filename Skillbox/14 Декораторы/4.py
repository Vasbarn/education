"""
Реализуйте декоратор counter, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы global и nonlocal (об этом мы ещё расскажем).
"""
from typing import Callable, Any
import functools


dict_counter: dict[str, int] = dict()


def counter(func: Callable) -> Callable:
	"""Декоратор для подсчета количество раз вызова функций с этим декоратором"""
	@functools.wraps(func)
	def wrapped_func(*args, **kwargs) -> Any:
		if dict_counter.get(func.__name__):
			dict_counter[func.__name__] += 1
		else:
			dict_counter[func.__name__] = 1
		result = func(*args, **kwargs)
		return result
	return wrapped_func


@counter
def func1() -> None:
	"""Болванка"""
	pass


@counter
def func2() -> None:
	"""Болванка"""
	pass


func1()
func1()
func2()

print(dict_counter)
