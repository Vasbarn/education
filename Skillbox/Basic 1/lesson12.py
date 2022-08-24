# функция
# def rock_paper_scissors(hand):
# 	hand = int(hand)
# 	my_hand = 2 # ножницы
# 	if hand == 1:
# 		# камень
# 		print("Выш камень выиграл!")
# 	elif hand == 2:
# 		# ножницы
# 		print("Ничья")
# 	elif hand == 3:
# 		# бумага
# 		print("Ваша бумага проиграла!")
# 	else:
# 		print("Не жульничать!")
#
#
# def guess_the_number(num):
# 	num = int(num)
# 	my_num = 69
# 	while num != my_num:
# 		if num < my_num:
# 			print("Не угадал попробуй больше ")
# 			num = int(input("Угадай число: "))
#
# 		elif num > my_num:
# 			print("Не угадал попробуй меньше ")
# 			num = int(input("Угадай число: "))
#
# 		else:
# 			print("Не жульничать!")
# 			num = int(input("Угадай число: "))
#
# 	print("Угадал")
#
#
#
# def main_menu(variant):
# 	# Здесь главное меню игры
# 	if variant == 1:
# 		num = int(input("Выберите камень(1), ножницы(2), бумагу(3): "))
# 		rock_paper_scissors(num)
# 	elif variant == 2:
# 		num = int(input("Угадай число: "))
# 		guess_the_number(num)
#
#
# while True:
# 	init = int(input("Выберите игру: 1 - КНБ и 2 - УЧ"))
# 	main_menu(init)


# нод
# def	nod(numer1, numer2):
# 	minim = min(numer1, numer2)
# 	maxim = max(numer1, numer2)
# 	for iter1 in range(maxim, 0, -1):
# 		if maxim % iter1 == 0 and minim % iter1 == 0:
# 			print("НОД =", iter1)
# 			break
#
#
# num1 = int(input("Первое число: "))
# num2 = int(input("Второе число: "))
# nod(num1, num2)
# минимальный извращенец
# number1 = int(input("Первое число: "))
# number2 = int(input("Второе число: "))
# difference1 = number1 - number2
# difference2 = number2 - number1
# min_value, maxvalue = sorted((number2, number1))
# print("Максимальное число =", min_value)

# металлоискатель
# def search_money(x, y):
# 	if -1 <= x <= 1 and -1 <= y <= 1:
# 		print("Монетка где-то рядом.")
# 	else:
# 		print("Нет монет!")
#
#
# while True:
# 	x_xis = float(input("Введите координату X"))
# 	y_xis = float(input("Введите координату Y"))
# 	search_money(x_xis, y_xis)


# поиск цифр и букв в слове
# def search_something(my_string, num, word):
# 	count_num = 0
# 	count_word = 0
# 	for element in str(my_string).lower():
# 		if element in word:
# 			count_word += 1
# 		elif element in num:
# 			count_num += 1
# 	print("В вашем слове:\n", count_num, "цифр", num, "\n", count_word, "буквы", word)
#
#
# while True:
# 	my_text = input("Напишите ваш текст: ")
# 	my_word = input("Напишите вашу букву: ")
# 	my_num = input("Напишите вашу цифру: ")
# 	search_something(my_text, my_num, my_word)

# число наоборот
# def revers(string):
# 	revers_string = ""
# 	for word in str(string):
# 		revers_string = word + revers_string
# 	print("Обратное", int(revers_string))
#
#
# while True:
# 	my_string = int(input("Правильное число: "))
# 	revers(my_string)

# мой калькулятор
# def my_sum(string):
# 	total_sum = 0
# 	for word in str(string):
# 		total_sum += int(word)
# 	print("Сумма цифр вашего числа =", total_sum)
#
#
# def my_min(string):
# 	minim = 99**99
# 	for word in str(string):
# 		if int(word) < minim:
# 			minim = int(word)
# 	print("Минимальная цифра в вашем числе это:", minim)
#
#
# def my_max(string):
# 	maxim = 0
# 	for word in str(string):
# 		if int(word) > maxim:
# 			maxim = int(word)
# 	print("Максимальная цифра в вашем числе это:", maxim)
#
#
# while True:
# 	my_num = input("Введите число: ")
# 	action = int(input("Что сделать: 1 - сумма цифр, 2 - минимальная цифра числа, 3 - максимальная цифра числа"))
# 	if action == 1:
# 		my_sum(my_num)
# 	elif action == 2:
# 		my_min(my_num)
# 	elif action == 3:
# 		my_max(my_num)
# 	else:
# 		print("Пропустил")


# test()
# def negative():
# 	print("Отрицательный")
#
#
# def positive():
# 	print("Положительный")
#
#
# def test():
# 	new_num = int(input("Введите число: "))
# 	if new_num > 0:
# 		positive()
# 	elif new_num < 0:
# 		negative()
#
#
# test()

# функция сумма н
# def summa_n(value):
# 	total_sum = 0
# 	for num in range(1, value+1):
# 		total_sum += num
# 	print("Я знаю, что сумма от 1 до", value, "равна", total_sum)
#
#
# your_num = int(input("Введите число: "))
# summa_n(your_num)

# GPS навигатор
# import math
#
#
# def distance(x_1, y_1, x_2, y_2):
# 	var_dist = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
# 	print("Это расстояние равно ", var_dist)
#
#
# text_value = int(input("Какое расстояние будет мерить.\n"
# 					"От вас до объекта(0) или расстояние между двумя точками(1)?"))
# if text_value == 0:
# 	x1 = 0
# 	y1 = 0
# 	x2 = float(input("Координата X второй точки: "))
# 	y2 = float(input("Координата Y второй точки: "))
# elif text_value == 1:
# 	x1 = float(input("Координата X первой точки: "))
# 	y1 = float(input("Координата Y первой точки: "))
# 	x2 = float(input("Координата X второй точки: "))
# 	y2 = float(input("Координата Y второй точки: "))
# else:
# 	print("Ошибаться в нашем деле нельзя!")
# distance(x1, y1, x2, y2)




# N просто или нет
# def is_prime(value):
# 	count = 0
# 	for iteration in range(2, value + 1):
# 		if value % iteration == 0:
# 			count += 1
# 	if count > 1:
# 		print(f"Число {value} непростое!")
# 	else:
# 		print(f"Число {value} простое!")
#
#
# while True:
# 	my_num = int(input("Введите значение: "))
# 	is_prime(my_num)

# Планеты
# from math import pi
#
#
# def square_planet(value):
# 	square = 4 * pi * value ** 2
# 	print("Площадь планеты =", square)
#
#
# def volume_planet(value):
# 	volume = 4 / 3 * pi * value ** 3
# 	print("Объем =", volume)
#
#
# radius = float(input("Введите радиус планеты: "))
# square_planet(radius)
# volume_planet(radius)

# вода
# def clear_w(price):
# 	print("Название: КлирВоде")
# 	print("Производитель: КлирВодеКорп")
# 	print("Цена:", price)
# 	print()
#
#
# clear_w(55)
# clear_w(20)
# clear_w(99)


# почти
# def my_data():
# 	print("Фамилия:", "Иванов")
# 	print("Имя:", "Василий")
# 	print("Улица:", "Пушкина")
# 	print("Дом:", 32)
# 	print()
#
#
# my_data()
# my_data()
# my_data()

# гос компания
# def how_mach():
# 	a = int(input())
# 	b = int(input())
# 	print("Всего", a+b, "шт.")
#
# print("Сколько мешков рыбы и мяса?")
# how_mach()
# print("Сколько буханок белого и чёрного хлеба?")
# how_mach()
# print("Сколько вёдер воды и молока?")
# how_mach()

