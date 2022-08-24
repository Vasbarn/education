#

# 4.2
# my_dict = {}
# while True:
# 	data = input("Введите Фамилию Имя Номер:").split()
# 	if len(data) == 3:
# 		new_key = (data[0], data[1])
# 		value = data[2]
# 		if my_dict.get(new_key):
# 			print(new_key, "уже записан")
# 		else:
# 			my_dict[new_key] = value
# 	else:
# 		print("Что-то не так")
# 4.1
# data = {
# 	(5000, 123456): ('Иванов', 'Василий'),
# 	(6000, 111111): ('Иванов', 'Петр'),
# 	(7000, 222222): ('Медведев', 'Алексей'),
# 	(8000, 333333): ('Алексеев', 'Георгий'),
# 	(9000, 444444): ('Георгиева', 'Мария')
# }
#
# while True:
# 	query = input("Введите серию и номер паспорта: ").split()
# 	my_tuple = (int(query[0]), int(query[1]))
# 	if data.get(my_tuple):
# 		print("Вы нашли {} {}".format(data[my_tuple][0], data[my_tuple][1]))
# 	else:
# 		print("Таких нет")

# 3.3
# print([i_item for i_key, i_item in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])

# 3.2
# server_data = {
#     "server": {
#         "host": "127.0.0.1",
#         "port": "10"
#     },
#     "configuration": {
#         "access": "true",
#         "login": "Ivan",
#         "password": "qwerty"
#     }
# }
# for key, item in server_data.items():
#     print("{}:".format(key))
#     for key2, item2 in server_data[key].items():
#         print("\t{}: {}".format(key2, item2))

# 3.1
# incomes = {
#     'apple': 5600.20,
#     'orange': 3500.45,
#     'banana': 5000.00,
#     'bergamot': 3700.56,
#     'durian': 5987.23,
#     'peach': 10000.50,
#     'pear': 1020.00,
#     'persimmon': 310.00,
# }
# for key, item in incomes.items():
#     print("{}--{}".format(key, item))


# 2.3
# def check(data):
# 	mylist = []
# 	for num, value in enumerate(data):
# 		if num % 2 == 0:
# 			mylist.append(value)
# 	return mylist
#
#
# your_text = input("Введите текст:")
# your_text = check(your_text)
# print(your_text)


# 2.2
# import random
# text_strint = "абвгдеёжзийклмнопрст"
# list1 = [text_strint[random.randint(0, len(text_strint)-1)] for _ in range(10)]
# list2 = [text_strint[random.randint(0, len(text_strint)-1)] for _ in range(10)]
# print("Список 1 {}".format(list1))
# print("Список 2 {}".format(list2))
# dict1 = {x: y for x, y in enumerate(list1)}
# dict2 = {x: y for x, y in enumerate(list2)}
# print("Словарь 1 {}".format(dict1))
# print("Словарь 2 {}".format(dict2))

# 2.1 enumerate
# my_string = input("Введите строку с символом ~: ")
# print("Ответ: ", end="")
# for num, elem in enumerate(my_string):
# 	if elem == "~":
# 		print(num, end=" ")

# 1.3
# import random
#
#
# def change(nums):
# 	index = random.randint(0, 4)
# 	value = random.randint(100, 1000)
# 	new_tuple = tuple(nums[x] if x != index else value for x in range(5))
# 	return new_tuple, value
#
#
# my_nums = (1, 2, 3, 4, 5)
# new_nums, rand_val = change(my_nums)
# print(new_nums, rand_val)
# new_nums, rand_val_2 = change(new_nums)
# print(new_nums, rand_val_2 )
# rand_val += rand_val_2
# print(rand_val)

# 1.2
# import math
#
#
# def my_func(radius, height):
# 	my_side = 2 * math.pi * radius * height
# 	my_full = my_side + 2 * math.pi * radius ** 2
# 	return my_full, my_full
#
#
# rad = float(input("Введите радиус цилиндра: "))
# hei = float(input("Введите высоту цилиндра: "))
# side, full = my_func(rad, hei)
# print("Площадь боковой поверхности = {0:.2f}\n Полная площадь  = {0:.2f}".format(side, full))

# 1.1 задание
# import random
# tuple1 = tuple(random.randint(0, 5) for _ in range(10))
# tuple2 = tuple(random.randint(-5, 0) for _ in range(10))
# tuple3 = tuple1 + tuple2
# print("Третий картеж {}".format(tuple3), "\n Количество 0 = {}".format(tuple3.count(0)))

