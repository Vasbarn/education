"""
Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он написал надоедливый декоратор,
который при вызове декорируемой функции спрашивает у пользователя «Как дела?», вне зависимости от ответа
пишет что-то вроде «А у меня не очень!» и только потом запускает саму функцию.
"""
from typing import Callable, Any
import functools


def my_decoration(func: Callable) -> Callable:
	"""Декоратор, который перед выполнением вложенной функции запрашивает подтверждение"""

	@functools.wraps(func)
	def wrapped_func(*args, **kwargs) -> Any:
		input("Вы действительно хотите, чтобы {} начала выполняться?\n".format(func.__name__))
		print("По большому счету, мне без разницы что ты хочешь, я начинаю выполнение")
		return func(*args, **kwargs)
	return wrapped_func


@my_decoration
def func_test() -> None:
	print("Работать")


func_test()
