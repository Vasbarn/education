# 6

# 5
# import os
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "words.txt"
# name_log = "errors.log"
# count_poly = 0
#
#
# def is_poly(value):
# 	dict_word = dict()
# 	count_odd = 0
# 	for letter in value:
# 		if dict_word.get(letter):
# 			dict_word[letter] += 1
# 		else:
# 			dict_word[letter] = 1
# 	for item in dict_word.values():
# 		if item % 2 == 1:
# 			count_odd += 1
# 		if count_odd > 1:
# 			return False
# 	return True
#
#
# with open(path + os.sep + name, 'r', encoding='utf-8') as file:
# 	count_palindrome = 0
# 	for line in file:
# 		try:
# 			line = line.replace("\n", "")
# 			if not line.isalpha():
# 				raise ValueError
# 			if is_poly(line):
# 				count_palindrome += 1
# 		except ValueError:
# 			with open(path + os.sep + name_log, 'a', encoding='utf-8') as log_file:
# 				log_file.write(str(line) + " " + str(ValueError) + "\n")
# 			raise
#
# print("В списке {} слов-палиндромов".format(count_palindrome))


# 4
# import os
#
#
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "people.txt"
# total_symbol = 0
# try:
# 	with open(path + os.sep + name, 'r', encoding='utf-8') as file:
# 		for line in file:
# 			line = line.replace("\n", "")
#
# 			if len(line) <= 3:
# 				raise BaseException("Длина строки меньше 3 символов: {}".format(line))
# 			total_symbol += len(line)
# except BaseException:
# 	raise
# finally:
# 	print("Всего символов {}".format(total_symbol))

# 3
# import os
#
#
# my_string = input("Введите строку: ")
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "file.txt"
# try:
# 	try:
# 		with open(path, 'w', encoding='utf-8') as file:
# 			print(file)
# 	except PermissionError as error:
# 		with open(path + os.sep + name, 'w', encoding='utf-8') as file:
# 			try:
# 				my_string = int(my_string)
# 			except ValueError:
# 				print(my_string, "в целое число не превратить")
# 			finally:
# 				try:
# 					file.write(my_string)
# 				except TypeError:
# 					print("Аргумент передаваемый в write() должен быть текстового формата")
# 					file.write(str(my_string))
# except Exception as error:
# 	print("Эта ошибка неожиданная\n", error)
# else:
# 	print("Программа завершена правильно, как планировалось")


# 2
# import os
# path = os.path.abspath(os.sep) + os.path.join('Users', 'мвидео', 'Desktop', "Папка для тестов")
# name = "ages.txt"
# try:
# 	with open(path, 'r', encoding="utf-8") as file:
# 		for line in file:
# 			print(line)
# except PermissionError:
# 	print("Вы попытались передать папку вместо файла")
#
# result = ""
#
# with open(path + os.sep + name, 'r', encoding="utf-8") as file:
# 	for num_line, line in enumerate(file):
# 		try:
# 			result += "{} : {}\n".format(chr(65 + num_line), int(line))
# 		except (ValueError, TypeError):
# 			print(line[:-1], ": Некорректное значение")
#
# if os.path.exists(path + os.sep + "result.txt"):
# 	print("Файл уже существует")
# else:
# 	with open(path + os.sep + "result.txt", 'w', encoding='utf-8') as file:
# 		file.write(result)

# 1
# try:
# 	BRUCE_WILLIS = 42
# 	input_data = input('Введите строку: ')
# 	leeloo = int(input_data[4])
# 	result = BRUCE_WILLIS * leeloo
# 	print(f'- Leeloo Dallas! Multi-pass № {result}!')
# except ValueError:
# 	print("Ошибка значения")
# except IndexError:
# 	print("Ошибка индекса")
# except Exception:
# 	print("Какая-то другая ошибка")

