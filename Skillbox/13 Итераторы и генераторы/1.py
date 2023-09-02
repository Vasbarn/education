
# 1

from collections.abc import Iterable
class MySqr:
	def __init__(self, max_bound: int):
		self.__max_bound = max_bound
		self.__counter = 0

	def __iter__(self) -> Iterable[int]:
		self.__counter = 0
		return self

	def __next__(self) -> int:
		self.__counter += 1
		if self.__counter > self.__max_bound:
			raise StopIteration
		return self.__counter ** 2


def gen_my(nums: int) -> Iterable[int]:
	num = 0
	while True:
		num += 1
		if num > nums:
			return
		yield num ** 2


for elem in MySqr(10):
	print(elem)

for elem in gen_my(10):
	print(elem)

for elem in (x ** 2 for x in range(1, 11)):
	print(elem)
