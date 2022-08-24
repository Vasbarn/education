

# ролики
# def my_sort(var_list):
# 	for item1 in range(1, len(var_list)):
# 		for item0 in range(0, len(var_list)):
# 			if var_list[item0] > var_list[item1]:
# 				var_list[item0], var_list[item1] = var_list[item1], var_list[item0]
#
#
# count_rollers = int(input("Количество роликов"))
# list_rollers = []
# for _ in range(count_rollers):
# 	list_rollers.append(int(input("Размер пары роликов: ")))
# my_sort(list_rollers)
#
# count_people = int(input("Количество людей"))
# list_foot = []
# for _ in range(count_people):
# 	list_foot.append(int(input("Размер ног людей: ")))
# my_sort(list_foot)
#
# count = 0
# for men_n in list_foot:
# 	for boots_n in list_rollers:
# 		if men_n <= boots_n:
# 			list_foot.remove(men_n)
# 			list_rollers.remove(boots_n)
# 			count += 1
# 			break
# print("Счастливчиков,", count)

# списка - не осилил
# def make_list(len_list):
# 	new_list = []
# 	for num in range(1, len_list + 1):
# 		new_list.append(int(input(f"Введите {num} число: ")))
# 	return new_list
#
#
# list1 = make_list(3)
# list2 = make_list(7)
# print("Список первый: ", list1)
# print("Список второй: ", list2)
# list1.extend(list2)
# for element in list1:
# 	pass
#
# print("Итоговый список: ", list1)


# music
# def check(var_list, var_value):
# 	for element in var_list:
# 		if element == var_value:
# 			return True
# 	return False
#
#
# violator_songs = [
# 	['World in My Eyes', 4.86],
# 	['Sweetest Perfection', 4.43],
# 	['Personal Jesus', 4.56],
# 	['Halo', 4.9],
# 	['Waiting for the Night', 6.07],
# 	['Enjoy the Silence', 4.20],
# 	['Policy of Truth', 4.76],
# 	['Blue Dress', 4.29],
# 	['Clean', 5.83]
# ]
# new_track = []
# len_playlist = int(input("Введите количество песен: "))
# list_name = [violator_songs[x][0] for x in range(len(violator_songs))]
# list_dur = [violator_songs[x][1] for x in range(len(violator_songs))]
# total_dur = 0
# for _ in range(len_playlist):
# 	add_song_name = input("Введите название песни: ")
# 	if check(list_name, add_song_name):
# 		dur = list_dur[list_name.index(add_song_name)]
# 		new_track.append([add_song_name, dur])
# 		total_dur += dur
# print("Мой лист", new_track)
# print("длительность:", round(total_dur, 2))

# party in the house
# guests = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
#
#
# def check(var_list, var_value):
# 	for element in var_list:
# 		if element == var_value:
# 			return True
# 	return False
#
#
# while True:
# 	print(f"Сейчас на вечеринке {len(guests)} гостей")
# 	print(guests)
# 	if len(guests) == 0:
# 		print("Вечеринка закончилась, ну и бардак!")
# 	my_text = input("Введите команду").lower()
# 	if my_text == "пора спать":
# 		print("Все легли спать")
# 		break
# 	elif my_text == "пришел":
# 		guest = input("Кто пришел: ")
# 		if len(guests) <= 5:
# 			guests.append(guest)
# 		else:
# 			print("Гость расстроился что у вас так тесно, и решил уйти")
# 	elif my_text == "ушел":
# 		guest = input("Кто ушел: ")
# 		if check(guests, guest):
# 			print(f"Вы попрощались с {guest}")
# 			guests.remove(guest)
# 		else:
# 			print("Вы перепили, и пытаетесь проводить вешалку")

#  магазин
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
# 		['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
#
#
# def how_mach(value, mylist):
# 	total_price = []
# 	for good, price in mylist:
# 		if good == value:
# 			total_price.append(price)
# 	return total_price
#
#
# while True:
# 	select_goods = input("Выберете что-нибудь: ")
# 	data = how_mach(select_goods, shop)
# 	count_goods = len(data)
# 	price_goods = sum(data)
# 	print("\nОстаток товара =", count_goods, "на сумму", price_goods, end="\n")

#  сортировка
# def my_sort(var_list):
# 	for item1 in range(1, len(var_list)):
# 		for item0 in range(0, len(var_list)):
# 			if var_list[item0] > var_list[item1]:
# 				var_list[item0], var_list[item1] = var_list[item1], var_list[item0]
#
#
# class1 = [x for x in range(160, 177, 2)]
# class2 = [x for x in range(162, 181, 3)]
# class1.extend(class2)
# my_sort(class1)
# print(class1)
# Задача 1
# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# a.extend(b)
# print("В перовом списке цифра 5 повторяется", a.count(5), "раза")
# for _ in range(a.count(5)):
# 	a.remove(5)
# a.extend(c)
# print("В перовом списке цифра 5 повторяется", a.count(3), "раза")
# print("Сам список", a)
