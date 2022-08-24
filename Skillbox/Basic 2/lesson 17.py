# 10 ЦЕЗАР
# def caesar_code(your_string, reference, shift_num):
# 	code_string = ''
# 	for word in your_string:
# 		if word in reference:
# 			code_word = reference[(reference.find(word) + shift_num) % len(reference)]
# 			code_string += code_word
# 		else:
# 			code_string += word
# 	return code_string
#
#
# word_a = ord('а')
# list_code = ''.join([chr(i) for i in range(word_a, word_a + 6)] + [chr(word_a + 33)] +
# 					[chr(i) for i in range(word_a + 6, word_a + 32)])
# my_text = input("Введите текст: ").lower()
# shift = int(input("Введите сдвиг: "))
# my_text = caesar_code(my_text, list_code, shift)
# print("Зашифрованное сообщение", my_text)

# 9 задание три списка в списке
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# very_nice_list = list(y for item in nice_list for x in item for y in x)
# print(very_nice_list)

# палки
# import random
# count_sticks = int(input("Введите количество палок: "))
# count_throw = int(input("Количество доступных бросков: "))
# table = "|" * count_sticks
# for my_try in range(count_throw):
# 	left_rand = random.randint(1, count_sticks)
# 	right_rand = random.randint(left_rand, count_sticks)
# 	lstr = table[:left_rand-1]
# 	midstr = (right_rand-left_rand+1) * "."
# 	rstr = table[right_rand:]
# 	table = lstr + midstr + rstr
# 	print("{} бросок с {} по {}".format(my_try + 1, left_rand, right_rand))
# print(lstr + midstr + rstr)

# заказ
# my_list = list(list(y for y in range(1 + x, 10 + x, 4)) for x in range(4))
# print(my_list)

# сжатие
# import random
# def_list = list(random.randint(0, 2) for x in range(10))
# zero_list = list(x for x in def_list if x == 0)
# value_list = list(x for x in def_list if x != 0)
# zero_list.extend(value_list)
# print("Исходный массив:{}".format(def_list))
# print("Приведенный массив:", zero_list)

# HH
# def search_hh(my_text):
# 	text = list(my_text)
# 	r_text = list(my_text[::-1])
# 	i1 = text.index("h")
# 	i2 = text.index("h")
# 	new_str = text[:i1] + r_text[i2:len(text) - i2] + text[len(text)-i2:]
# 	print(new_str)
#
#
# my_string = input("Моя строка: ")
# search_hh(my_string)

#  4 задание
# alphabet = 'abcdefg'
# print(alphabet[:])
# print(alphabet[::-1])
# print(alphabet[::2])
# print(alphabet[1::2])
# print(alphabet[:1])
# print(alphabet[:-2:-1])
# print(alphabet[3:4])
# print(alphabet[len(alphabet)-3:])
# print(alphabet[3:5])
# print(alphabet[-3:-5:-1])

# 2 команды со случ
# import random
# team_one = list(random.uniform(5, 10) for _ in range(20))
# team_two = list(random.uniform(5, 10) for _ in range(20))
# win_team = list(team_one[x] if team_one[x] > team_two[x] else team_two[x] for x in range(20))
# print("Команда первая:", team_one)
# print("Команда вторая:", team_two)
# print("Команда победителей: ", win_team)

# N генирация
# num_N = int(input("Введите число: "))
# gen_list = list((1 if x % 2 == 0 else x % 510)for x in range(1, num_N))
# print(gen_list)

# только гласные
# def check_word(var_string):
# 	list_right_words = "ауоыэяюёие"
# 	new_string = []
# 	for word in var_string:
# 		if word in list_right_words:
# 			new_string.append(word)
# 	return new_string
#
#
# your_text = input("Введите ваш текст: ").lower()
# your_text = check_word(your_text)
# print(your_text)
