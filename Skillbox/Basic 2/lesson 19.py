
# множества 3
# my_string = set(input("Введите строку: "))
# value = {x for x in my_string if '0' <= x <= '9'}
# print("Различные цифры в строк:", value)

# множества два
# import random
# num_list_1 = [random.randint(0, 30) for _ in range(40)]
# num_list_2 = [random.randint(0, 30) for _ in range(40)]
#
# print("Изначальный список 1:", num_list_1)
# print("Изначальный список 2:", num_list_2)
# num_list_1 = set(num_list_1)
# num_list_2 = set(num_list_2)
# print("Полученное множество 1:", num_list_1)
# print("Полученное множество 2:", num_list_2)
# print("Минимальное значение 1 множества (его и удалим):", min(num_list_1))
# print("Минимальное значение 2 множества (его и удалим):", min(num_list_2))
# num_list_1.remove(min(num_list_1))
# num_list_2.remove(min(num_list_2))
# print("Добавить по случайному числу от 100 до 200")
# num_list_1.add(random.randint(100, 200))
# num_list_2.add(random.randint(100, 200))
# print("Полученное множество 1:", num_list_1)
# print("Полученное множество 2:", num_list_2)
# union_data = num_list_1.union(num_list_2)
# intersection_data = num_list_1.intersection(num_list_2)
# print("Это объединение:", union_data)
# print("А это пересечение:", intersection_data)
# diff_2_1 = num_list_2.difference(num_list_1)
# print("Следующие элементы есть в только в множестве 2: ", diff_2_1)

# множества
# punctuation_marks = {".", ",", ";", ":", "!", "?"}
# my_text = input("Введите текст: ")
# count_list = sum([my_text.count(x) for x in punctuation_marks])
# print("Всего пунктуационных знаков:", count_list)

# комнады 3
# players_dict = {
# 	1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
# 	2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
# 	3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
# 	4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
# 	5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
# 	6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
# 	7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
# 	8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
# }
#
# list_a = [user["name"] for user in players_dict.values() if user["team"] == "A" and user["status"] == "Rest"]
# list_b = [user["name"] for user in players_dict.values() if user["team"] == "B" and user["status"] == "Training"]
# list_c = [user["name"] for user in players_dict.values() if user["team"] == "C" and user["status"] == "Travel"]
#
# print("Группа А и отдыхает", list_a)
# print("Группа B и тренируется", list_b)
# print("Группа C и путешествует", list_c)

# дебилизм тз
"""
family_member = {
	"name": "Jane",
	"surname": "Doe",
	"hobbies": ["running", "sky diving", "singing"],
	"age": 35,
	"children": [
		{
			"name": "Alice",
			"age": 6
		},
		{
			"name": "Bob",
			"age": 8
		}
	]
}"""


# family_member = dict()
# family_member["name"] = "Jane"
# family_member["surname"] = "Doe"
# family_member["hobbies"] = ["running", "sky diving", "singing"]
# family_member["age"] = 35
# family_member["children"] = [
# 	{"name": "Alice",
# 		"age": 6},
# 	{"name": "Bob",
# 		"age": 8}
# ]
#
#
# for my_dict in family_member.get("children"):
# 	if my_dict.get('name') == 'Bob':
# 		mark = True
# if mark:
# 	print(family_member["surname"])
# else:
# 	print("Nosurname")

# гистограмма частоты
# def analise_text(random_text):
# 	new_dict = {}
# 	for word in random_text:
# 		new_dict[word] = random_text.count(word)
# 	return new_dict
#
#
# my_text = input("Введите текст: ")
# value_dict = analise_text(my_text)
# sorted_value = dict(sorted(value_dict.items(), key=lambda x: x[0]))
# print(sorted_value)
# print("Максимальное значение: ", max(sorted_value.values()))

# словарь
# incomes = {
# 	'apple': 5600.20,
# 	'orange': 3500.45,
# 	'banana': 5000.00,
# 	'bergamot': 3700.56,
# 	'durian': 5987.23,
# 	'grapefruit': 300.40,
# 	'peach': 10000.50,
# 	'pear': 1020.00,
# 	'persimmon': 310.00,
# }
# total_sum = sum(incomes.values())
# print("Общий доход:", total_sum)
# min_good_key = min(incomes, key=incomes.get)
# print("Минимальное значение у ", min_good_key, "он равен", incomes.get(min_good_key))
# incomes.pop(min_good_key)
# print(incomes)

# склады
# small_storage = {
# 	'гвозди': 5000,
# 	'шурупы': 3040,
# 	'саморезы': 2000
# }
#
# big_storage = {
# 	'доски': 1000,
# 	'балки': 150,
# 	'рейки': 600
# }
# small_storage.update(big_storage)
# while True:
# 	name_goods = input("Введите название товара").lower()
# 	if small_storage.get(name_goods):
# 		print("Количество товара:", small_storage[name_goods])
# 	else:
# 		print("Такого товара нет")

# справочник
# new_dict = {}
# while True:
# 	new_contact = input("Введите новый контакт: ")
# 	number = input("Введите номер: ")
# 	if new_dict.get(new_contact) == None:
# 		new_dict[new_contact] = number
# 	else:
# 		print("Такой контакт уже есть!")
# 	print(new_dict)

# студент
# def separate(var_text):
# 	var_list = var_text.split()
# 	my_dict = {
# 		"Имя": var_list[0],
# 		"Фамилия": var_list[1],
# 		"Город": var_list[2],
# 		"Место учебы": var_list[3],
# 		"Оценки": var_list[4:]
# 	}
# 	return my_dict
#
#
# value = input("Введите имя, фамилию, город, место учебы, оценки: ")
# value = separate(value)
# print(value)

# словарь квадратов чисел
# def make_dict(numer):
# 	new_dict = dict()
# 	for iterate in range(1, numer + 1):
# 		new_dict[iterate] = iterate ** 2
# 	print(new_dict)
#
#
# int_num = int(input("Введите номер:"))
# make_dict(int_num)
