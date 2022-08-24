# 6
# import os
#
#
# def show_chat():
# 	path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# 	file_name = "chat_data.txt"
# 	try:
# 		with open(path + os.sep + file_name, 'r', encoding='utf-8') as file:
# 			for line in file:
# 				print(line, end="")
# 	except FileNotFoundError:
# 		print("Чат еще не создан(пусто)")
#
#
# def send_message(user_name="", message_text=""):
# 	path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# 	file_name = "chat_data.txt"
# 	with open(path + os.sep + file_name, 'a', encoding='utf-8') as file:
# 		file.write(" ".join((user_name, message_text, '\n')))
#
#
#
#
# name = input("Как вас зовут?")
# while True:
# 	print("Что хотите сделать?\n1) Посмотреть чат\n2) Написать сообщение")
# 	move = input("Напиши 1 или 2:\n")
#
# 	if move == '1':
# 		show_chat()
# 	elif move == '2':
# 		value = input("Напиши сообщение: ")
# 		send_message(name, value)
# 	print()

# 5
# import os
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "calc.txt"
# total_sum = 0
#
#
# def check(cal_string):
# 	value = cal_string.split()
# 	try:
# 		if len(value) != 3:
# 			raise IndexError
# 		if value[1] not in "+-*//%":
# 			raise ("Неизвестная операция")
# 		value[0] = int(value[0])
# 		value[2] = int(value[2])
# 	except ValueError:
# 		print("Не могу преобразовать аргументы в целое число!")
# 		value = new_data()
# 		value = None
# 	except TypeError:
# 		print("Я не знаю такую операцию")
# 		value = None
# 	except IndexError:
# 		print("Неправильное количество аргументов")
# 		value = None
# 	finally:
# 		return value
#
#
# def new_data():
# 	value1 = input("Хотите поправить строку?:")
# 	flag = True
# 	while flag:
# 		if value1.lower() == "да":
# 			value = input("Введите данные 'аргумент операция аргумент'")
# 			strip_string = value.split()
# 			if len(value) != 3:
# 				continue
# 			if strip_string[1] not in "+-*//%":
# 				continue
# 			try:
# 				strip_string[0] = int(strip_string[0])
# 				strip_string[2] = int(strip_string[2])
# 			except Exception as error:
# 				print(error)
# 				continue
# 			return value
# 		elif value1.lower() == "нет":
# 			return None
# 		else:
# 			print("Так да или нет?")
# 			value1 = input("Хотите поправить строку?:")
# 			continue
#
#
#
#
#
# def calculate(cal_list):
# 	answer = 0
# 	if cal_list[1] == "+":
# 		answer = cal_list[0] + cal_list[2]
# 	elif cal_list[1] == "-":
# 		answer = cal_list[0] - cal_list[2]
# 	elif cal_list[1] == "*":
# 		answer = cal_list[0] * cal_list[2]
# 	elif cal_list[1] == "/":
# 		answer = cal_list[0] / cal_list[2]
# 	elif cal_list[1] == "//":
# 		answer = cal_list[0] // cal_list[2]
# 	elif cal_list[1] == "%":
# 		answer = cal_list[0] % cal_list[2]
# 	return answer
#
#
# with open(path + os.sep + name, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		my_string = check(line)
# 		if my_string is not None:
# 			result = calculate(my_string)
# 			total_sum += result
#
# print("Сумма результатов {}".format(total_sum))

# 4
# import os
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "data file.txt"
#
#
# def check(value, path_to_file):
# 	try:
# 		if len(value) != 3:
# 			raise IndexError
# 		if not value[0].isalpha():
# 			raise NameError
# 		if "." not in value[1] or "@" not in value[1]:
# 			raise SyntaxError
# 		if not 10 <= int(value[2]) <= 99:
# 			raise ValueError
# 	except (IndexError, NameError, SyntaxError, ValueError):
# 		with open(path_to_file + os.sep + "data with errors.log", "a", encoding='utf-8') as file:
# 			file.write(" ".join((str(x) for x in value)) + '\n')
# 	else:
# 		with open(path_to_file + os.sep + "data without errors.log", "a", encoding='utf-8') as file:
# 			file.write(" ".join((str(x) for x in value)) + '\n')
#
#
# with open(path + os.sep + name, 'r', encoding='utf-8') as my_file:
# 	for line in my_file:
# 		check(line.split(), path)

# 3
# import os
# import random
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "luck_game.txt"
# luck_int = 777
# user_sum = 0
# try:
# 	while user_sum < luck_int:
# 		if random.randint(1, 17) == 1:
# 			raise BaseException
#
# 		value = int(input("Введите число: "))
# 		with open(path + os.sep + name, 'a', encoding='utf-8') as file:
# 			file.write(str(value) + "\n")
# except BaseException:
# 	print("Упс вам не повезло")

# 2
# import random
# import os
#
#
# def func1(x, y):
# 	try:
# 		y += random.randint(0, 10)
# 		x += random.randint(0, 5)
# 		if y == 0:
# 			raise ZeroDivisionError
# 		return x / y
# 	except ZeroDivisionError:
# 		print("В первой функции y принял нулевое значение")
#
#
# def func2(x, y):
# 	try:
# 		y -= random.randint(0, 10)
# 		x -= random.randint(0, 5)
# 		if x == 0:
# 			raise ZeroDivisionError
# 		return y / x
# 	except ZeroDivisionError:
# 		print("Во второй функции y принял нулевое значение")
#
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "coordinates.txt"
# with open(path + os.sep + name, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		nums_list = line.split()
# 		res1 = func1(int(nums_list[0]), int(nums_list[1]))
# 		res2 = func2(int(nums_list[0]), int(nums_list[1]))
# 		if res2 is not None and res1 is not None:
# 			number = random.randint(0, 100)
# 			my_list = sorted([res1, res2, number])
# 			with open(path + os.sep + 'result.txt', 'a', encoding='utf-8') as result_file:
# 				result_file.write(' '.join((str(x) for x in my_list)) + '\n')

# 1
# import os
#
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "people.txt"
# file_log_name = "errors.log"
# total_symbol = 0
# count_errors = 0
# with open(path + os.sep + name, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		line = line.replace("\n", "")
# 		try:
# 			if len(line) <= 3:
# 				raise BaseException
# 		except BaseException as error:
# 			count_errors += 1
# 			with open(path + os.sep + file_log_name, 'a', encoding='utf-8') as log_file:
# 				log_file.write("{} {}\n".format(error, line))
# 		finally:
# 			total_symbol += len(line)
#
# print("Всего Фамилий меньше 4 символов {}".format(count_errors))
# print("Всего символов {}".format(total_symbol))
