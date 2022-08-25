import logging
import random
from typing import List


class AllInfo(logging.Filter):
	def filter(self, record):
		return record.levelname == "INFO"


class AllDebug(logging.Filter):
	def filter(self, record):
		return record.levelname == "DEBUG"


class Other(logging.Filter):
	def filter(self, record):
		return record.levelname != "DEBUG" and record.levelname != "INFO"


log_1 = logging.getLogger("Какой-то логгер")
log_1.setLevel(logging.INFO)

file_hand_info = logging.FileHandler("only_info.log", "a", 'utf-8')
format_hand_info = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_hand_info.setFormatter(format_hand_info)
file_hand_info.addFilter(AllInfo())

file_hand_debug = logging.FileHandler("only_debug.log", "a", 'utf-8')
format_hand_debug = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_hand_debug.setFormatter(format_hand_debug)
file_hand_debug.addFilter(AllDebug())

file_hand_other = logging.FileHandler("other.log", "a", 'utf-8')
format_hand_other = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_hand_other.setFormatter(format_hand_other)
file_hand_other.addFilter(Other())


log_1.addHandler(file_hand_info)
log_1.addHandler(file_hand_debug)
log_1.addHandler(file_hand_other)


def luck_numbers(list_nums: List[int]) -> List[int]:
	luck_nums = [random.randint(min(list_nums) * -1, max(list_nums) * 2) for _ in range(10)]
	log_1.debug("Список счастливых номеров сгенерированных функцией: {}".format(luck_nums))
	coincidences = [x for x in luck_nums for y in list_nums if x == y]
	if not coincidences:
		try:
			log_1.warning("Не удача! Совпадений нет!")
			raise ValueError
		except ValueError:
			log_1.exception("Совпадений нет!")
	return coincidences


if __name__ == "__main__":
	for _ in range(100):
		random_nums = [random.randint(0, 9) for _ in range(10)]
		log_1.info("Мой список получился такой: {}".format(random_nums))
		result = luck_numbers(random_nums)
		log_1.info("Совпавшие числа: {}".format(result))
