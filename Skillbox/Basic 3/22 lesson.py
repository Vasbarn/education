# 9
# import os
#
#
# def into_search(path, new_data=None):
# 	if new_data is None:
# 		new_data = ""
# 	for item in os.listdir(path):
# 		new_path = path + os.path.sep + item
# 		if os.path.isdir(new_path):
# 			new_data = into_search(new_path, new_data)
# 		else:
# 			with open(new_path, 'r', encoding='utf-8') as file:
# 				for line in file:
# 					new_data += line
# 				new_data += "\n" + "*" * 40 + "\n"
# 	return new_data
#
#
# my_path = os.path.abspath(os.path.join(".."))
# new_file = into_search(my_path)
#
# path_to_save = os.path.abspath(os.path.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов") + \
# 				os.path.sep + "ALL SCRIPT.txt"
# with open(path_to_save, "w", encoding='utf-8') as file:
# 	file.write(new_file)

# 8
# import os
#
#
# path_to_dir = os.path.abspath(os.path.sep) + os.path.join("Users", "мвидео", "Desktop", "Папка для тестов", )
# + os.path.sep
# name_file = "numbers.txt"
#
# with open(path_to_dir + name_file, 'r', encoding='utf-8') as file:
# 	total_sum = 0
# 	for line in file:
# 		total_sum += int(line)
#
# with open(path_to_dir + "answer.txt", "w") as file:
# 	file.write(str(total_sum))

# 7
# import os
# import random
#
#
# def search_file(path, value, result=None):
# 	if result is None:
# 		result = []
# 	if os.path.isdir:
# 		for elem in os.listdir(path):
# 			full_name = os.path.join(path, elem)
# 			if os.path.isdir(full_name):
# 				search_file(full_name, value, result)
# 			elif os.path.isfile(full_name):
# 				if elem.find(value) >= 0:
# 					result.append(full_name)
# 	return result
#
#
# my_path = os.path.abspath("..")
# name_file = "practik"
# list_file = search_file(my_path, name_file)
#
#
# for item in list_file:
# 	print(item)
#
#
# with open(list_file[random.randint(0, len(list_file)-1)], 'r') as file:
# 	for line in file:
# 		print(line, end="")

# 6
# import os

# path1 = os.path.abspath(os.path.sep) + os.path.join("task", "group 1.txt")
# path2 = os.path.abspath(os.path.sep) + os.path.join("task", "Additional info", "group 2.txt")
#
#
# summa = 0
# diff = 0
# with open(path1, 'r', encoding="utf-8") as file:
# 	for i_line in file:
# 		value = i_line.split()[2]
# 		summa += int(value)
# 		diff -= int(value)
#
# pred = 1
# with open(path2, 'r', encoding="utf-8") as file:
# 	for i_line in file:
# 		value = i_line.split()[2]
# 		pred *= int(value)
#
# print(summa)
# print(diff)
# print(pred)


# file_2 = open('E:\task\group_2.txt', 'read')
# compose = 0
# for i_line in file:
# 	info = i_line.split()
# 	compose *= info[2]
# print(summa)
# print(diff)
# print(compose)

# 5
# import os
#
#
# def search_file(path, value, result=None):
# 	if result is None:
# 		result = []
# 	if os.path.isdir:
# 		for elem in os.listdir(path):
# 			full_name = os.path.join(path, elem)
# 			if os.path.isdir(full_name):
# 				search_file(full_name, value, result)
# 			elif os.path.isfile(full_name):
# 				if elem.find(value) >= 0:
# 					result.append(full_name)
# 	return result
#
#
# my_path = os.path.abspath("..")
# name_file = "practik"
# list_file = search_file(my_path, name_file)
#
# for item in list_file:
# 	print(item)

# 4
# import os
#
#
# def testy(path):
# 	if os.path.exists(path):
# 		if os.path.isdir(path):
# 			print("Это папка")
# 		if os.path.isfile(path):
# 			print("Это файл")
# 			print("Его размер", os.path.getsize(path))
# 	else:
# 		print("По такому пути ничего нет!")
#
#
# path1 = os.path.abspath('')
# testy(path1)


# 3
# import os
#
# path = os.path.abspath(os.path.sep)
# print(path)

# 2
# import os
#
# path = os.path.abspath(os.path.join("..", "Basic 1"))
# print("Папка {} содержит следующие файлы: ".format(path))
# for file in os.listdir(path):
# 	print("   ", file)

# 1
# import os
#
# abs_path = os.path.abspath(os.path.join("access", "admin.bat"))
# no_abs_path = os.path.join(os.path.sep, "Basic 3", "access", "admin.bat")
# print(abs_path)
# print(no_abs_path)
