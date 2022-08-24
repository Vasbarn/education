# 5
# import os
# name = "numbers2.txt"
# path = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep
#
# with open(path + name, 'r', encoding="utf-8") as file:
# 	for rows in file:
# 		print(rows)


# 4

# def issimple(value):
# 	num = 0
# 	for item in range(2, value + 1):
# 		if value % item == 0:
# 			num += 1
# 		if num > 1:
# 			return False
# 	return True
#
#
# def endless_gen():
# 	start_num = 0
# 	while True:
# 		if issimple(start_num):
# 			yield start_num
# 		start_num += 1
#
#
# for elem in endless_gen():
# 	print(elem)

# 3
# import random
#
#
# class MyIter:
# 	def __init__(self, value):
# 		self.__counter = 0
# 		self.__max = value
# 		self.__f_val = 0
#
# 	def __iter__(self):
# 		self.__counter = 0
# 		self.__f_val = 0
# 		return self
#
# 	def __next__(self):
# 		self.__counter += 1
# 		if self.__counter > self.__max:
# 			raise StopIteration()
# 		self.__f_val += random.random()
# 		return self.__f_val
#
#
# elems_cls = MyIter(5)
# for elem in elems_cls:
# 	print(elem)


# 2 мой счетчик

# class СountIterator:
# 	def __init__(self):
# 		self.__counter = 0
#
# 	def __iter__(self):
# 		self.__counter = 0
# 		return self
#
# 	def __next__(self):
# 		self.__counter += 1
# 		return  self.__counter
#
#
# my_iter = СountIterator()
# for i_elem in my_iter:
# 	print(i_elem)


# 1 свой for
# import random
# my_list = [random.randint(0, 20)for _ in range(5)]
# print(my_list )
# iter_of_my_list = my_list.__iter__()
# while True:
# 	try:
# 		new_elem = iter_of_my_list.__next__()
# 		print(new_elem)
# 	except StopIteration:
# 		break

