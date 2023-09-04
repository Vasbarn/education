# 1
"""
Напишите декоратор check_permission, который проверяет, есть ли у пользователя доступ к вызываемой функции, и если нет,
то выдаёт исключение PermissionError.
"""
import functools
from typing import Callable, Any


users_permission = ['admin']


def check_permission(user_name: str) -> Callable:
	def check_permission_into(func: Callable) -> Callable:
		"""
		Декоратор, который проверяет пользователя на наличие прав выполнить функцию
		"""
		@functools.wraps(func)
		def wrapped_func(*args, **kwargs) -> Any:
			if user_name not in users_permission:
				raise PermissionError ('У пользовать {} недостаточно прав для выполнения функции {}'.format(
					user_name, func.__name__)
				)
			result = func(*args, **kwargs)
			return result
		return wrapped_func
	return check_permission_into


@check_permission("admin")
def del_site():
	print("Удаление сайта")


@check_permission("user_1")
def add_comment():
	print("Добавляем комментарий")


del_site()
add_comment()
