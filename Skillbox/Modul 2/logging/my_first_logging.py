import logging
"""
DEBUG > INFO > WARING > ERROR > CRITICAL
"""


def func_1():
	try:
		for num in range(101):
			logging.debug("Я на числе {}".format(num))
			if num == 53:
				x = "test" / 2
	except Exception:
		logging.exception(f"Ошибка:")

def func_2():
	try:
		for word in "фывапролджюбьтимсчяйцукенгшщ":
			logging.debug("Я на букве {}".format(word))
	except Exception:
		logging.exception(f"Ошибка:")




if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	func_1()