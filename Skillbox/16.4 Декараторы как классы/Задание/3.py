"""
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и в который
можно передавать формат вывода даты и времени логирования
"""
from typing import Callable, Any
import functools
import datetime

# TODO не смог понять как корректно передать аргумент
# def decorate_class(date_format: str = "yyyy") -> Callable:
# 	"""Декоратор для логирования функций, с указанием формата даты логирования"""
def decorate_class_into(func: Callable) -> Callable:
	@functools.wraps(func)
	def wrapped_func(*args, **kwargs) -> Any:
		print("{date} - Работает функция '{name_func}'".format(
			date=datetime.datetime.now(),
			name_func=func.__name__
		))
		print("Порядковые аргументы:")
		print("Именованные аргументы:")
		result = func(*args, **kwargs)
		return result
	return wrapped_func
	# return decorate_class_into


def for_all_method(cls):
	# @functools.wraps(decorator)
	# def decorate(cls):
	# 	"""Декоратор для применения другого декоратора ко всем* функциям класса"""
	for method in dir(cls):
		if method.startswith("__"):
			continue
		current_method = getattr(cls, method)
		setattr(cls, method, decorate_class_into(current_method))
	return cls
	# return decorate


@for_all_method
class A:

	def print_name(self):
		print("Я класс")

	def say_hello(self):
		print("Hello")


A().print_name()
A().say_hello()
