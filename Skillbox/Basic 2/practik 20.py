# 10
# my_string = "abcd"
# my_tuple = (1, 2, 3, 4)
# value = ((my_string[num], my_tuple[num]) for num in range(min(len(my_tuple), len(my_string))))
# print(value)
# for elem in value:
# 	print(elem)

# 9 затупил
# count_record = 6  # int(input("Сколько было игр?"))
# new_dict = dict()
# total = dict()
# test = ["123 мама", "123 амама", "123 ямама", "124 я", "124 ты", "122 оно"]
# for i_num in range(1, count_record + 1):
# 	record = test[i_num-1].split()  # input("{}-я запись: ".format(i_num)).split()
# 	if new_dict.get(record[1]):
# 		if new_dict[record[1]] >= record[0]:
# 			pass
# 		else:
# 			new_dict[record[1]] = record[0]
# 	else:
# 		new_dict[record[1]] = record[0]
# print(new_dict)
# top_list = []
#
# for key, item in new_dict.items():
# 	item = int(item)
# 	if len(top_list) < 3:
# 		top_list.append([item, key])
# 	else:
# 		for i_top in range(len(top_list)-1, -1, -1):
# 			if item > top_list[i_top][0]:
# 				top_list.pop(i_top)
# 				top_list.insert(i_top, [item, key])
# 				break
#
# print(top_list)
# flag = True
# while flag:
# 	flag = False
# 	for i_list in range(len(top_list)-1):
# 		if top_list[i_list][0] < top_list[i_list + 1][0]:
# 			flag = True
# 			top_list[i_list], top_list[i_list + 1] = top_list[i_list + 1], top_list[i_list]
#
#
# print(top_list)

# 8
# my_contacts = dict()
# def add_new_contact(value, var_dict):
# 	if var_dict.get((value[0], value[1])):
# 		print("Такой контакт уже есть!")
# 	else:
# 		var_dict[(value[0], value[1])] = value[2]
# 	print("Текущий словарь:\n", var_dict)
#
#
# def search_contact(value, var_dict):
# 	for key, item in var_dict.items():
# 		if value.lower() in key:
# 			print(key, item)
# 		else:
# 			print("Таких нет")
#
#
# while True:
# 	my_command = input("Добавить контакт или найти контакт?").lower()
# 	if my_command == "добавить контакт":
# 		data = input("Введите Фамилию Имя и Номер через пробел").lower().split()
# 		if len(data) == 3:
# 			add_new_contact(data, my_contacts)
# 		else:
# 			print("Данные не корректны")
# 	elif my_command == "найти контакт":
# 		data = input("Введите кого хотите найти:").lower()
# 		search_contact(data, my_contacts)
# 	else:
# 		print("Выбирайте одно из двух:")


# 7
# def get_tuple(var_tuple):
# 	if isinstance(sum(var_tuple), float):
# 		return tuple()
# 	else:
# 		return tuple(sorted(var_tuple))
#
#
# default_tuple = (-23, 123, 13, 96, -22, 0, -1, 99, -17)
# new_tuple = get_tuple(default_tuple)
# print(default_tuple)
# print(new_tuple)

# 6
# import random
# start_list = [random.randint(0, 10) for _ in range(10)]
# second_second_list = [(start_list[x], start_list[x + 1]) for x in range(0, 10, 2)]
# print(start_list)
# print(second_second_list)

# 5
# my_data = {
# 	("Васильева", "Эльвира"): 25,
# 	("васильев", "александр"): 27,
# 	("Пуц", "георгий"): 25,
# 	("попов", "Ян"): 27,
# }
#
# while True:
# 	text = input("Кого ищем: ").lower()
# 	for key in my_data:
# 		for part in range(len(key)):
# 			if key[part].lower().find(text) != -1:
# 				print(key[0], key[1], my_data[key])




# 4
# players = {
# 	("Ivan", "Volkin"): (10, 5, 13),
# 	("Bob", "Robbin"): (7, 5, 14),
# 	("Rob", "Bobbin"): (12, 8, 2)
# }
#
# new_file = []
# for key, item in players.items():
# 	new_file.append(key + item)
# print(new_file)


# 3
# import random
#
#
# def do_it(var_tuple, value):
# 	if var_tuple.count(value) == 2:
# 		new_tuple = var_tuple[var_tuple.index(value):]
# 		print("Два точно есть")
# 		return new_tuple[:new_tuple[1:].index(value) + 2]
# 	elif var_tuple.count(value) == 1:
# 		print("Есть только один")
# 		return var_tuple[var_tuple.index(value):]
# 	else:
# 		print("Не повезло")
# 		return tuple()
#
#
# my_tuple = tuple(random.randint(1, 50) for _ in range(50))
# my_value = random.randint(1, 49)
# print(my_tuple)
# print(my_value)
#
# my_value = do_it(my_tuple, my_value)
# print(my_value)

# 2 ошибка в тз
# def is_prime(num):
# 	count = 0
# 	for numer in range(2, num + 1):
# 		if num % numer == 0:
# 			count += 1
# 		if count > 1:
# 			return False
# 	return True
#
#
# def get_list(value):
# 	return [item for my_index, item in enumerate(value) if is_prime(my_index)]
#
#
# my_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data = get_list(my_value)
# print(data)

# 1
# students = {
# 	1: {
# 		'name': 'Bob',
# 		'surname': 'Vazovski',
# 		'age': 23,
# 		'interests': ['biology, swimming']
# 	},
# 	2: {
# 		'name': 'Rob',
# 		'surname': 'Stepanov',
# 		'age': 24,
# 		'interests': ['math', 'computer games', 'running']
# 	},
# 	3: {
# 		'name': 'Alexander',
# 		'surname': 'Krug',
# 		'age': 22,
# 		'interests': ['languages', 'health food', 'running']
# 	}
# }
#
#
# def uniq_hobby(var_dict):
# 	surnames_len = 0
# 	total_interests = set()
# 	for elem in var_dict.values():
# 		surnames_len += len(elem["surname"])
# 		total_interests.update(elem["interests"])
# 	return total_interests, surnames_len
#
#
# id_age = []
# for key, item in students.items():
# 	id_age.append((key, students[key]["age"]))
# print("Список с ID и возрастом:", id_age)
#
# interests, len_surnames = uniq_hobby(students)
# print("Все интересы: ", interests)
# print("Длина всех фамилия составляет {} символа".format(len_surnames))