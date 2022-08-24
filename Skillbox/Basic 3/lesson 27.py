# 6
# from typing import Callable, Dict
#
# PLUGINS: Dict = dict()
#
#
# def plug_1(func: Callable) -> Callable:
# 	PLUGINS[plug_1.__name__] = plug_1
# 	return func
#
#
# def plug_2(func: Callable) -> Callable:
# 	PLUGINS[plug_2.__name__] = plug_2
# 	return func
#
#
# @plug_1
# @plug_2
# def my_def():
# 	pass
#
# print(PLUGINS)

# 5
# from typing import Callable
#
#
# def bread_top(func: Callable) -> Callable:
# 	def wrapped_func(*args, **kwargs):
# 		func(*args, **kwargs)
# 		return print("</{}\\>".format("-" * 7))
# 	return wrapped_func
#
#
# def bread_down(func: Callable) -> Callable:
# 	def wrapped_func(*args, **kwargs):
# 		func(*args, **kwargs)
# 		return print("</{}\\>".format("_" * 7))
# 	return wrapped_func
#
#
# def into(func: Callable) -> Callable:
# 	def wrapped_func(*args, **kwargs):
# 		func(*args, **kwargs)
# 		return print("#Помидоры#\n--Ветчина--\n~Салат~")
# 	return wrapped_func
#
#
# @bread_top
# @into
# @bread_down
# def sandwich():
# 	return


# sandwich()
# 4
# from typing import Callable, Any, List
# import time
#
#
# def timer(func: Callable) -> Callable:
# 	"""Замеряем время выполнения передаваемой функции и выводим на экран"""
# 	def wrapped_func(*args, **kwargs) -> Any:
# 		start_time = time.time()
# 		result = func()
# 		end_time = time.time()
# 		duration = round(end_time - start_time, 4)
# 		print("Время отработки функции составило {} секунды".format(duration))
# 		return result
# 	return wrapped_func
#
#
# @timer
# def hard_func() -> List:
# 	my_list = []
# 	for x in range(1000):
# 		print(x)
# 		for y in range(100):
# 			for z in range(1000):
# 				my_list.append(x * y * z)
# 	return my_list
#
#
# hard_func()

# 3
# from typing import Callable, Any
#
#
# def do_twice(func: Callable) -> Callable:
#
# 	def wrapped_func(*args, **kwargs) -> Any:
# 		func(*args, **kwargs)
# 		func(*args, **kwargs)
# 	return wrapped_func
#
#
# @do_twice
# def greeting(name: str) -> None:
# 	print('Привет, {name}!'.format(name=name))
#
#
# greeting("Саша")

# 2
# from typing import Callable, Any, List
# import time
#
#
# def timer(func: Callable) -> Any:
# 	"""Замеряем время выполнения передаваемой функции и выводим на экран"""
# 	start_time = time.time()
# 	result = func()
# 	end_time = time.time()
# 	duration = round(end_time - start_time, 4)
# 	print("Время отработки функции составило {} секунды".format(duration))
# 	return result
#
#
# def hard_func() -> List:
# 	my_list = []
# 	for x in range(1000):
# 		print(x)
# 		for y in range(100):
# 			for z in range(1000):
# 				my_list.append(x * y * z)
# 	return my_list


# timer(hard_func)




# 1
# from typing import Callable, Any
#
#
# def func_2(func: Callable, *args, **kwargs) -> Any:
# 	"""Перемножаем значение двух внутренних функций"""
# 	result_1 = func(*args, **kwargs)
# 	result_2 = func(*args, **kwargs)
# 	return result_1 * result_2
#
#
# def func_1(x: int,) -> int:
# 	return x + 10
#
#
# print(func_2(func_1, 0))


