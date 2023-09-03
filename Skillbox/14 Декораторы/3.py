"""
Реализуйте декоратор logging, который будет отвечать за логирование функций. На экран выводится название функции и её
документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл function_errors.log записываются
название функции и ошибки.

Также постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки, а обрабатывала все
декорируемые функции и сразу записывала все ошибки в файл.

Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.
"""
from typing import Callable, Any
import functools
from datetime import datetime


def logging(func: Callable) -> Callable:
	"""
	Логирование выполнения функций, если в ходе работы вложенной функции возникает ошибка, она будет сохранена в
	отдельный файл.
	"""
	@functools.wraps(func)
	def wrapped_func(*args, **kwargs) -> Any:
		try:
			print("Приступаю к выполнению функции {name}".format(name=func.__name__))
			print("Документация:\n{doc}".format(doc=func.__doc__))
			result = func(*args, **kwargs)
			print()
			return result
		except Exception as _exc:
			with open("all_errors.log", "a", encoding="utf-8") as file:

				text = "{} - {}\n".format(datetime.now(), _exc)
				file.write(text)
	return wrapped_func


@logging
def func1() -> None:
	"""Документация первой функции"""
	print("Отработала первая функция")


@logging
def func2() -> None:
	"""Документация второй функции"""
	print("Отработала вторая функция")


@logging
def func3() -> None:
	"""Документация третьей функции"""
	raise TypeError("Очевидная ошибка типа данных")
	print("Отработала третья функция")


@logging
def func4() -> None:
	"""Документация четвертой функции"""
	print("Отработала четвертой функция")


func1()
func2()
func3()
func4()

