
# lower и нет
# def my_def(string):
# 	count_l = 0
# 	for word in string:
# 		if word.islower():
# 			count_l += 1
# 	if count_l >= len(string) // 2:
# 		return string.lower()
# 	else:
# 		return string.upper()
#
#
# my_text = input("Введите текст: ")
# my_text = my_def

# Проверка пути:
# path = input("Введите путь: ").lower()
# my_disk = input("Введите диск: ").lower()
# my_format = input("Введите формат: ").lower()
# if path.startswith("{}:/".format(my_disk)) and path.endswith(".{}".format(my_format)):
# 	print("Путь верный")
# else:
# 	print("Путь неверный")


# Цезар 2 - считаю первый вариант - удачной реализацией

# шаблон поздравления
# sample = input("Введите шаблон поздравления, обязательно используя {name} вместо имени и {age} вместо возраста:\n")
# list_name = input('Введите имена через ",": ').split(",")
# list_age = input('Введите возраст через ",": ').split(",")
# print(list_age)
# for iterate in range(len(list_age)):
# 	print(sample.format(name=list_name[iterate], age=list_age[iterate]))

# Убрать пробелы
# your_text = input("Введите текст: ").strip()
# your_text = " ".join("Ваш текст: {}".format(your_text).split())
# print(your_text)

# Лингвисты 2
# list_word = list()
# for _ in range(3):
# 	list_word.append(input("Введите слово: "))
# my_text = input("Введите текст: ")
#
# for word in list_word:
# 	print('Слово "{}" встречает "{}" раз'.format(word, my_text.count(word)))

#  ip address
# num = []
# for _ in range(4):
# 	num.append(int(input("Введите число:")))
# print("Ваш ип:{}:{}:{}:{}".format(num[0], num[1], num[2], num[3],))

# Где деньги Лебовский
# my_name = input("Введите имя: ")
# duty = float(input("Сумма долга: "))
#
# print("{0}, где деньги {0} {1} рублей {0}. Где. Мои. {1} рублей".format(my_name, duty))

# заказ
# my_name = input("Ваше имя: ")
# numer_order = int(input("Номер вашего заказ: "))
# print("Здравствуйте, {}! Ваш заказ {} готов".format(my_name, numer_order))

