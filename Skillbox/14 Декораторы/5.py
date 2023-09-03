"""
Создайте декоратор, который кэширует (сохраняет для дальнейшего использования) результаты вызова функции и,
при повторном вызове с теми же аргументами, возвращает сохранённый результат.

Примените его к рекурсивной функции вычисления чисел Фибоначчи.
"""
from typing import Callable, Any, Optional
import functools
import time

dict_caching: dict = dict()


def caching(func: Callable) -> Callable:
	"""Декоратор для кэширования данных функций, для последующего ускорения работы вложенной функции"""
	@functools.wraps(func)
	def wrapped_func(*args, **kwargs) -> Any:
		# TODO не понял как корректно сохранить аргументы при рекурсии, и как их корректно вернуть. Нужно реализовать.
		result = func(*args, **kwargs)
		return result
	return wrapped_func


def timer(func: Callable) -> Callable:
	"""Декоратор - таймер, для подсчета время выполнения вложенной функции"""

	def wrapped_func(*args, **kwargs) -> Any:
		time_start = time.time()
		result = func(*args, **kwargs)
		time_finish = time.time()
		print("{} длительность {} секунд".format(func.__name__, round(time_finish - time_start, 4)))
		return result

	wrapped_func.mark = True
	return wrapped_func


@timer
@caching
def my_fib(index: int, last_num: Optional[int] = 0, cur_num: Optional[int] = 1, counter: Optional[int] = 0) -> int:
	"""
	Возвращает значение элемента в ряде Фибоначчи под заданым индексом
	:param index: индекс элемента желаемого к получению
	:param last_num:  предыдущие число
	:param cur_num: текущие
	:param counter:  счетчик текущий операции
	:return: искомое число
	"""
	if index < 0:
		raise TypeError
	if index == 0:
		return last_num
	elif index == counter:
		return cur_num
	counter += 1
	result = my_fib(index=index, last_num=cur_num, cur_num=last_num + cur_num, counter=counter)
	return result


print(my_fib(index=100))
print(my_fib(index=100))
