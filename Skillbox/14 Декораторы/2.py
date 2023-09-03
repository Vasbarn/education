"""
Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.
"""

from typing import Callable, Any, Optional
import functools
import time


def wait_seconds(count: int) -> Callable:
	def wait_seconds_into(func: Callable) -> Callable:
		"""
		Декоратор, который добавляет паузу перед выполнением вложенной функции.
		Есть возможность передать время паузы, по умолчанию 5 секунд.
		"""
		@functools.wraps(func)
		def wrapped_func(*args, **kwargs) -> Any:
			print("Ждем {} секунд...".format(count))
			time.sleep(count)
			return func(*args, **kwargs)
		return wrapped_func
	return wait_seconds_into


@wait_seconds(3)
def print_hello() -> None:
	"""Пишем строчку"""
	print("Hello")


print_hello()
print(print_hello.__doc__)
