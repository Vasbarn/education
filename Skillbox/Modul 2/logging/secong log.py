import logging
"""
DEBUG > INFO > WARING > ERROR > CRITICAL
"""


def func_1():
	try:
		for num in range(101):
			log.debug("Я на числе {}".format(num))
			if num == 53:
				x = "test" / 2
	except Exception:
		log.exception(f"Ошибка:")

def func_2():
	try:
		for word in "фывапролджюбьтимсчяйцукенгшщ":
			log2.debug("Я на букве {}".format(word))
	except Exception:
		log2.exception(f"Ошибка:")

if __name__ == "__main__":
	log = logging.getLogger("Логер функции 1")
	log.setLevel(logging.DEBUG)
	fh = logging.FileHandler("log_f1.log", "w", "utf-8")
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	fh.setFormatter(formatter)
	log.addHandler(fh)

	log2 = logging.getLogger("Логер функции 2")
	log2.setLevel(logging.DEBUG)
	fh = logging.FileHandler("log_f2.log", "w", "utf-8")
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	fh.setFormatter(formatter)
	log2.addHandler(fh)

	func_1()
	func_2()
