
# яма
# number = int(input("Введите число: "))
# step = number + 1
# for x_axis in range(1, number + 1):
# 	for y_axis in range(1, number + 1):
# 		if x_axis >= y_axis:
# 			print(step - y_axis, end="")
# 		else:
# 			print(".", end="")
# 	for y_axis in range(number, 0, -1):
# 		if x_axis >= y_axis:
# 			print(step - y_axis, end="")
# 		else:
# 			print(".", end="")
# 	print()

#  треугольник с нечетным
# height = int(input("Высота пирамиды: "))
# start = height
# step = 0
# number = 1
# for x_axis in range(1, height + 1):
# 	for y_axis in range(1, height**2):
# 		if start - step <= y_axis <= start + step:
# 			if y_axis % 2 == 1:
# 				print(number, end="\t")
# 				number += 2
# 			else:
# 				print("", end="\t")
# 		else:
# 			print("", end="\t")
# 	step += 1
# 	print()



# равнобедренный треугольник
# height = int(input("Высота пирамиды: "))
# start = height
# step = 0
# for x_axis in range(1, height + 1):
# 	for y_axis in range(1, height**2):
# 		if start - step <= y_axis <= start + step:
# 			print("#", end="\t")
#
# 		else:
# 			print("", end="\t")
# 	step += 1
# 	print()


# сумма чисел наибольшего числа
# my_number = input("Введите числа: ") + " "
# max_number = "0"
# var_number = ""
# my_sum = 0
# for number in my_number:
# 	if number != " ":
# 		var_number += number
# 	else:
# 		if int(var_number) > int(max_number):
# 			max_number = var_number
# 		var_number = ""
#
# for number in max_number:
# 	my_sum += int(number)
# print("Максимальное число: ", max_number, "сумма цифр этого числа равна", my_sum)


# сумма факториалов
# number_n = int(input("Введите число: "))
# sum_1 = 0
# for num1 in range(1, number_n + 1):
# 	sum_2 = 1
# 	for num2 in range(1, num1 + 1):
# 		sum_2 = sum_2 * num2
# 	sum_1 += sum_2
# print("Ответ ", sum_1)

# количество простых

# count_number = int(input("Сколько будет чисел: "))
# total = 0
# for num in range(1, count_number + 1):
# 	print(num, end=" ")
# 	value_num = int(input("Введите число: "))
# 	count = 0
# 	for number in range(2, value_num + 1):
# 		if value_num % number == 0:
# 			count += 1
# 	if count == 1:
# 		total += 1
# print("Из", count_number, "чисел", total, "простых")

# иск
# square_size = int(input("Введите размер шрифта: "))
# for x_axis in range(square_size):
# 	for y_axis in range(square_size):
# 		if y_axis == x_axis or x_axis + y_axis == square_size - 1:
# 			print("^", end="\t")
# 		else:
# 			print(" ", end="\t")
# 	print()

# рамка

# len_x_axis = int(input("Введите высоту: "))
# len_y_axis = int(input("Введите ширину: "))
# for x_axis in range(len_x_axis):
# 	for y_axis in range(len_y_axis):
# 		if x_axis == 0 or x_axis == len_x_axis - 1:
# 			if y_axis == 0 or y_axis == len_y_axis - 1:
# 				print("|", end="")
# 			else:
# 				print("-", end="")
# 		elif y_axis == 0 or y_axis == len_y_axis - 1:
# 			print("|", end="")
# 		else:
# 			print(" ", end="")
# 	print()


# лестица из цифр
# my_num = int(input("Введите ваше число: "))
# start = 0
# for step1 in range(my_num + 1):
# 	for step2 in range(start, my_num + 1):
# 		print(step2, end="\t")
# 	start += 1
# 	print()

# больше пяти
# my_number = input("Ведите любое число из любого количество цифр: ")
# count = 0
# for num in my_number:
# 	if int(num) > 5:
# 		count += 1
# print("В последовательности количество цифр больше 5 =", count)

# очередь
# queue_length = int(input("Количество человек в очереди: "))
# start = 0
# for hour in range(queue_length):
# 	print(hour, "час. Номера клиентов в очереди:", end=" ")
# 	for men in range(start, queue_length):
# 		print(men, end=" ")
# 	start += 1
# 	print()

# матрица
#
# matrix = int(input("Введите размер матрицы: "))
# for x_axis in range(matrix):
# 	for y_axis in range(matrix):
# 		if y_axis + x_axis == matrix - 1:
# 			print(1, end="\t")
# 		elif y_axis + x_axis < matrix - 1:
# 			print(0, end="\t")
# 		else:
# 			print(2, end="\t")
# 	print()

# дорога
# field = int(input("Введите размер поля: "))
# len_x_axis = field // 3
# len_y_axis = field
# y_cont1 = len_y_axis // 2 + 2
# y_cont2 = len_y_axis // 2 - 3
# for x_axis in range(len_x_axis + 1):
# 	for y_axis in range(len_y_axis + 1):
# 		if y_axis == (len_y_axis // 2) and x_axis != len_x_axis // 2:
# 			print("|", end="")
# 		elif x_axis != len_x_axis // 2:
# 			print(" ", end="")
# 		else:
# 			print("-", end="")
# 		if y_axis == y_cont2 and x_axis != len_x_axis // 2:
# 			print("/", end="")
# 		if y_axis == y_cont1 and x_axis != len_x_axis // 2:
# 			print("\\", end="")
# 	y_cont2 -= 1
# 	y_cont1 += 1
# 	print()


# ворота
# len_x_axis = int(input("Введите высоту: "))
# len_y_axis = int(input("Введите ширину: "))
# for x_axis in range(len_x_axis):
# 	for y_axis in range(len_y_axis):
# 		if x_axis == 0:
# 			print("-", end="")
# 		elif y_axis == 0 or y_axis == len_y_axis - 1:
# 			print("|", end="")
# 		else:
# 			print(" ", end="")
# 	print()

# ось
# field = int(input("Введите размер поля: "))
# for x_axis in range(field // 2):
# 	for y_axis in range(field):
# 		if y_axis == (field // 2) and x_axis != field // 2 // 2:
# 			print("|", end="")
# 		elif x_axis != field // 2 // 2:
# 			print(" ", end="")
# 		else:
# 			print("-", end="")
# 	print()

# автомат на зачете
# size_matrix = int(input("Введите размер матрица: "))
# for x_axis in range(1, size_matrix + 1):
# 	for y_axis in range(1, size_matrix + 1):
# 		if y_axis % 3 == 0:
# 			print(y_axis, end='\t')
# 		else:
# 			print(x_axis, end='\t')
# 	print()


# if во вложенных циклах
# n_num = int(input("Введите число N: "))
# for num_x in range(1, n_num + 1):
# 	for num_y in range(1, n_num + 1):
# 		if num_x % 2 == 1:
# 			print(num_y, end="\t")
# 		else:
# 			print(num_x, end="\t")
# 	print()

# опредить алгоримт по видду
#
# for num1 in range(10):
# 	for num2 in range(0, -10, -1):
# 		print(num2 + num1, end="\t")
# 	print()
# сумма числе от 1 до н
#
# my_n = int(input("Введите число: "))
# for x_axis in range(0, my_n + 1):
# 	print(x_axis, end="\t")
# 	for y_axis in range(1, my_n + 1):
# 		print(y_axis + x_axis, end="\t")
# 	print()


# таблица умножения
# for x_axis in range(1, 10):
# 	for y_axis in range(1, 10):
# 		print(x_axis * y_axis, end="\t")
# 	print()
