"""При работе с сетью и веб-сервисами иногда используется функция callback, так называемая функция обратного вызова.
Это функция, которая вызывается при срабатывании определённого события: переходе на страницу, получении сообщения или
окончании обработки процессором. В неё можно передать функцию, чтобы она выполнилась после определённого события. Это
используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.
"""
from typing import Callable, Any
import functools


app: dict[str:Callable] = dict()


def get_func(name_func: str) -> Callable:
	"""Декоратор, который возвращает запрашиваемую функцию"""
	def into_func(func: Callable) -> Callable:
		app[name_func] = func

		@functools.wraps(func)
		def wrapped_func(*args, **kwargs) -> Any:
			return func(п*args, **kwargs)
		return wrapped_func
	return into_func


@get_func("\\")
def func_for_apI():
	"""Функция делающая что-то"""
	return "OK"


print(app)
response = app.get("\\")
if response:
	response = response()
	print("Ответ:", response)
else:
	print("Ответ: такой функции нет")
