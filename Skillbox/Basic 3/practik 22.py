# 9
import os
import zipfile

name = "WAR AND PEACE.zip"
name_2 = "anal war and peace.txt"
name_into = "Tolstoyi_L._Shkolnayabibli._Voyina_I_Mir_Tom_1.txt"
path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep
total_word = 0
dict_to_anal = dict()
with zipfile.ZipFile(path_to_file + name, 'r') as zip_into:
	with zip_into.open(name_into, "r" ) as file:
		for line in file:
			value = line.decode('cp1251').lower()
			for symbol in value:
				total_word += 1
				if dict_to_anal.get(symbol):
					dict_to_anal[symbol] += 1
				else:
					dict_to_anal[symbol] = 1

		revers_dict = dict()
		for key, item in dict_to_anal.items():
			if revers_dict.get(item):
				revers_dict[int(item)].append(key)
			else:
				revers_dict[int(item)] = [key]
		total_string = ""
		for key, item in sorted(revers_dict.items(), reverse=True):
			total_string += " ".join([str(key), sorted(item)[0], "\n"])
	with open(path_to_file + name_2, 'w', encoding='utf-8') as file:
		file.write(total_string)


# 8

# import os
# import string
#
# standard = string.ascii_lowercase
# name_1 = "text 2.txt"
# name_2 = "text 2 ANALISE.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep
# dict_to_anal = dict()
# total_word = 0
# with open(path_to_file + name_1, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		for symbol in line:
# 			if symbol in standard:
# 				total_word += 1
# 				if dict_to_anal.get(symbol):
# 					dict_to_anal[symbol] += 1
# 				else:
# 					dict_to_anal[symbol] = 1
# revers_dict = dict()
# for key, item in dict_to_anal.items():
# 	dict_to_anal[key] = round(item / total_word, 3)
# 	if revers_dict.get(item):
# 		revers_dict[item].append(key)
# 	else:
# 		revers_dict[item] = [key]
# total_string = ""
# for key in sorted(revers_dict, reverse=True):
# 	for item in sorted(revers_dict[key]):
# 		total_string += " ".join([str(round(key / total_word, 3)), sorted(item)[0], "\n"])
# print(total_string)
#
# with open( path_to_file + name_2, 'w', encoding='utf-8') as file:
# 	file.write(total_string)


# 7
# import os
#
#
# name_tour1 = "tour 1.txt"
# name_tour2 = "tour 2.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep
# total_list = []
# with open(path_to_file + name_tour1, 'r', encoding="utf-8") as file:
# 	for num, line in enumerate(file):
# 		if num == 0:
# 			score = int(line.strip())
# 		else:
# 			s_name, f_name, p_score = line.split()
# 			if int(p_score) > score:
# 				total_list.append([int(p_score), f_name[0] + ".", s_name])
# 	total_string = ""
# 	total_string += "Всего участников {} \n".format(len(total_list))
# 	for num, item in enumerate(sorted(total_list, reverse=True)):
# 		sc, f_n, s_n = item
# 		total_string += " ".join([str(num + 1) + ")", f_n + s_n, str(sc), "\n"])
#
# with open(path_to_file + name_tour2, 'w', encoding='utf-8') as file:
# 	file.write(total_string)


# 6
# import os
#
#
# def code_cesar(var_string, shift):
# 	secret_string = ""
# 	var_string = var_string.lower()
# 	word_a = ord('а')
# 	list_code = ''.join([chr(i) for i in range(word_a, word_a + 6)] + [chr(word_a + 33)] +
# 						[chr(i) for i in range(word_a + 6, word_a + 32)])
# 	for word in var_string:
# 		if word in list_code:
# 			code_word = list_code[(list_code.find(word) + shift) % len(list_code)]
# 			secret_string += code_word
# 		else:
# 			secret_string += word
# 	return secret_string
#
#
# name = "text.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep + name
#
# with open(path_to_file, "r", encoding='utf-8') as file:
# 	code_text = ""
# 	for num, line in enumerate(file):
# 		code_text += code_cesar(line, num + 1)
# print(code_text)


# 5
# import os
#
# name_file = input("Введите название текстового файла:\n")
# your_path = input("Куда хотите сохранить файл укажите папки путь через пробел:\n")
# full_path = os.path.abspath(os.sep)
# for elem in your_path.split():
# 	full_path = os.path.join(full_path , elem)
# full_path += os.sep
# print(full_path)
# if os.path.exists(full_path):
# 	real_full_name = full_path + name_file
# 	print(real_full_name)
# 	if os.path.exists(real_full_name):
# 		answer = input("Файл уже существует. Вы хотите перезаписать его? (да или нет)\n").lower()
# 		if answer == "да":
# 			with open (real_full_name, 'w', encoding="utf-8") as file:
# 				file.write("данные файла перезапись")
# 	else:
# 		with open(real_full_name, 'w', encoding="utf-8") as file:
# 			file.write("данные файла")
# else:
# 	print("Введен некорректный путь")



# 4
# import os
#
#
# def data_info(path, count_dir=0, count_file=0, size_file=0):
# 	for item in os.listdir(path):
# 		new_path = path + os.sep + item
# 		if os.path.isdir(new_path):
# 			count_dir += 1
# 			count_dir, count_file, size_file = data_info(new_path, count_dir, count_file, size_file)
# 		else:
# 			count_file += 1
# 			size_file += os.path.getsize(new_path)
# 	return count_dir, count_file, size_file
#
#
# my_path = os.path.abspath("..")
# count_dis, count_files, size_file = data_info(my_path)
# size_file =round(size_file / 1024, 2)
# print("Количество папок: {} \nКоличество файлов: {} \nРазмеры файлов: {}".format(count_dis, count_files, size_file))


# 3
# import os
#
# name = "zen.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep + name
# with open(path_to_file, 'r', encoding='utf-8') as file:
# 	count_row = 0
# 	count_word = 0
# 	count_letter = 0
# 	dict_letter = dict()
# 	for line in file:
# 		count_row += 1
# 		line_list = line.replace("/n", " ").replace(".", "").replace(",", "").replace("'", "").replace("-", "")\
# 			.replace("!", "").replace("*", "").split()
# 		count_word += len(line_list)
# 		for word in line_list:
# 			count_letter += len(word)
# 			for letter in word:
# 				symbol = letter.lower()
# 				if dict_letter.get(symbol):
# 					dict_letter[symbol] = dict_letter[symbol] + 1
# 				else:
# 					dict_letter[symbol] = 1
# print("Количество строк {} \n Количество слов {} \n Количество букв {}".format(count_row, count_word, count_letter))
# revers_dict = dict()
# for key, item in dict_letter.items():
# 	if revers_dict.get(item):
# 		revers_dict[item].append(key)
# 	else:
# 		revers_dict[item] = [key]
#
# min_value = revers_dict[min(revers_dict)][0]
# print("Самая редкая буква", min_value)
# 2
# import os
#
# name = "zen.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep + name
# with open(path_to_file, 'r', encoding='utf-8') as file:
# 	for line in reversed(file.readlines()):
# 		if line != "\n":
# 			print(line, end="")



# 1
# import os
# name = "numbers.txt"
# path_to_file = os.path.abspath(os.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + os.sep + name
# value = 0
# with open(path_to_file, 'r', encoding='utf-8') as file:
# 	for line in file:
# 		data = line.replace("\t", " ").replace("\n", " ").split()
# 		value += sum([int(x) for x in data])
# print(value)

