# goods
goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_good = [input("Название товара: "), int(input("Цена: "))]
goods.append(new_good)
print(goods)
for elem in goods:
	elem[1] *= 1.08
	elem[1] = round(elem[1], 2)
print(goods)


# команды
# count_team = int(input("Количество команд: "))
# len_team = int(input("Количество человек в одной команде: "))
# teams = []
# start = 1
# for _ in range(count_team):
# 	teams.append(list(range(start, start + len_team)))
# 	start += len_team
# print(teams)

# вложенный список
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
# 	for col in row:
# 		print(col, end="\t")
# 	print()

# пакеты Мария-ра
# count_packet = int(input("Количество пакетов: "))
# message = []
# error = 0
# for iterate in range(count_packet):
# 	packs = []
# 	print("Итерация ", iterate)
# 	for elem in range(4):
# 		value = int(input("Бибуб Бибоб 1 or 0 or -1"))
# 		packs.append(value)
# 	if packs.count(-1) > 1:
# 		error += 1
# 	else:
# 		message.extend(packs)
# print("Закодированное сообщение:", message)
# print("Ошибок", error)

# вирусам вирус
# text_1 = input("Введите первый текст: ")
# text_2 = input("Введите второе текст: ")
# count_1 = list(text_1).count("?") + list(text_1).count("!")
# count_2 = list(text_2).count("?") + list(text_2).count("!")
# if count_2 < count_1:
# 	print(text_1 + text_2)
# elif count_2 > count_1:
# 	print(text_2 + text_1)
# else:
# 	print("Ой !")

# поглощение
# main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
# first_company = [0, 0, 0]
# second_company = [1, 0, 0, 1, 1]
# third_company = [1, 1, 1, 0, 1]
#
# for var_list in [first_company, second_company, third_company]:
# 	main.extend(var_list)
# print("Всего задач:", main)
# print("Количество невыполненных:", main.count(0))

# Кино сайт
# films = [
# 	"Мимино", "Крепкий орешек", "Пила", "Усатый нянь",
# 	"Один дома", "Горбатая горая", "У холмов есть глаза"
# ]
# my_list = []
#
#
# def check(var_list, value):
# 	for iterate in var_list:
# 		if iterate == value:
# 			return True
# 	return False
#
#
# while True:
# 	print("\nВаши избранные фильмы:\n", my_list)
# 	name_film = input("Введите название: ")
# 	if check(films, name_film):
# 		my_command = input("Пропишите команду: добавить, вставить, удалить:")
# 		if my_command.lower() == "добавить":
# 			if check(my_list, name_film):
# 				print("Уже добавлено")
# 			else:
# 				my_list.append(name_film)
# 		elif my_command.lower() == "вставить":
# 			ind = int(input("Куда:"))
# 			if ind <= len(my_list):
# 				if check(my_list, name_film):
# 					my_list.remove(name_film)
# 					my_list.insert(ind, name_film)
# 				else:
# 					my_list.insert(ind, name_film)
# 			else:
# 				print("Слишком большой индекс")
# 		elif my_command.lower() == "удалить":
# 			if check(my_list, name_film):
# 				my_list.remove(name_film)
# 			else:
# 				print("А такого фильма у вас и нету!")
# 		else:
# 			print("Донт компрендо май френд репит агайн")
# 	else:
# 		print("Такого фильма у нас нет!")




# темные времена
# def check(var_list, value):
# 	for iterate in var_list:
# 		if iterate == value:
# 			return True
# 	return False
#
#
# list_amount = []
# count_worker = int(input("введите количество сотрудников"))
# for _ in range(count_worker):
# 	amount = int(input("Введите зарплату сотрудника: "))
# 	list_amount.append(amount)
# while check(list_amount, 0):
# 	list_amount.remove(0)
# for worker_n in range(len(list_amount)):
# 	print("у сотрудника №", worker_n, "зарплата =", list_amount[worker_n])

# zoo
# zoo = ["Лев", "Кенгуру", "Слон", "Обезьяна"]
# print(zoo)
# zoo.insert(1, "Медведь")
# print(zoo)
# zoo.remove("Слон")
# print(zoo)
# print("Обезьяна сидит в клетки номер:", zoo.index("Обезьяна"))
# print("Лев сидит в клетки номер:", zoo.index("Лев"))
