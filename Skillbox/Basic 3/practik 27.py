# 4
def debug(func):
	def wrapped_func(*args, **kwargs):
		print(repr("Название функции {}".format(repr(func))))
		result = func(*args, **kwargs)
		print("Вернула {}".format(result))
		return result
	return wrapped_func


@debug
def my_func(**kwargs):
	for key, value in kwargs.items():
		if key == "name":
			print("Привет {}.".format(key))
			return 5

my_func(name="саша")

# 3

# def logging(func):
# 	def wrapped_func(*args, **kwargs):
# 		print(func.__name__, func.__doc__)
# 		result = None
# 		try:
# 			result = func(*args, **kwargs)
# 		except Exception as error:
# 			with open("function_errors.log", 'a', encoding="utf-8") as file:
# 				file.write("{}\t{}".format(func.__name__, error))
#
# 		return result
# 	return wrapped_func
#
#
# @logging
# def my_func(value):
# 	return value + 2
#
#
# my_func(2)
# my_func("ФФФ")

# 2
# import time
#
#
# def sleep(func):
# 	def wrapped_func(*args, **kwargs):
# 		time.sleep(3)
# 		result = func(*args, **kwargs)
# 		return result
# 	return wrapped_func
#
#
# @sleep
# def say_hi():
# 	print("Привет")
#
#
# say_hi()

# 1

# def how_are_you(func):
# 	def wrapped_func(*args, **kwargs):
# 		input("Как твои дела?\n")
# 		print("А мои не очень, ладно к делу...")
# 		result = func(*args, **kwargs)
# 		return result
# 	return wrapped_func
#
#
# @how_are_you
# def simple_func():
# 	print("2 + 2 = {}".format(2 + 2))
#
#
# simple_func()
