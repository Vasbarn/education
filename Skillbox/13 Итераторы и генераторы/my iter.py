# 1 первый итератор
# def my_iter(iter_obj):
# 	iterrat = iter(iter_obj)
# 	while True:
# 		try:
# 			print(next(iterrat))
# 		except StopIteration:
# 			return
#
# my_list = [1, 2, 3]
# my_iter(my_list)

# 2 реализация итератора
# import random
#
#
# class MgIter:
# 	def __init__(self, limit: int):
# 		self.__limit = limit
# 		self.__counter = 0
#
# 	def __next__(self):
# 		if self.__counter < self.__limit:
# 			self.__counter += 1
# 			return random.randint(-10, 10)
# 		else:
# 			raise StopIteration
#
# 	def __iter__(self):
# 		return self
#
#
# my_iter = MgIter(5)
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
# # print(next(my_iter))
#
# for elem in my_iter:
# 	print(elem)

# 3


# class MyFib:
# 	def __init__(self, number: int):
# 		self.__counter = 0
# 		self.__current_num = 0
# 		self.__next_num = 1
# 		self.__number = number
#
# 	def __iter__(self):
# 		self.__counter = 0
# 		self.__current_num = 0
# 		self.__next_num = 1
# 		return self
#
# 	def __next__(self):
# 		self.__counter += 1
# 		if self.__counter > 1:
# 			if self.__counter > self.__number:
# 				raise StopIteration
#
# 			self.__current_num, self.__next_num = self.__next_num, self.__next_num + self.__current_num
# 		return self.__current_num
#
#
# fib = MyFib(10)
# for elem in fib:
# 	print(elem)
# print()
# print(8 in fib)

# 4 Генераторы

#
# def fib_generation(number: int):
# 	current_num = 0
# 	next_num = 1
# 	for _ in range(number):
# 		yield current_num
# 		current_num, next_num = next_num, current_num + next_num
# 		if current_num > 10 ** 6:
# 			return
#
#
# def squar(numbers):
# 	for elem in numbers:
# 		yield elem ** 2
#
#
# fin_g = fib_generation(10)
# for elem in fin_g:
# 	print(elem)
#
# print()
# # генератор от генератора
# print(sum(squar(fib_generation(10))))
#
# # генераторное выражение
# cubs_number_gen = (num ** 3 for num in range(10))
# for elem in cubs_number_gen:
# 	print(elem)

# задание под уроком
# 1
# class My_iter:
# 	def __init__(self):
# 		self.__counter = 0
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		self.__counter += 1
# 		return self.__counter - 1
#
#
# for elem in My_iter():
# 	print(elem)


# 2
# import random
#
#
# class MyIter:
# 	def __init__(self, numer: int):
# 		self.__numer = numer
# 		self.__counter = 0
# 		self.__cur_value = 0
# 		self.__next_value = self.__cur_value + random.random()
#
# 	def __iter__(self):
# 		self.__cur_value = 0
# 		self.__counter = 0
# 		self.__next_value = self.__cur_value + random.random()
# 		return self
#
# 	def __next__(self):
# 		if self.__counter > self.__numer:
# 			raise StopIteration
# 		self.__counter += 1
# 		self.__cur_value, self.__next_value = self.__next_value, self.__next_value + random.random()
# 		return round(self.__cur_value, 2)
#
#
# for elem in MyIter(5):
# 	print(elem)
#
# for elem in MyIter(5):
# 	print(elem)

# 3


# class Primes:
# 	def __init__(self, numer: int):
# 		self.__current_num = 1
# 		self.__numer = numer
# 		self.__memory = []
#
# 	def __iter__(self):
# 		self.__current_num = 1
#
# 		return self
#
# 	def __next__(self):
# 		while self.__current_num < self.__numer:
# 			self.__current_num += 1
# 			for num in self.__memory:
# 				if self.__current_num % num == 0:
# 					break
# 			else:
# 				self.__memory.append(self.__current_num)
# 				return self.__current_num
# 		raise StopIteration
#
#
# for elem in Primes(10):
# 	print(elem)


# генератор

# 1

# def my_generation():
# 	num = 0
# 	memory = []
# 	while True:
# 		for record in memory:
# 			if num % record == 0:
# 				break
# 		else:
# 			if num > 1:
# 				memory.append(num)
# 				yield num
# 		num += 1
#
#
# for elem in my_generation():
# 	print(elem)


# 2
from collections.abc import Iterable

some_txt_file = """1 2 3 4 5 6 7 8 9 10\n1 2 3 4 5 6 7 8 9 10"""


def generation(str_file: str) -> Iterable[int]:
	for rows in str_file.split("\n"):
		for elem in rows.split():
			yield int(elem)
#
#
def sum_my(iterator):
	total_sum = 0
	for elem in iterator:
		total_sum += elem
	return total_sum


gen = generation(some_txt_file)
print(sum_my(gen))

# Анотация типов

