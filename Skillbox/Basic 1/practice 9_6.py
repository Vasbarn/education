# сендвич
"""
'дешифроватор'
my_word = input("Напишите слово: ")
num_letter = 1
f_half = ""
e_half = ""
for letter in my_word:
	if num_letter % 2 == 1:
		f_half += letter
	else:
		e_half = letter + e_half
	num_letter += 1
print("Ваше слово: " + f_half + e_half)
"""


	# молоко вдвойне вкусней!
'''
input_string = input("Введите строку длиной 10 букв из символов a и b: ")
performance = 2
performance_per_day = 0
for letter in input_string:
	if letter.lower() == "b":
		performance_per_day += performance
	performance += 2
print("За день произведено", performance_per_day,"литров молока"
'''

# колонтитул
'''
max_len_string = int(input("Длина строки: "))
importance_level = int(input("Уровень важности: "))
half = (max_len_string - importance_level) // 2
if (max_len_string - importance_level) % 2 == 1:
	print('~' * half + "!" * importance_level + '~' * (half+1))
else:
	print('~' * half + "!" * importance_level + '~' * half)
'''


'''
# самое длинное слово
my_word = input("Напиши сюда любой текст:")
max_l = 0
my_len = 0
for letter in my_word:
	if letter == " ":
		my_len = 0
	else:
		my_len += 1
		if max_l < my_len:
			max_l = my_len
print("Самое сдлинное слово состоит из", max_l, "букв")
'''
# шифрованная s
'''
encrypted_string = input("Напишите шифр: ")
max_s = 0
my_len = 0
for letter in encrypted_string:
	if letter.lower() == "s":
		my_len += 1
		if max_s < my_len:
			max_s = my_len
	else:
		my_len = 0
print("Номер буквы",max_s)
'''

# марсоход
"""
room_length = int(input("Введите длину комнаты: "))
room_width = int(input("Введите ширину комнаты: "))
x = room_length // 2 + 1
y = room_width // 2
print("Марсоход опустился на координаты:", x, ",", y)
while True:
	command = input("Управляй на WASD: ")
	if command == "W" or command == "w" and x < room_length:
		x += 1
	elif command == "A" or command == "a" and y > 1:
		y -= 1
	elif command == "S" or command == "s" and x > 1:
		x -= 1
	elif command == "D" or command == "d" and y < room_width:
		y += 1
	print("Координаты марсохода: X = ", x, "Y = ", y)
"""
