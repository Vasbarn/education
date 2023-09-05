"""
Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая должна быть декоратором,
и даёт возможность любому декоратору принимать произвольные аргументы.
"""
from typing import Callable, Any
import functools


def decorated_decorator2(decorator: Callable):
	"""Декоратор дает возможность другому декоратору принимать аргументы"""
	def decorator_maker(*args, **kwargs) -> Callable:
		def decorator_wrapped(func: Callable):
			return decorator(func, *args, **kwargs)
		return decorator_wrapped
	return decorator_maker


@decorated_decorator2
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
	"""Обычный декоратор"""
	@functools.wraps(func)
	def wrapped_func(*args2, **kwargs2) -> Any:
		print(args)
		print(kwargs)
		print("Обычный декоратор отработал")
		return func(*args2, **kwargs2)
	return wrapped_func


@decorated_decorator(1, 2, 3, ключ=123)
def my_func(my_text: str, my_int: int) -> None:
	"""Моя функция"""
	print("Привет", my_text, my_int)


my_func("Алекс", 22)



