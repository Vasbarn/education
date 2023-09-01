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


def fib_generation(number: int):
	current_num = 0
	next_num = 1
	for _ in range(number):
		yield current_num
		current_num, next_num = next_num, current_num + next_num
		if current_num > 10 ** 6:
			return


def squar(numbers):
	for elem in numbers:
		yield elem ** 2


fin_g = fib_generation(10)
for elem in fin_g:
	print(elem)

print()
# генератор от генератора
print(sum(squar(fib_generation(10))))

# генераторное выражение
cubs_number_gen = (num ** 3 for num in range(10))
for elem in cubs_number_gen:
	print(elem)
