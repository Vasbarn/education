"""
Используя функцию reduce, реализуйте код, который считает, сколько раз слово was встречается в списке:



sentences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic", "because
her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic", "or had been"]

"""
from functools import reduce


entences = ["Nory was a Catholic", "because her mother was a Catholic", "and Nory’s mother was a Catholic",
			"because her father was a Catholic", "and her father was a Catholic", "because his mother was a Catholic",
			"or had been"]

# TODO то тебе надо редьюс, не хочу два аргумента передовать
def serch_was(value: str):
	serch = "was"
	count = 0
	start_row = 0
	while True:
		if value[start_row:start_row +len(serch)].lower() == serch:
			count += 1
		start_row += 1
		if start_row + len(serch) > len(value):
			break
	return count

result = reduce(serch_was, entences)
print(entences)