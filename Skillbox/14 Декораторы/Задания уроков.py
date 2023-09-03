# Функции высшего порядка
# 1
# """
# Дана функция func_1, которая принимает число и возвращает результат его сложения с числом 10:
# Реализуйте функцию высшего порядка func_2, которая будет возвращать перемножение двух результатов переданной функции.
# """
# from typing import Callable
#
#
# def sum_it(a: [int, float]) -> [int, float]:
# 	return a + 10
#
#
# def product_it(func: Callable, *args, **kwargs) -> Callable:
# 	return func(*args, **kwargs) * func(*args, **kwargs)
#
#
# answer = sum_it(9)
# print(answer)
# answer = product_it(sum_it, 9)
# print(answer)

# 2
# """
# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы переданной
# функции func и выдаёт ответ на экран.
# """
#
# from typing import Callable
# import time
#
#
# def timer(func: Callable, *args, **kwargs) -> Callable:
# 	time_start = time.time()
# 	result = func(*args, **kwargs)
# 	time_finish = time.time()
# 	print("Время выполнения {name_func} = {duration} сек".format(
# 		name_func=func, duration=round(time_finish - time_start, 4)))
# 	return result
#
#
# def big_func() -> int:
# 	x = 2 ** 100000000
# 	return x
#
#
# timer(big_func)

# Декораторы
# 1
# """
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию.
# Не забывайте про документацию и аннотации типов.
# """
# from typing import Callable, Any
#
#
# def do_twice(func: Callable) -> Callable:
# 	"""
# 	Декоратор, который выполняет вложенную функцию 2 раза.
# 	"""
# 	def wrapped_func(*args, **kwargs) -> tuple:
# 		return func(*args, **kwargs), func(*args, **kwargs)
#
# 	return wrapped_func
#
#
# @do_twice
# def print_and_return_value(value: Any):
# 	print(str(value))
# 	return value
#
#
# result = print_and_return_value("Привет")
# print(result)

# 2
# """
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.
# """
# from typing import Callable, Any
# import time
#
#
# def timer(func: Callable) -> Callable:
# 	"""Декоратор - выводящий в терминал время выполнения переданной функции."""
# 	def wrapped_func(*args, **kwargs) -> Any:
# 		time_start = time.time()
# 		result = func(*args, **kwargs)
# 		time_finish = time.time()
# 		print("Time duration {name} = {duration} sec.".format(name=func, duration=round(time_finish - time_start, 4)))
# 		return result
# 	return wrapped_func
#
#
# @timer
# def big_func() -> int:
# 	result = 2 ** 1000000
# 	return result
#
#
# x = big_func()
# print(x)

# 3
# """
# Есть функция, которая выводит начинку сэндвича. Сверху и снизу от начинки идут различные ингредиенты вроде салата,
# помидоров и других. Всё это в свою очередь содержится между двух половинок булочки. Реализуйте такую функцию и два
# соответствующих декоратора — ингредиенты и хлеб.
# """
# from typing import Callable, Any
#
#
# def intro(func: Callable) -> Callable:
# 	"""Декоратор выводящий в терминал начинку сэндвича"""
# 	def wrapped_func(*args, **kwargs) -> Any:
# 		print("-----соус------")
# 		print("------сыр------")
# 		print("---помидорка----")
# 		print("---котлетка----")
# 		print("-----соус------")
# 		return func(*args, **kwargs)
# 	return wrapped_func
#
#
# def bread(func:Callable) -> Callable:
# 	"""Декоратор выводящий в терминал хлебные части от сэндвича"""
# 	def wrapped_func(*args, **kwargs) -> Any:
# 		print("||||Верх булочки|||||")
# 		result = func(*args, **kwargs)
# 		print("||||Низ булочки||||||")
# 		return result
# 	return wrapped_func
#
#
# @bread
# @intro
# def sandwich() -> None:
# 	return
#
#
# sandwich()

# 4
# """
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и
# заносить их в соответствующий словарь.
# """
# from typing import Callable
#
# PLUGINS = dict()
#
#
# def reg_plugin(func: Callable) -> Callable:
# 	PLUGINS[func.__name__] = func
# 	return func
#
#
# def func_test1(x: int, y: int) -> int:
# 	return x + y
#
#
# @reg_plugin
# def func_test2(x: int, y: int) -> int:
# 	return x + y
#
#
# def func_test3(x: int, y: int) -> int:
# 	return x + y
#
#
# @reg_plugin
# def func_test4(x: int, y: int) -> int:
# 	return x + y
#
#
# print(PLUGINS)
# print(func_test1(1, 1))
# print(func_test2(1, 1))
# print(func_test3(1, 1))
# print(func_test4(1, 1))

