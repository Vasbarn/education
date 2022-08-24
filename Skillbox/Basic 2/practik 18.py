# странный друг
# def format_string(var_string):
# 	str_separate = ".,!?:; "
# 	new_string = ''
# 	value = ""
# 	for word in range(len(var_string)):
# 		if var_string[word] in str_separate:
# 			new_string += value + var_string[word]
# 			value = ""
# 		else:
# 			value = var_string[word] + value
# 	if value != "":
# 		new_string += value
# 	return new_string
#
#
# my_text = input("Введите текст: ")
# new_text = format_string(my_text)
# print(new_text)


# проверка строк
# def check(string1, string2):
# 	if len(string1) == len(string2):
# 		for iterate in range(len(string1)):
# 			var_string = "".join([string2[iterate:len(string2)], string2[:iterate]])
# 			if var_string == string1:
# 				print("Строки равны")
# 				return
# 	print("Строки не равны")
#
#
# str1 = input("Введите первую строку: ").lower()
# str2 = input("Введите вторую строку: ").lower()
# check(str1, str2)

# ip ардес
# def check(list_var):
# 	if len(list_var) != 4:
# 		print("IP-адрес должен состоять из 4 наборов чисел от 0 до 255, разделенных точками")
#
# 	else:
# 		for iterate in list_var:
# 			if iterate.isdigit():
# 				if 0 <= int(iterate) <= 255:
# 					pass
# 				else:
# 					print("Допускаются только цифры от 0 до 255, исправьте ", iterate)
# 					return
# 			else:
# 				print("Допускаются только цифры от 0 до 255, исправьте ", iterate)
# 				return
# 		print("Подключение к {}", format(".".join(list_var)))
#
#
# while True:
# 	ip_address = input("Введите ip-адрес: ").split(".")
# 	check(ip_address)



# кодирование
# def coding(string):
# 	code_str = my_string[0]
# 	word_1 = my_string[0]
# 	num = 1
# 	for word in string[1:]:
# 		if word == word_1:
# 			num += 1
# 		else:
# 			code_str += str(num) + word
# 			word_1 = word
# 			num = 1
# 	code_str += str(num)
# 	return code_str
#
#
# my_string = input("Введите текст: ")
# new_string = coding(my_string)
# print("Закодированная строка ", new_string)

# надежный пароль
# def check (string):
# 	mark1 = False
# 	mark2 = False
# 	num_mark2 = 0
# 	if len(string) > 7:
# 		for word in string:
# 			if word.isupper():
# 				mark1 = True
# 			if word.isdigit():
# 				num_mark2 += 1
# 			if num_mark2 >= 3:
# 				mark2 = True
# 			if mark1 and mark2:
# 				return True
# 	return False
#
#
# while True:
# 	my_text = input()
# 	if check(my_text):
# 		print("Пароль подходит")
# 	else:
# 		print("Пароль не походит")

# заглавные буквы
# my_string = input("Введите текст: ")
# value_string = " ".join(list(x.capitalize() for x in my_string.split()))
# print(value_string)

# самое длинное слово
# value = input("Введите текст: ").split()
# len_value = list(len(x) for x in value)
# print("Самое длинное слово: {}".format(value[len_value.index((max(len_value)))]))
# print("Его длина {} символа".format(max(len_value)))

# парсинг меню
# parsing_string = "утиное филе;фланк-стейк;банановый пирог;плов"
# value_string = ", ".join(parsing_string.split(";"))
# print("Первичная строка:", parsing_string)
# print("Вторичная строка:", value_string)

# exclusion = '@№$%^&*()'
# while True:
# 	my_text = input("Введите название файла: ").lower()
# 	if not my_text[0] in exclusion and (my_text.endswith(".txt") or my_text.endswith(".docx")):
# 		print("Назва@ние походит")
# 	else:
# 		print("Название не походит")
