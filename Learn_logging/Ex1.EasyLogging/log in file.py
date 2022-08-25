import logging
import random
from typing import List


def luck_numbers(list_nums: List[int]) -> List[int]:
	luck_nums = [random.randint(min(list_nums) * -1, max(list_nums) * 2) for _ in range(10)]
	logging.debug("Список счастливых номеров сгенерированных функцией: {}".format(luck_nums))
	coincidences = [x for x in luck_nums for y in list_nums if x == y]
	if not coincidences:
		try:
			logging.warning("Не удача! Совпадений нет!")
			raise ValueError
		except ValueError:
			logging.exception("Совпадений нет!")
	return coincidences


if __name__ == "__main__":
	for _ in range(100):
		logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler("In file.log", "a", "utf-8")])

		random_nums = [random.randint(0, 9) for _ in range(10)]
		logging.info("Мой список получился такой: {}".format(random_nums))
		result = luck_numbers(random_nums)
		logging.info("Совпавшие числа: {}".format(result))
