# 3.3
# def create_dict(data, template=None):
# 	if template is None:
# 		template = dict()
# 	if isinstance(data, dict):
# 		return data
# 	if isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
# 		template[data] = data
# 		return template
#
#
# def data_preparation(old_list):
# 	new_list = []
# 	for i_element in old_list:
# 		new_list.append(create_dict(i_element))
# 	return new_list
#
#
# data = ["sad", {"sds": 23}, {43}, [12, 42, 1], 2323]
# data = data_preparation(data)
# print(data)

# 3.2
# def my_func(num, lst=None):
# 	if lst is None:
# 		lst = [num]
# 		print(lst)
#
#
# my_func(5)
# my_func(10)
# my_func(15)

# 3.1
# def strange_def(arg1, arg2="Неверный ввод. Пожалуйста, введите 'да' или 'нет'.", arg3=4):
# 	if arg1.lower() == "да":
# 		return 1
# 	elif arg1.lower() == "нет":
# 		return 0
# 	else:
# 		arg3 -= 1
# 		if arg3 <= 0:
# 			print("Спасибо! Было классно! Приходите еще!")
# 			return
# 		else:
# 			print("Осталось {} попытки".format(arg3))
# 			arg1 = input(arg2)
# 			return strange_def(arg1, arg2, arg3)
#
#
# question1 = input("Хотите сыру?\n")
# if 	strange_def(question1):
# 	question2 = input("С плесенью?\n")
# 	if strange_def(question2,"Вы гурман или нет?"):
# 		question3 = input("Вы уверены??\n")
# 		if strange_def(question3, "Последний шанс", 2):
# 			print("Кушайте")


# 2.2
# def about_me(value):
# 	print("Тип:", type(value))
# 	if type(value) in ["int", "float", "str", "tuple", "bool"]:
# 		print("Этот тип данных неизменяемых")
# 	elif type(value) in ['list', 'dict', 'set']:
# 		print("Этот тип данных изменяемый")
# 	else:
# 		print("Затрудняюсь ответить какой это тип данных")
# 	print("ID: {}".format(id(value)))
#
#
# var = {1}
# about_me(var)

# 2.1
# import random

# def change_dict(dct):
# 	num = random.randint(1, 100)
# 	new_dict = dict()
# 	for i_key, i_value in dct.items():
#
# 		if isinstance(i_value, list):
# 			new_dict[i_key] = [x for x in i_value]
# 			new_dict[i_key].append(num)
# 		if isinstance(i_value, dict):
# 			new_dict[i_key] = {x: y for x, y in i_value.items()}
# 			i_value[num] = i_key
# 		if isinstance(i_value, set):
# 			new_dict[i_key] = {x for x in i_value}
# 			new_dict[i_key].add(num)
# 		if isinstance(i_value, tuple):
# 			new_dict[i_key] = tuple(i_value[num] if num != len(i_value) else num for num in range(len(i_value) + 1))
# 	return new_dict
#
#
# nums_list = [1, 2, 3]
# some_dict = {1: 'text', 2: 'another text'}
# uniq_nums = {1, 2, 3}
# print(nums_list)
# print(some_dict)
# print(uniq_nums)
# common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
# new = change_dict(common_dict)
#
# print(common_dict)
# print(new)

# 1.3
# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Мой сайт'
# 		},
# 		'body': {
# 			'h2': 'Здесь будет мой заголовок',
# 			'div': 'Тут, наверное, какой-то блок',
# 			'p': 'А вот здесь новый абзац'
# 		}
# 	}
# }
#
#
# def search_element(value, var_dict):
# 	if value in var_dict:
# 		return var_dict[value]
# 	for val in var_dict.values():
# 		if isinstance(val, dict):
# 			result = search_element(value, val)
# 			if result:
# 				break
# 	else:
# 		result = None
# 	return result
#
#
# while True:
# 	my_value = input("Введите ключ: ")
# 	search_value = search_element(my_value, site)
# 	print(search_value)

# 1.2
# def power(a, n):
# 	if n == 1:
# 		return a
# 	else:
# 		return a * power(a, n-1)
#
#
# float_num = float(input('Введите вещественное число: '))
# int_num = int(input('Введите степень числа: '))
# print(float_num, '**', int_num, '=', power(float_num, int_num))

# 1.1

# def my_factor(num):
# 	if num == 1:
# 		return num
# 	else:
# 		return num * my_factor(num - 1)
#
#
# value = int(input("Введите число: "))
# print("Факториал числа {} = {}".format(value, my_factor(value)))
