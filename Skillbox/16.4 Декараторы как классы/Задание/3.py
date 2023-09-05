"""
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и в который
можно передавать формат вывода даты и времени логирования
"""
from typing import Callable, Any
import functools
import datetime


def decorate_class(date_format: str = '%d.%m.%Y %H:%M') -> Callable:
	"""Декоратор для логирования функций, с указанием формата даты логирования"""
	def decorate_class_into(func: Callable) -> Callable:
		@functools.wraps(func)
		def wrapped_func(*args, **kwargs) -> Any:
			print("{date} - Работает функция '{name_func}'".format(
				date=datetime.datetime.now().strftime(date_format),
				name_func=func.__name__
			))

			result = func(*args, **kwargs)
			print("Порядковые аргументы:", *args)
			print("Именованные аргументы:", **kwargs)
			return result
		return wrapped_func
	return decorate_class_into


def for_all_method(decorator):
	@functools.wraps(decorator)
	def decorate(cls):
		"""Декоратор для применения другого декоратора ко всем* функциям класса"""
		for method in dir(cls):
			if method.startswith("__"):
				continue
			current_method = getattr(cls, method)
			setattr(cls, method, decorator(current_method))
		return cls
	return decorate


@for_all_method(decorate_class())
class A:

	@classmethod
	def print_name(cls, *args, **kwargs):
		print("Я класс")

	@classmethod
	def say_hello(cls, *args, **kwargs):
		print("Hello")


A().print_name()
A().say_hello()
