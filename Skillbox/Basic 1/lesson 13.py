#

# спейсX - не осилил

# амплитуда мячика
# initial_amplitude = float(input("Введите начальную амплитуду: "))
# end_amplitude = float(input("Введите конец амплитуды: "))
# iterate = 0
# while initial_amplitude - initial_amplitude * 0.084 > end_amplitude:
# 	iterate += 1
#
# 	initial_amplitude -= initial_amplitude * 0.084
# print("Потребует ", iterate + 1, "итераций до полной остановки")

# переработка программы
# def len_number(num):
# 	iterate = 0
# 	while num // 10 != 0:
# 		num //= 10
# 		iterate += 1
# 	return iterate
#
#
# def half_reverse(num):
# 	len_num = len_number(num)
# 	mid_word = ""
# 	iterate = 0
# 	if len_num > 1:
# 		for word in str(num):
# 			if iterate == len_num:
# 				end_word = word
# 			elif iterate == 0:
# 				start_word = word
# 			else:
# 				mid_word += word
# 			iterate += 1
# 		return int(end_word + mid_word + start_word)
# 	else:
# 		return num
#
#
# def check(num, my_len):
# 	while len_number(num) < my_len - 1:
# 		print("Количество цифр в числе должно быть не меньше", my_len)
# 		num = int(input("Введите число: "))
# 	return num
#
#
# num1 = check(int(input("Введите первое число: ")), 3)
# num2 = check(int(input("Введите второе число: ")), 4)
# r_num1 = half_reverse(num1)
# r_num2 = half_reverse(num2)
# print("Первое отредактированное число =", r_num1)
# print("Второе отредактированное число =", r_num2)
# print("Сумма =", r_num1 + r_num2)

# Информатика 3
# def change_format(num):
# 	degree = 0
# 	while num > 10:
# 		degree += 1
# 		num /= 10
# 	while num < 1:
# 		degree -= 1
# 		num *= 10
#
# 	return num, degree
#
#
# my_num = float(input("Введите число: "))
# my_mantis, my_degree = change_format(my_num)
# print("Мантисcа =", my_mantis)
# print("Порядок =", my_degree)

# перевертыш 2
# def reverse_sting(string):
# 	string = str(string)
# 	reverse_str = ""
# 	for word in string:
# 		reverse_str = word + reverse_str
# 	return int(reverse_str)
#
#
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# sum1 = num1 + num2
# num1 = reverse_sting(num1)
# num2 = reverse_sting(num2)
# sum2 = num1 + num2
# print("Первое число наоборот =", num1)
# print("Второе число наоборот =", num2)
# print("Сумма перевертышей =", sum2)
# print("Сумма ваших =", sum1)

# максимум из трех чисел
# def duo_max(num1, num2):
# 	if num1 > num2:
# 		return num1
# 	elif num2 > num1:
# 		return num2
# 	else:
# 		return None
#
#
# numer_1 = int(input("Введите первое число: "))
# numer_2 = int(input("Введите второе число: "))
# numer_1 = duo_max(numer_1, numer_2)
# numer_2 = int(input("Введите третье число: "))
# maxim = duo_max(numer_1, numer_2)
# print("Максимальное число =", maxim)

# Информатика 2
# def change_format(num):
# 	degree = 0
# 	while num > 10:
# 		degree += 1
# 		num /= 10
# 	while num < 1:
# 		degree -= 1
# 		num *= 10
# 	num = str(num) + " * 10 ** " + str(degree)
# 	return num
#
#
# my_num = float(input("Введите число: "))
# my_num = change_format(my_num)
# print("В формате плавающий точки это будет:", my_num)

##
# Практика
##

# float сравнение 2
# def comparison(num_1, num_2, sum1_2):
# 	if abs((num_1 + num_2) - sum1_2) < 1e-15:
# 		print("Верно")
# 	else:
# 		print("Неверно")
#
#
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите втрое число: "))
# num3 = float(input("Сумма этих двух чисел: "))
# comparison(num1, num2, num3)

# float сравнение
# def comparison(num1, num2):
# 	if abs(num1 + num2) == abs(num1 + 1e-15) or abs(num1 + num2) == abs(num2 + 1e-15):
# 		print("Бюджет не изменится")
# 	else:
# 		print("Бюджет изменится")
#
#
# budget_country = float(input("Введите бюджет странны: "))
# movement = float(input("Введите суммы операции: "))
# comparison(budget_country, movement)

# 1 больше 2
# def count_iterate(num):
# 	mark = 2
# 	iterate = 0
# 	start = 1
# 	while start <= mark:
# 		iterate += 1
# 		start += num
# 	print("Через ", iterate, "итерации число станет  больше", mark)
#
#
# strange_num = float(input("Введите число в экспоненциальной форме: "))
# count_iterate(strange_num)

# число в плавающую точку
# def change_format(num):
# 	degree = 0
# 	while num > 10:
# 		degree += 1
# 		num /= 10
# 	num = str(num) + " * 10 ** " + str(degree)
# 	return num
#
#
# my_num = int(input("Введите число: "))
# my_num = change_format(my_num)
# print("В формате плавающий точки это будет:", my_num)

# вещественная хуета е1
# num = 1
# iterate = 0
# while num / 2 != 0:
# 	iterate += 1
# 	num /= 2
# 	print(f"Итерация {iterate}: результат {num}")


# Приоритет
# def numeral_count(num):
# 	count_num = 1
# 	if num >= 0:
# 		while num // 10 != 0:
# 			count_num += 1
# 			num = num // 10
# 	else:
# 		count_num = 0
# 	return count_num
#
#
# count_task = int(input("Введите количество задач: "))
# priority, num_p = 0, 0
# for iterate in range(count_task):
# 	numer = int(input("Введите номер задачи: "))
# 	value = numeral_count(numer)
# 	if value > num_p:
# 		priority = numer
# 		num_p = value
# print(f"Самая приоритетная задача {priority} ")

# Назад в будущее gcd 2123w21313
# def my_gcd(num1, num2):
# 	if num1 > num2:
# 		maxim = num1
# 		minim = num2
# 	else:
# 		maxim = num2
# 		minim = num1
# 	while maxim % minim != 0:
# 		maxim = maxim % minim
# 		maxim, minim = minim, maxim
# 	return minim
#
#
# val1 = int(input("Введите первое число:"))
# val2 = int(input("Введите второе число:"))
# print(my_gcd(val1, val2))

# N от N
# def sum_n(numer):
# 	total_sum = 0
# 	for iterate in range(1, numer + 1):
# 		total_sum += iterate
# 	return total_sum
#
#
# your_num = int(input("Введите число: "))
# val_1 = sum_n(your_num)
# val_2 = sum_n(val_1)
# print(f"Сумма от {1} до {your_num} равна {val_1}")
# print(f"Сумма от {1} до {val_1} равна {val_2}")
