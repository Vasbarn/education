# 3 слова
# list_word = []
# word_count = [0, 0, 0]
# list_text = []
# for _ in range(3):
# 	my_string = input("Введите слова которое будем считать: ")
# 	list_word.append(my_string)
# text = input("Введите текст: ")
# while text != "end":
# 	list_text.append(text)
# 	for ind in range(3):
# 		if list_word[ind] == text:
# 			word_count[ind] += 1
# 	text = input("Введите текст: ")
# print("Слово", list_word[0], "встречается", word_count[0])
# print("Слово", list_word[1], "встречается", word_count[1])
# print("Слово", list_word[2], "встречается", word_count[2])

# строка и номер символа
# my_list = list(input("Введите строку: "))
# my_index = int(input("Введите номер символа"))
# left_symbol = my_list[my_index - 1]
# right_symbol = my_list[my_index + 1]
# count = 0
# for iterate in [left_symbol, right_symbol]:
# 	if iterate == my_list[my_index]:
# 		count += 1
# print("Символ слева: ", left_symbol)
# print("Символ справа: ", right_symbol)
# if count == 0:
# 	print("Таких же символов нету")
# elif count == 1:
# 	print("Есть равно один такой символ")
# elif count == 2:
# 	print("Есть два таких символа")

# : на ;
# my_string = input("Ведите текст: ")
# my_list = list(my_string)
# for ind, element in enumerate(my_list):
# 	if element == ":":
# 		my_list[ind] = ";"
# 	print(my_list[ind], end="")

# собачий бега
# count_dog = int(input("Количество собак: "))
# list_dog = []
# for num_dog in range(count_dog):
# 	score = int(input("Введите количество очков: "))
# 	list_dog.append(score)
# print(list_dog)
# max_score = max(list_dog)
# min_score = min(list_dog)
# for ind_dog in range(count_dog):
# 	if list_dog[ind_dog] == max_score:
# 		list_dog[ind_dog] = min_score
# 	elif list_dog[ind_dog] == min_score:
# 		list_dog[ind_dog] = max_score
# print(list_dog)

# индексы и кратность
# count_num = int(input("Введите количество чисел: "))
# list_num = []
# for _ in range(count_num):
# 	num = int(input("Введите число: "))
# 	list_num.append(num)
#
# dominator = int(input("Введите кратность: "))
# for num in range(count_num):
# 	if list_num[num] % dominator == 0:
# 		print("Число в списке под номером", num + 1, "равное", list_num[num], "кратно", dominator)

# мин и макс
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
# for _ in range(N):
# 	num = int(input('Очередное число: '))
# 	nums_list.append(num)
# maximum = min(nums_list)
# minimum = max(nums_list)
# print('Максимальное число в списке:', maximum)
# print('Минимальное число в списке:', minimum)

# id сотрудника
# count_workers = int(input("Количество сотрудников: "))
# list_workers = []
# for iterate in range(1, count_workers + 1):
# 	list_workers.append(iterate*10)
# 	print("ID сотрудника", iterate * 10)
# search = int(input("Какой ID ищем?"))
# if search in list_workers:
# 	print("Сотрудник работает")
# else:
# 	print("Такого сотрудника нет")

# простоя задача
# numbers = []
# for num in range(101):
# 	numbers.append(num)
# print(numbers)

# таблица степеней
# numbers = [3, 7, 5]
# while True:
# 	number = int(input('Новое число: '))
# 	numbers.append(number)
# 	print('Текущий список чисел:', numbers)
# 	for i in numbers:
# 		print(i ** 2, i ** 3, i ** 4)
# 		print()