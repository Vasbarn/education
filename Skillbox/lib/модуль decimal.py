print(3.31 == 3.30999999999999991)  # тут будет True что проблема в некоторых вычислениях
print(0.00 == 9e-325)
print(0.3 + 0.3 + 0.3 + 0.1)

import random
import decimal

print(decimal.getcontext())  # что можно делать
decimal.getcontext().prec = 50
print(decimal.getcontext())  # задали точность 50 знаков после запятой


def create_long_nums():
	result = []
	for _ in range(10):
		my_str = ""
		for num, _ in enumerate(range(40)):
			if num == 0:
				my_str += str(random.randint(0, 9))
			elif num == 1:
				my_str += "."
			else:
				my_str += str(random.randint(0, 9))
		result.append(my_str)
	return result


def sum_long_num(some_iter):
	sum_float = []
	sum_decimal = []
	mult = 1.23
	for num in some_iter:
		sum_float.append(float(num))
		sum_decimal.append(decimal.Decimal(num))
	print("Сумма по флоту:", sum(sum_float) * mult)
	print("Сумма по decimal:", sum(sum_decimal) * decimal.Decimal(mult))

create_long_nums()
sum_long_num(create_long_nums())


#
def form_muler(x, y):
	return 108 - (815 - 1500 / x) / y


float0 = 4.0
float1 = 4.25
float2 = None
for _ in range(2, 31):
	float2 = form_muler(float0, float1)
	float0, float1 = float1, float2
print("Тридцатый член последовательности равен:", float2)

decimal.getcontext().prec = 35

float0 = decimal.Decimal(4.0)
float1 = decimal.Decimal(4.25)
for _ in range(2, 31):
	float2 = form_muler(float0, float1)
	float0, float1 = float1, float2
print("Тридцатый член последовательности(decimal) равен:", float2)

decimal.getcontext().prec = 50

float0 = decimal.Decimal(4.0)
float1 = decimal.Decimal(4.25)
for _ in range(2, 31):
	float2 = form_muler(float0, float1)
	float0, float1 = float1, float2
print("Тридцатый член последовательности(decimal) равен:", float2)

# округление

num = decimal.Decimal("10.025")

print("Банковский метод:", num.quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_EVEN))
print("Арифметический метод:", num.quantize(decimal.Decimal("1.00"), decimal.ROUND_HALF_UP))
print("Метод обрезания чисел без округления:", num.quantize(decimal.Decimal("1.00"), decimal.ROUND_FLOOR))
