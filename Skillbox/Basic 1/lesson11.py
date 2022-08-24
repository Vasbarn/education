
# # извращенный макс (так можно было?
# number1 = int(input("Первое число: "))
# number2 = int(input("Второе число: "))
# difference1 = number1 - number2
# difference2 = number2 - number1
# min_value, maxvalue = sorted((number2, number1))
# print("Максимальное число =", maxvalue)
#  уровнение мамама
# import math
# c = float(input("Введите число c: "))
# b = float(input("Введите число b: "))
# a = float(input("Введите число a(!= 0): "))
# while a == 0:
# 	a = float(input("Введите число a(!= 0): "))
#
# # a∙x2+b∙x+c=0
# d = b**2 - 4 * a * c
#
# if d < 0:
# 	print("Корней нет!")
# elif d == 0:
# 	x = -b / (2 * a)
# 	print("Корень = ", x)
# else:
# 	x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
# 	x2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
# 	print(f'Первый корень равен {x1}')
# 	print(f'Второй корень равен {x2}')
# ход конем
#
# x_axis1 = int(float(input("Координаты фигуры по горизонтали: ")) * 10)
# y_axis1 = int(float(input("Координаты фигуры по вертикали: ")) * 10)
# x_axis2 = int(float(input("Координаты хода по горизонтали: ")) * 10)
# y_axis2 = int(float(input("Координаты хода по вертикали: ")) * 10)
# if 0 <= x_axis1 <= 8 and 0 <= y_axis1 <= 8 and 0 <= x_axis2 <= 8 and 0 <= y_axis2 <= 8:
# 	print(f"Конь в ячейки {x_axis1}, {y_axis1} ")
# 	if (abs(abs(x_axis1) - abs(x_axis2)) == 2 and abs(abs(y_axis1) - abs(y_axis2)) == 1) or \
# 		(abs(abs(x_axis1) - abs(x_axis2)) == 1 and abs(abs(y_axis1) - abs(y_axis2)) == 2):
# 		print(f"Ячейка {x_axis2}, {y_axis2} доступна")
# 	else:
# 		print("Координаты некорректны")
# else:
# 	print("Координаты некорректны")

# фарингейт и цельсий кто кого
# t_start = int(input("Минимальная температура: "))
# t_end = int(input("Максимальная температура: "))
# t_step = int(input("Шаг: "))
# if t_start < t_end :
# 	f_const = 32
# 	one_c = 1.8
# 	print("С    F")
# 	for iteration in range(t_start, t_end+1, t_step):
# 		print(iteration, end='\t')
# 		print(int(iteration * one_c + f_const))
# 		if iteration + t_step > t_end:
# 			print(t_end, end='\t')
# 			print(int(t_end * one_c + f_const))
# else:
# 	print("Я не понимаю тебя!")

# Сравнение планет
# from math import pi
# s_earth = 10.8321 * 10**11
# radius = float(input("Введите радиус: "))
# s_search = 4 / 3 * pi * radius**3
# index = s_search / s_earth
# if s_search / s_earth < 1:
# 	print(f"Ваша планет меньше в {format(s_earth / s_search,'.3f')} раз")
# else:
# 	print(f"Ваша планет больше в {format(index,'.3f')} раз")

# # первая десятичная цифра
# my_number = float(input("Ведите вещественное число: "))
# print("Первая цифра после запятой это:", int(my_number * 10 % 10))

# steam attack
# size_file = int(input("Введите размер файла: "))
# speed_internet = int(input("Скорость интернета: "))
# idx = 1
# for size in range(0, size_file + 1):
# 	if (size % speed_internet == 0 or size == size_file) and size != 0:
# 		print(f"Прошла {idx} секунда. Скачено {size} из {size_file} ({format(size / size_file,'.0%')}) ")
# 		idx += 1

# округление усталого аналитика
# import math
# count_number = int(input("Введите количество чисел: "))
# for num in range(count_number):
# 	input_num = float(input("Введите число: "))
# 	if input_num > 0:
# 		input_num = math.ceil(input_num)
# 		print("Ваш X =", input_num, "log(x) =", math.log(input_num))
# 	elif input_num < 0:
# 		input_num = math.floor(input_num)
# 		print("Ваш X =", input_num, "exp**x =", math.log(input_num))
# 	else:
# 		print("Пропустим это сообщение")

# конвектор евро в рубли через доллары
# price = float(input("Введите стоимость в евро: "))
# price *= 1.25 * 60.87
# print("В рублях стоимость составит:", format(price, ".2f"))

# все функции кеши
# import math
#
# my_number = float(input("Введите ваше число: "))
# print(f"Округление вниз {math.floor(my_number)}")
# print(f"Округление вверх {math.ceil(my_number)}")
# print(f"Модуль {abs(my_number)}")
# print(f"Квадратный корень {math.sqrt(my_number)}")
# print(f"Возвести экспоненту в степень {math.exp(my_number)}")
# print(f"Натуральный логарифм числа {math.log(my_number)}")
# print(f"Логарифм числа на основании 2 {math.log2(my_number)}")
# print(f"Логарифм числа на основании 10  {math.log10(my_number)}")
# print(f"Синус числа  {math.log10(my_number)}")   # нужны радианы
# print(f"Косинус числа   {math.log10(my_number)}") # нужны радианы


# радар танков
# import math
#
# distance = float(input("Расстояние до танка: "))
# angle = float(input("Градус поворота: "))
# angle /= 57.2958
# x = math.cos(angle) * distance
# y = math.sin(angle) * distance
# print("Координаты вражеского танка", format(x, ".2f"), format(y, ".2f"))

# герон площадь треугольника
# from math import sqrt
#
# len_a = float(input("Длина стороны А: "))
# len_b = float(input("Длина стороны B: "))
# len_c = float(input("Длина стороны C: "))
# hp = (len_c + len_b + len_a) / 2
# square = sqrt(hp * (hp - len_a) * (hp - len_b) * (hp - len_c))
# print(f"Принт площадь вашего треугольника = {square}")

# шахматная доска
# x_axis = float(input("Координаты по горизонтали: "))
# y_axis = float(input("Координаты по вертикали: "))
# if 0 <= x_axis <= 8 and 0 <= y_axis <= 8:
# 	print(f"Фигура в ячейки {int(x_axis * 10)}, {int(y_axis * 10)} ")
# 	print(f"Сдвиньте ячейки {format((0.05 - x_axis % 0.1) ,'.3f')}, {format((0.05 -y_axis % 0.1), '.3f')} ")
# else:
# 	print("Координаты некорректны")

# космические рейнджеры
# how_CH = int(input("Сколько чатлов: "))
# CR = how_CH / 2200
# print(f"Это {CR} кредитов")
# print(f"Это {int(CR / 0.5)} кораблей")

# индекс массы тела
# growth = float(input("Рост в метрах: "))
# weight = float(input("Вес в кг: "))
# bmi = weight / growth**2
# print(f"Ваш индекс массы тела = {format(bmi, '.2f')}")
# if bmi < 18.5:
# 	print("Недобор")
# elif bmi < 25:
# 	print("Норма")
# elif bmi < 30:
# 	print("Избыток")
# else:
# 	print("Ожирение")

# день рождения
# age = int(input("Возраст: "))
# temperature = float(input("Температура: "))
# sum_gift = 1.5 * age * temperature
# print(f"Сумма подарка {round(sum_gift, 0)}")

# букмекерская
# bid = int(input("Ведите ставку: "))
# coefficient = float(input("Введите коэффициент: "))
# print("Потенциальный выигрыш: ", format(bid * coefficient, ".2f"))