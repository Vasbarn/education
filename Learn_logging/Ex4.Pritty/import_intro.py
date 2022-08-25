
from Logging_with_filter import log_1, luck_numbers
import random





for _ in range(100):
	random_nums = [random.randint(0, 9) for _ in range(10)]
	log_1.info("Мой список получился такой: {}".format(random_nums))
	result = luck_numbers(random_nums)
	log_1.info("Совпавшие числа: {}".format(result))
