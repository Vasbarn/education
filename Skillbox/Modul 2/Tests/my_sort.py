from random import randint

def my_sort_v1(value):
	if isinstance(value, list):
		flag = True
		while flag:
			flag = False
			for num in range(0, len(value) - 1):
				if value[num] > value[num + 1]:
					value[num], value[num + 1] = value[num + 1], value[num]
					flag = True
		return value
	else:
		raise TypeError("Принимает только список")


def my_sort_v2(value):
	if isinstance(value, list):
		if len(value) <= 1:
			return value
		pivot = value[randint(0, len(value)-1)]
		list_low = []
		list_up = []
		for elem in value:
			if elem > pivot:
				list_up.append(elem)
			elif elem < pivot:
				list_low.append(elem)

		return my_sort_v2(list_low) + [pivot] + my_sort_v2(list_up)
	else:
		raise TypeError("Принимает только список")


def my_sort(value):
	return sorted(set(value))