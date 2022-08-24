

# 4
# почитал задания и забил

# 3
# import os
#
# name = "Папка для тестов"
# path = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop") + os.sep
# full_name = path + name + os.sep
#
#
# def gen_files_path():
#     return [full_name + new_name for new_name in os.listdir(full_name)]
#
#
# for elem in gen_files_path():
#     print(elem)


# 2
# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
# [print(x, y, x * y)  for x in list_1 for y in list_2 if x * y == to_find]

# from collections.abc import Iterable
# # 1
#
#
# class MyIter:
# 	def __init__(self, value: int):
# 		self.__value = value
# 		self.__count = 0
#
# 	def __iter__(self) -> Iterable[int]:
# 		self.__count = 0
# 		return self
#
# 	def __next__(self) -> int:
# 		self.__count += 1
# 		if self.__count > self.__value:
# 			raise StopIteration
# 		return self.__count ** 2
#
#
# def func_gen(value):
# 	count = 1
# 	while True:
# 		yield count ** 2
# 		count += 1
# 		if count > value:
# 			break
#
#
# one = MyIter(10)
# for elem in one:
# 	print(elem)
# print()
# gen_x = func_gen(10)
# for elem in gen_x:
# 	print(elem)
# print()
# [print(x ** 2) for x in range(1, 11)]
