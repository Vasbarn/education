from collections import defaultdict
"""Суть в том что мы сразу добавляем в словарь значение, как будто ключ уже существует"""
my_list = [
	[1, 2],
	[2, 5],
	[3, 4],
	[1, 27],
	[3, 6],
	[2, 1],
]
total = defaultdict(lambda: [])
for key, value in my_list:
	total[key].append(value)
print(total)

total = defaultdict(int)
for key, value in my_list:
	total[key] += value
print(total)