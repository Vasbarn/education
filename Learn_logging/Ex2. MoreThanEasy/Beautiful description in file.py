import logging
import random
from typing import List


def luck_numbers(list_nums: List[int]) -> List[int]:
	luck_nums = [random.randint(min(list_nums) * -1, max(list_nums) * 2) for _ in range(10)]
	my_log.debug("Список счастливых номеров сгенерированных функцией: {}".format(luck_nums))
	coincidences = [x for x in luck_nums for y in list_nums if x == y]
	if not coincidences:
		try:
			my_log.warning("Не удача! Совпадений нет!")
			raise ValueError
		except ValueError:
			my_log.exception("Совпадений нет!")
	return coincidences


if __name__ == "__main__":
	my_log = logging.getLogger("Логер_шмогер")
	my_log.setLevel(logging.DEBUG)
	file_hand = logging.FileHandler("B1.log", "a", 'utf-8')
	format_hand = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	file_hand.setFormatter(format_hand)
	my_log.addHandler(file_hand)

	for _ in range(100):
		random_nums = [random.randint(0, 9) for _ in range(10)]
		my_log.info("Мой список получился такой: {}".format(random_nums))
		result = luck_numbers(random_nums)
		my_log.info("Совпавшие числа: {}".format(result))
